#include <Python.h>

static PyObject *StringTooShortError = NULL;

static PyObject *method_fputs(PyObject *self, PyObject *args) {
    char *str, *filename = NULL;
    int bytes_copied = -1;

    /* Parse arguments */
    if(!PyArg_ParseTuple(args, "ss", &str, &filename)) {
        return NULL;
    }

    if (strlen(str) <= 0) {
        PyErr_SetString(StringTooShortError, "String length must be greater than 0");
        return NULL;
    }

    FILE *fp = fopen(filename, "w");
    bytes_copied = fputs(str, fp);
    fclose(fp);

    return PyLong_FromLong(bytes_copied);
}


static PyMethodDef FputsMethods[] = {
    {"fputs", method_fputs, METH_VARARGS, "Python interface for fputs C library function"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fputsmodule = {
    PyModuleDef_HEAD_INIT,
    "fputs",
    "Python interface for the fputs C library function",
    -1,
    FputsMethods
};


PyMODINIT_FUNC PyInit_fputs(void) {
    /* Assign module value */
    PyObject *module = PyModule_Create(&fputsmodule);
    /* Initialize new exception object */
    StringTooShortError = PyErr_NewException("fputs.StringTooShortError", NULL, NULL);
    /* Add exception object to your module */
    PyModule_AddObject(module, "StringTooShortError", StringTooShortError);

    return module;
}
