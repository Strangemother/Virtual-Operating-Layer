/* Generated code for Python source for module '__main__'
 * created by Nuitka version 0.6.1rc9
 *
 * This code is in part copyright 2018 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "__helpers.h"

/* The _module___main__ is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module___main__;
PyDictObject *moduledict___main__;

/* The module constants used, if any. */
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain___main__;
extern PyObject *const_str_plain___cached__;
extern PyObject *const_int_0;
static PyObject *const_str_plain_sys;
static PyObject *const_str_plain_os;
extern PyObject *const_str_plain_site;
static PyObject *const_str_digest_7e86cad3d33d2eccd1b2858422796924;
static PyObject *const_str_plain___annotations__;
static PyObject *const_str_angle_module;
extern PyObject *const_str_plain_print;
static PyObject *const_str_plain_a;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_types;
static PyObject *const_str_digest_fe7811365b4cff3d43d1d212699c3b4d;
extern PyObject *const_tuple_empty;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_plain_sys = UNSTREAM_STRING_ASCII( &constant_bin[ 0 ], 3, 1 );
    const_str_plain_os = UNSTREAM_STRING_ASCII( &constant_bin[ 3 ], 2, 1 );
    const_str_digest_7e86cad3d33d2eccd1b2858422796924 = UNSTREAM_STRING_ASCII( &constant_bin[ 5 ], 55, 0 );
    const_str_plain___annotations__ = UNSTREAM_STRING_ASCII( &constant_bin[ 60 ], 15, 1 );
    const_str_angle_module = UNSTREAM_STRING_ASCII( &constant_bin[ 75 ], 8, 0 );
    const_str_plain_a = UNSTREAM_STRING_ASCII( &constant_bin[ 15 ], 1, 1 );
    const_str_digest_fe7811365b4cff3d43d1d212699c3b4d = UNSTREAM_STRING_ASCII( &constant_bin[ 83 ], 19, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants___main__( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_4e88adc24e0a5df505ee97f7484b79f4;
/* For use in "MainProgram.c". */
PyCodeObject *codeobj_main = NULL;

static void createModuleCodeObjects(void)
{
    module_filename_obj = const_str_digest_7e86cad3d33d2eccd1b2858422796924;
    codeobj_4e88adc24e0a5df505ee97f7484b79f4 = MAKE_CODEOBJ( module_filename_obj, const_str_angle_module, 1, const_tuple_empty, 0, 0, CO_NOFREE );
    codeobj_main = codeobj_4e88adc24e0a5df505ee97f7484b79f4;
}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef___main__ =
{
    PyModuleDef_HEAD_INIT,
    "__main__",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

extern PyObject *const_str_plain___package__;

#if PYTHON_VERSION >= 300
extern PyObject *const_str_dot;

extern PyObject *const_str_plain___loader__;
#endif

#if PYTHON_VERSION >= 340
extern PyObject *const_str_plain___spec__;
extern PyObject *const_str_plain__initializing;
extern PyObject *const_str_plain_submodule_search_locations;
#endif

extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();
#if PYTHON_VERSION >= 350
extern void _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
extern void _initCompiledAsyncgenTypes();
#endif

extern PyTypeObject Nuitka_Loader_Type;

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( __main__ )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module___main__ );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    /* Initialize the compiled types of Nuitka. */
    _initCompiledCellType();
    _initCompiledGeneratorType();
    _initCompiledFunctionType();
    _initCompiledMethodType();
    _initCompiledFrameType();
#if PYTHON_VERSION >= 350
    _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
    _initCompiledAsyncgenTypes();
#endif

#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
    puts("__main__: Calling setupMetaPathBasedLoader().");
#endif
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 300
    patchInspectModule();
#endif

#endif

    /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleConstants().");
#endif
    createModuleConstants();

    /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleCodeObjects().");
#endif
    createModuleCodeObjects();

    // puts( "in init__main__" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module___main__ = Py_InitModule4(
        "__main__",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No "__doc__" is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else

    module___main__ = PyModule_Create( &mdef___main__ );
#endif

    moduledict___main__ = MODULE_DICT( module___main__ );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        PyObject *module_name = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__ );

        UPDATE_STRING_DICT1(
            moduledict___main__,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 300
        PyObject *module_name = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__ );
        char const *module_name_cstr = PyString_AS_STRING( module_name );

        char const *last_dot = strrchr( module_name_cstr, '.' );

        if ( last_dot != NULL )
        {
            UPDATE_STRING_DICT1(
                moduledict___main__,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize( module_name_cstr, last_dot - module_name_cstr )
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__ );
        Py_ssize_t dot_index = PyUnicode_Find( module_name, const_str_dot, 0, PyUnicode_GetLength( module_name ), -1 );

        if ( dot_index != -1 )
        {
            UPDATE_STRING_DICT1(
                moduledict___main__,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring( module_name, 0, dot_index )
            );
        }
#endif
#endif
    }

    CHECK_OBJECT( module___main__ );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PyImport_GetModuleDict(), const_str_plain___main__, module___main__ );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if ( GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if !defined(_NUITKA_EXE) || !1
        value = PyModule_GetDict( value );
#endif

        UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___builtins__, value );
    }

