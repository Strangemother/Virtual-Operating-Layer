import sys
import os
from time import gmtime, strftime
from pybuild.steps import *


def main(buildfile_name=None, root_path=None, *args):
    parser = Parser(root_path, buildfile_name)
    result = parser.run()
    render(result)


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
        self.root_path = root_path
        abs_path = os.path.abspath(root_path)
        print('Parser set root_path', abs_path)

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
        build_fn = self.buildfile_name


        if build_fn is not None:
            bfp = os.path.join(self.abs_path, build_fn)
            if os.path.isfile(bfp):
                return bfp

        if len(opts) == 1:
            if build_fn is not None:
                print('ignoring given buildfile name "{}" as only one was discovered'.format(build_fn))
            else:
                print('Using buildfile', build_fn)
            return opts[0]

        if len(opts) == 0:
            print('No builderfile found')
            return None

        if build_fn is None:
            print('More then one buildfile exists, but no chosen name. "default" used. ')
            build_fn = 'default.builderfile'

        for path in opts:
            fne = os.path.basename(path)
            fn, ext = os.path.splitext(fne)

            if fn == build_fn or fn == build_fn:
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


def myfunc(session):
    print("myfunc session CWD:", session['CWD'])


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
