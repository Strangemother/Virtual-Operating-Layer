"""Using cython, build the libs into the envs for copy
"""
import pyximport
import os
import sys
import shutil


SETTINGS = None

def main(settings):
    global SETTINGS
    SETTINGS = settings

    build_c_extensions()

def build_c_extensions():

    out_dir = "{OUTPUT_PATH}/{LIB_TARGET_NAME}/{TARGET_LIB_NAME}".format(**SETTINGS)
    #build_libs = os.path.join(out_dir, SETTINGS['LIB_TARGET_NAME'])
    build_libs = os.path.abspath(out_dir)
    temp_dir = 'TEMP'
    comp_dir = 'COMPILED'

    print('Building c extensions to "{}"'.format(build_libs))

    if os.path.exists('setup.py'):
        print('Compiling addons')
        # python setup.py build_ext
        sys.argv += ['build_ext', '--inplace', '--build-temp', temp_dir]
        print(sys.argv)
        import setup


    if os.path.isdir(temp_dir):
        print('Deleting target folder "{}"'.format(temp_dir))
        shutil.rmtree(temp_dir)
        assert os.path.exists(temp_dir) is False
        print('Deleted.')

    if os.path.isdir(comp_dir):
        print('Success. Copying to "{}"'.format(out_dir))
        # copy to the correct location
        if os.path.isdir(out_dir):
            print('Deleting target folder "{}"'.format(out_dir))
            shutil.rmtree(out_dir)
            assert os.path.exists(out_dir) is False
            print('Deleted.')

        print('Copying "{}" to "{}"'.format(comp_dir, out_dir))
        shutil.copytree(comp_dir, out_dir)

        print('Deleting COMPILED/ folder')
        shutil.rmtree(comp_dir)
        assert os.path.exists(comp_dir) is False
        print('Deleted.')
    print('C Lib complete at: "{}"'.format(out_dir))