#if PYTHON_VERSION >= 300
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type );
#endif

#if PYTHON_VERSION >= 340
#if 1
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___spec__, Py_None );
#else
    {
        PyObject *bootstrap_module = PyImport_ImportModule("importlib._bootstrap");
        CHECK_OBJECT( bootstrap_module );
        PyObject *module_spec_class = PyObject_GetAttrString( bootstrap_module, "ModuleSpec" );
        Py_DECREF( bootstrap_module );

        PyObject *args[] = {
            GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__ ),
            (PyObject *)&Nuitka_Loader_Type
        };

        PyObject *spec_value = CALL_FUNCTION_WITH_ARGS2(
            module_spec_class,
            args
        );

#if 0
        SET_ATTRIBUTE( spec_value, const_str_plain_submodule_search_locations, PyList_New(0) );
#endif

        SET_ATTRIBUTE( spec_value, const_str_plain__initializing, Py_True );

        UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain___spec__, spec_value );

        Py_DECREF( module_spec_class );
    }
#endif
#endif


    // Temp variables if any
    struct Nuitka_FrameObject *frame_4e88adc24e0a5df505ee97f7484b79f4;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;

    // Module code.
    // Frame without reuse.
    frame_4e88adc24e0a5df505ee97f7484b79f4 = MAKE_MODULE_FRAME( codeobj_4e88adc24e0a5df505ee97f7484b79f4, module___main__ );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_4e88adc24e0a5df505ee97f7484b79f4 );
    assert( Py_REFCNT( frame_4e88adc24e0a5df505ee97f7484b79f4 ) == 2 );

    // Framed code:
    {
    PyObject *tmp_name_name_1;
    PyObject *tmp_level_name_1;
    PyObject *tmp_imported_value_1;
    tmp_name_name_1 = const_str_plain_os;
    tmp_level_name_1 = const_int_0;
    frame_4e88adc24e0a5df505ee97f7484b79f4->m_frame.f_lineno = 1;
    tmp_imported_value_1 = IMPORT_MODULE_KW( tmp_name_name_1, NULL, NULL, NULL, tmp_level_name_1 );
    if ( tmp_imported_value_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_imported_value_1 );
    }
    {
    PyObject *tmp_name_name_2;
    PyObject *tmp_level_name_2;
    PyObject *tmp_imported_value_2;
    tmp_name_name_2 = const_str_plain_sys;
    tmp_level_name_2 = const_int_0;
    frame_4e88adc24e0a5df505ee97f7484b79f4->m_frame.f_lineno = 1;
    tmp_imported_value_2 = IMPORT_MODULE_KW( tmp_name_name_2, NULL, NULL, NULL, tmp_level_name_2 );
    assert( !(tmp_imported_value_2 == NULL) );
    Py_DECREF( tmp_imported_value_2 );
    }
    {
    PyObject *tmp_name_name_3;
    PyObject *tmp_level_name_3;
    PyObject *tmp_imported_value_3;
    tmp_name_name_3 = const_str_plain_types;
    tmp_level_name_3 = const_int_0;
    frame_4e88adc24e0a5df505ee97f7484b79f4->m_frame.f_lineno = 1;
    tmp_imported_value_3 = IMPORT_MODULE_KW( tmp_name_name_3, NULL, NULL, NULL, tmp_level_name_3 );
    if ( tmp_imported_value_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_imported_value_3 );
    }
    {
    PyObject *tmp_name_name_4;
    PyObject *tmp_level_name_4;
    PyObject *tmp_imported_value_4;
    tmp_name_name_4 = const_str_plain_site;
    tmp_level_name_4 = const_int_0;
    frame_4e88adc24e0a5df505ee97f7484b79f4->m_frame.f_lineno = 1;
    tmp_imported_value_4 = IMPORT_MODULE_KW( tmp_name_name_4, NULL, NULL, NULL, tmp_level_name_4 );
    if ( tmp_imported_value_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_imported_value_4 );
    }
    {
    PyObject *tmp_assign_source_1;
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    }
    {
    PyObject *tmp_assign_source_2;
    tmp_assign_source_2 = const_str_digest_7e86cad3d33d2eccd1b2858422796924;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    }
    {
    PyObject *tmp_assign_source_3;
    tmp_assign_source_3 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___cached__, tmp_assign_source_3 );
    }
    {
    PyObject *tmp_assign_source_4;
    tmp_assign_source_4 = PyDict_New();
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain___annotations__, tmp_assign_source_4 );
    }
    {
    PyObject *tmp_assign_source_5;
    tmp_assign_source_5 = const_str_digest_fe7811365b4cff3d43d1d212699c3b4d;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain_a, tmp_assign_source_5 );
    }
    {
    PyObject *tmp_called_name_1;
    PyObject *tmp_call_result_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_mvar_value_1;
    tmp_called_name_1 = LOOKUP_BUILTIN( const_str_plain_print );
    assert( tmp_called_name_1 != NULL );
    tmp_mvar_value_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_a );

    if (unlikely( tmp_mvar_value_1 == NULL ))
    {
        tmp_mvar_value_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_a );
    }

    CHECK_OBJECT( tmp_mvar_value_1 );
    tmp_args_element_name_1 = tmp_mvar_value_1;
    frame_4e88adc24e0a5df505ee97f7484b79f4->m_frame.f_lineno = 2;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_call_result_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    if ( tmp_call_result_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_call_result_1 );
    }

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_4e88adc24e0a5df505ee97f7484b79f4 );
#endif
    popFrameStack();

    assertFrameObject( frame_4e88adc24e0a5df505ee97f7484b79f4 );

    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_4e88adc24e0a5df505ee97f7484b79f4 );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_4e88adc24e0a5df505ee97f7484b79f4, exception_lineno );
    }
    else if ( exception_tb->tb_frame != &frame_4e88adc24e0a5df505ee97f7484b79f4->m_frame )
    {
        exception_tb = ADD_TRACEBACK( exception_tb, frame_4e88adc24e0a5df505ee97f7484b79f4, exception_lineno );
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;

    frame_no_exception_1:;

#if _NUITKA_EXPERIMENTAL_PKGUTIL_ITERMODULES
#if 0 && 1
    {
        PyObject *path_value = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___path__ );

        if (path_value && PyList_CheckExact(path_value) && PyList_Size(path_value) > 0)
        {
            PyObject *path_element = PyList_GetItem( path_value, 0 );

            PyObject *path_importer_cache = PySys_GetObject((char *)"path_importer_cache");
            CHECK_OBJECT( path_importer_cache );

            int res = PyDict_SetItem( path_importer_cache, path_element, (PyObject *)&Nuitka_Loader_Type );
            assert( res == 0 );
        }
    }
#endif
#endif

    return MOD_RETURN_VALUE( module___main__ );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
