import sys
import os
from time import gmtime, strftime

def main(buildfile_name=None, root_path=None, *args):
    print("Parsing", root_path)
    parser = Parser(root_path, buildfile_name)
    result = parser.run()
    render(result)



from string import Template

def convert_templated(src_path, dest_path=None, kwargs=None):
    """Convert a given tpy file to a standard py file. If the dest path
    is None, the src_path is used resulting in a tpy/py in the same directory
    """

    print('\nConverting tpy file')
    content = ''
    with open(src_path, 'r') as stream:
        for line in stream:
            content += line

    data = kwargs or SETTINGS
    if dest_path is None:
        dirn, filen = os.path.split(src_path)
        dest_path = os.path.join(dirn, filen)
        print('writing to "{}"'.format(dest_path))

    with open(dest_path, 'w') as stream:
        stream.write(Template(content).safe_substitute(data))


def template_str(content, data):
    return Template(content).safe_substitute(data)


class Parser(object):
    settings = None

    def __init__(self, root_path=None, buildfile_name=None):
        # Base location of CWD init.
        root_path = root_path or '.'
        # parser config.
        self.settings = self.settings or {}
        # name of the chosen buildfile if multiple exist.
        self.buildfile_name = buildfile_name
        self.set_root(root_path)
        # Record all active args
        self.session = self.create_session()

    def set_root(self, root_path):
        print('Parser from root_path', root_path)
        self.root_path = root_path
        abs_path = os.path.abspath(root_path)

        if os.path.isfile(abs_path):
            print('Given root is a file. Fixing...')
            abs_path = os.path.dirname(abs_path)
        self.abs_path = abs_path


    def create_session(self):
        """Generate the diction environment shared across all steps.
        """
        res = dict(
            BUILDERFILE_NAME=self.buildfile_name,
            ROOT_DIR=self.abs_path,
            START_TIME=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
            )

        return res

    def run(self):
        """Discover and run the buildfile
        Returns:
            tuple -- (index, success, instruction)
        """
        filepath = self.discover_buildfile()
        instructions = self.read(filepath)

        self.init_session(filepath, instructions)
        return self.run_instructions(instructions)

    def init_session(self, filepath, instructions):
        absdir = os.path.dirname(filepath)
        addon = dict(
            BUILDFILE_PATH=filepath,
            BUILDFILE_DIR=absdir,
            TARGET_NAME='build',
            )
        addon['CWD'] = absdir
        addon['TARGET'] = os.path.join(absdir, addon['TARGET_NAME'])
        self.session.update(addon)



    def run_instructions(self, instructions):
        self.session['instructions'] = instructions
        steps = Steps(self.session, self)
        #print('Run instructions,', steps.session)
        isc = len(instructions)
        instructions.setup(steps)
        isc2 = len(instructions)
        print("\n  --- Total instructions: {} (+{}) ---\n".format(isc2, isc2 - isc))
        return instructions.execute(steps)


    def discover_buildfile(self):
        path = self.pick_buildfile()
        if path is None:
            print("Did not discover buildfile in path", path)
            return False

        print('Using buildfile:', path)
        return path

    def pick_buildfile(self):
        # Select a chosen buildfile from the options
        # or default to one.
        opts = self.get_buildfile_options()
        bfn = self.buildfile_name

        if len(opts) == 1:
            if bfn is not None:
                print('ignoring given buildfile name "{}" as only one was discovered'.format(bfn))
            return opts[0]

        if len(opts) == 0:
            print('No builderfile found')
            return None

        if bfn is None:
            print('More then one buildfile exists, but no chosen name. "default" used. ')
            bfn = 'default.builderfile'

        for path in opts:
            fne = os.path.basename(path)
            fn, ext = os.path.splitext(fne)

            if fn == bfn or fn == bfn:
                return path

    def get_buildfile_options(self):
        buildfile_name = 'buildfile'
        buildfile_ext = '.{}'.format(buildfile_name)
        names = [buildfile_name, buildfile_ext]
        opts = []
        # Find the buildfile.
        if os.path.isfile(self.abs_path):
            opts.append(self.abs_path)
        else:
            for root, dirs, files in os.walk(self.abs_path):
                for filename in files:
                    # Capture any file called .buildfile.
                    if filename in names:
                        opts.append(os.path.join(root, filename))
                        continue
                    # Any file with the extension of .buildfile
                    if os.path.splitext(filename)[1] == buildfile_ext:
                        opts.append(os.path.join(root, filename))
        return opts

    def read(self, filepath):
        """Read the builderfile, returning a list of instructions"""
        with open(filepath) as stream:
            lines = [x.rstrip() for x in stream.readlines()]

        instructions = Instructions(lines)
        return instructions


def render(parser_result):

    for index, success, instr in parser_result:
        line = '#{} - {}: {}'.format(index, instr.type(), success)
        if success == PASS:
            continue
            line = '#{} passed'.format(index)
        print(line)


import json

