# -*- coding:utf-8 -*-

import inspect

def include_file(filename):
    file = open(filename, u'rb')
    str_lines = file.read();
    file.close();
    _locals = {}
    file_byte_code = compile(str_lines, filename, 'exec')
    exec(file_byte_code, globals(), _locals)
    _globals = globals()
    while len(_locals) > 0:
        temp_item = _locals.popitem();
        if inspect.isfunction(temp_item[1]) or inspect.ismodule(temp_item[1]):
            _globals[temp_item[0]] = temp_item[1]




if __name__ == "__main__":
    include_file(r"E:\5_Python\include_file\test.py")
    print locals()
    print globals()
    # test.test_print()
    test_print()
    print "Hello World"