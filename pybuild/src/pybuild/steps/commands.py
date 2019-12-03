import sys
import os
from time import gmtime, strftime
from string import Template
import json
import shlex

from pybuild.statement import Statement
from pybuild.template import template_str



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


class StepExecute(object):

    def step_exec(self):
        """Return a Statement instance for a persistent caller
        to self.echo"""
        return Statement(callback=self.exec_pyfile)

    def exec_pyfile(self, session, instruction):
        """Perform astandard echo to the std out"""
        import pdb; pdb.set_trace()  # breakpoint ef3eb8e6 //

        return True


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


class Steps(StepPrint, StepCallback, StepExecute, StepSettings,
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