class StepCWD(object):
    def step_cwd(self):
        #print('cwd')
        return Statement(
            setup=self.set_init_cwd,
            callback=self.set_cwd)

    def set_init_cwd(self, session, instruction):
        #session['foo'] =1
        print('setup called init function', session)

    def set_cwd(self, session, instruction):
        val = instruction.value(session)
        path = self.resolve_path(val)
        session['CWD'] = path
        os.chdir(path)
        #print('Call CWD with args', path)
        return True


class StepTarget(object):
    def step_target(self):
        #print('target')
        return Statement(callback=self.set_target)

    def set_target(self, session, instruction):
        """Set the output directory of the buildfile procedure"""
        path = self.resolve_path(instruction.value(session))
        #print('Target', path)
        if os.path.exists(path) is False:
            print('Creating target directory', path)
            os.makedirs(path)
        session['TARGET'] = path
        return True


class StepSettings(object):
    def step_settings(self):
        #print('settings')
        return Statement(
            setup=self.preload_settings,
            callback=self.load_settings)

    def preload_settings(self, session, instruction):
        val = instruction.value(session)
        fp = self.resolve_path(val)
        exists = os.path.exists(fp)
        if exists is False:
            print("\nERROR: File does not exist", fp, '\n')
            self._cache[val] = None
        else:
            with open(fp) as stream:
                content = json.load(stream)
            self._cache[val] = content

        return self._cache[val]

    def load_settings(self, session, instruction):
        """Update the session with the filepath given in the SETTINGS
        instruction.
        the content is attempted from the _cache. If the content does
        not exist, the data is collected using preload_settings.
        """
        val = instruction.value(session)
        content = self._cache.get(val, self.preload_settings(session, instruction))
        session.update(content)
        print("\nLoaded settings:", session.keys())
        return True


class StepCallback(object):

    def step_arg(self):
        """Return a Statement instance with a persistent caller to
        self.arg_callback."""
        return Statement(
            #setup=self.set_init_arg,
            callback=self.arg_callback)

    def arg_callback(self, session, instruction):
        """Set the session key:value given in the instruction."""
        val = template_str(instruction.statement, session)
        aa, *bb = val.split()[1:]
        print('\nSet {} to "{}"\n'.format(aa, bb))
        session[aa] = ' '.join(bb)
        return True


    def set_init_arg(self, session, instruction):
        instruction.execute(session, self)
        #print('setup called init function', session)


class StepPrint(object):

    def step_print(self):
        """Return a Statement instance for a persistent caller
        to self.echo"""
        return Statement(callback=self.echo)

    def echo(self, session, instruction):
        """Perform astandard echo to the std out"""
        print("\n!! ", instruction.value(session), '\n')
        return PASS


class StepExec(object):

    def step_exec(self):
        """Return a Statement instance for a persistent caller
        to self.echo"""
        return Statement(callback=self.exec_py)

    def exec_py(self, session, instruction):
        """Perform astandard echo to the std out"""
        v = exec(instruction.value(session))
        return True


def myfunc(session):
    print("myfunc session CWD:", session['CWD'])


class StepCMD(object):

    def step_cmd(self):
        #print('cmd')
        return Statement(callback=self.perform_cmd)

    def perform_cmd(self, session, instruction):
        return os.system(instruction.value(session)) == 0


class StepCopy(object):
    """
    Copy one or more files and folders to a destination location.
    The COPY targets are relative from the buildfile working directory -
    being the CWD.
    The destination is relative to the

    """
    def step_copy(self):
        return Statement(callback=self.perform_copy)

    def perform_copy(self, session, instruction):
        """Copy a file or folder from the target to the dest.
        """
        val = instruction.value(session)
        print('\n-- COPY func on', val)
        t_paths, dest = self.extract_paths(val, session)
        print('To:   ', dest)
        print('Copy: ', t_paths)
        return True

    def extract_paths(self, string, session=None):
        # extract the target and destination from the given string
        # relative to the CWD anf TARGET directories.
        splits = shlex.split(string)
        splits.reverse()
        target = self.get_target(session)
        dest, *targets = splits
        if len(targets) == 0 and dest != '':
            targets = [dest]
            dest = target

        if dest.startswith('/'):
            # Defined as '_root_'  null it.
            print('Stripping leading slash from output sub directory', dest)
            dest = dest[1:]
        _targets = []
        for tp in targets:
            if tp.startswith('/'):
                # Defined as '_root_'  null it.
                print('Stripping leading slash from output sub directory', tp)
                tp = tp[1:]
            path = os.path.normpath(os.path.join(self.get_cwd(), tp))
            _targets.append(path)
        dest = os.path.normpath(os.path.join(target, dest))

        return _targets, dest


