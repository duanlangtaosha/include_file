# -*- coding:utf-8 -*-

# 检查模块，用于检测是否是函数或模块等工能
import inspect

def include_file(filename):

    # 以二进制方式打开文件
    file = open(filename, u'rb')

    #读出文件
    str_lines = file.read();

    # 关闭文件
    file.close();

    #当前局部变量字典的变量
    _locals = {}

    # str_lines 传递进的字符串， filename可以是任一名字, exec是编译的类型
    file_byte_code = compile(str_lines, filename, 'exec')

    #执行exec会将globals的值赋值给_locals
    exec(file_byte_code, globals(), _locals)

    #_globals是引用而不是拷贝
    _globals = globals()
    while len(_locals) > 0:

        #返回的是字典方式的元组（key， value）
        temp_item = _locals.popitem();
        if inspect.isfunction(temp_item[1]) or inspect.ismodule(temp_item[1]) or inspect.isclass(temp_item[1]):
            if inspect.ismodule(temp_item[1]):

                #os模块，相当于import os, os_clone是指向
                os_clone = inspect.getmodule(temp_item[1])

                #os_clone.path和os.path一样的效果
                print os_clone.path

            #temp_item[0]是一个函数或者模块的字符串
            #temp_item[1]是一个函数或者模块的对象实例
            #_globals是一个字典，给相应的key赋值
            # print _globals
            # print globals()
            #在_globals字典中添加一个键值对
            _globals[temp_item[0]] = temp_item[1]
            # print _globals
            # print globals()
            # print _globals[temp_item[0]]

if __name__ == "__main__":

    #修改目录结构，放在include_file前会报错
    # import test
    include_file(r"E:\5_Python\include_file\test_dir\test.py")

    # 修改目录结构，放在include_file后会报错
    # import test
    print locals()
    print globals()
    test_print()
    print "Hello World"