class StepInclude(object):
    """
    INCLUDE another build file inline with the current build file.
    When executing - there is no distinction between current and included
    build statements.

    The INCLUDE statement uses a setup() on the initial returned statement,
    injecting the additional arguments by loading the filepath pointer as
    another Instructions and injecting the build statements.
    """
    # def step_include(self):
    #     return Statement(callback=self.perform_include)

    # def perform_include(self, session, instruction):
    #     """Copy a file or folder from the target to the dest.
    #     """
    #     val = instruction.value(session)
    #     print('\n-- COPY func on', val)
    #     t_paths, dest = self.extract_paths(val, session)
    #     print('To:   ', dest)
    #     print('Copy: ', t_paths)
    #     return True

    def step_include(self):
        return Statement(expand=True, setup=self.setup_include)

    def setup_include(self, session, instruction):
        instructions = session['instructions']
        index = instructions.index(instruction)
        instructions.remove(index)
        path = os.path.join(session.get('CWD'), instruction.value(session))
        includes = self.parser.read(path)
        instructions.inject(index, includes.items)
        session['instructions'] = instructions
        return instructions

import shlex


class Steps(StepPrint, StepCallback, StepSettings,
            StepTarget, StepCWD, StepExec, StepCMD,
            StepCopy, StepInclude):

    def __init__(self, session, parser):
        self.session = session
        self.parser = parser
        self._cache = {}

    def get_instruction(self, name_type):
        # print('Steps::get_instruction', name_type)
        name = "step_{}".format(name_type)
        method = getattr(self, name, self.step_none)
        return method()

    def step_none(self):
        return Statement(inactive=True)

    def __len__(self):
        return len(self.session['instructions'])

    def __getitem__(self, index):
        return self.session['instructions'][index]

    def get_cwd(self):
        return self.session['CWD']

    def get_target(self, session=None):
        target = (session or self.session).get('TARGET')
        return target

    def step_execute(self):
        print('execute')
        return Statement()

    def resolve_path(self, path):
        """Given a path, return an absolute path relative from
        the correct working directory."""
        if os.path.isabs(path):
            # no change.
            return path
        # Relative from the given CWD - originally the buildfile location.
        cwd = self.get_cwd()
        return os.path.abspath(os.path.join(cwd, path))


class Statement(object):

    def __init__(self, expand=False, inactive=False, **kwargs):
        """expand: Does this statement contain many statements"""
        self.expand = expand
        self.inactive = inactive
        self.callback = kwargs.get('callback', None)
        self.__dict__.update(kwargs)


PASS = '__PASS__'
FAIL = '__FAIL__'


class Instruction(object):

    def __init__(self, statement):
        #print('New instructions')
        self.statement = statement

    def __str__(self):
        return str(self.statement)

    def __eq__(self, other):
        return self.statement == other

    def __repr__(self):
        return '<Instruction: "{}">'.format(self.statement)

    def type(self):
        return self.statement.split(' ')[0].lower()

    def value(self, session):
        val = template_str(self.statement, session)
        aa, *bb = val.split()
        return ' '.join(bb)

    def is_statement(self):
        return self.is_empty() is False and self.is_comment() is False

    def is_empty(self, val=None):
        val = val or self.statement.lstrip()
        return len(val) == 0

    def is_comment(self, val=None):
        comments = ['#', ';']
        val = val or self.statement.lstrip()

        if self.is_empty(val):
            return False

        return val[0] in comments

    def setup(self, session, steps):
        """Called before any steps execute their ststements.
        Administer the session with init vars
        """
        return self.execute(session, steps, statement_func='setup')

    def execute(self, session, steps, statement_func='callback'):

        val = self.statement
        if self.is_statement() is False:
            return PASS

        print('Execute "{}" {}'.format(val, self))
        statement = steps.get_instruction(self.type())
        # call the statement.step_x function.
        method = getattr(statement, statement_func, None)
        if method:
            return method(session, self)
        return FAIL

    def statements(self):
        """Return all statements for this instuction. This
        will be one or more
        """
        return [self.statement]


class Instructions(object):

    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return Instruction(self.items[index])

    def __len__(self):
        v = filter(None, (Instruction(x).is_statement() for x in self.items))
        return len(tuple(v))

    def setup(self, steps):
        res = []
        for index, item in enumerate(self.items):
            inst = Instruction(self.items[index])
            inst.setup(steps.session, steps)
            res += inst.statements()
        return res

    def execute(self, steps, method='execute'):
        statements = self._extract_statements(steps)
        print("\n -- Running {} Statements of {} Lines".format(len(statements), len(self)))
        res = ()
        counter = 0

        for index, instr in enumerate(self):
            if instr.is_statement():
                counter += 1
                print('\n#{}/{} - St.{}::{}'.format(
                        counter,
                        len(statements),
                        index,
                        instr.type().upper()
                    )
                )
            #Instruction.execute
            success = getattr(instr, method)(steps.session, steps)
            res += ( (index, success, instr,), )
        return res

    def _extract_statements(self, _iterable=None):
        _iterable = _iterable or self
        ll = len(_iterable)

        statements = []
        counter = 0
        for instr in _iterable:
            if instr.is_statement():
                statements.append(instr)
        return statements

    def index(self, item):
        """Given an item, return its inter index"""
        for index, _item in enumerate(self.items):
            if _item == item:
                return index
        raise StopIteration()

    def remove(self, index):
        self.items.remove(self.items[index])

    def inject(self, index, values):
        items = self.items
        result = items[0:index] + values +  items[index:]
        self.items = result




if __name__ == '__main__':
    main(*sys.argv[1:])
