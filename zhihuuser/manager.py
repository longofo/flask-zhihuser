#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22 19:12:17
# @Author  : wushilong
# @Email   : 1320185818@qq.com | longofo.wu@gmail.com
# @Link    : http://longofo.cc

import os
from flask_script import Manager, Shell
from app import create_app, mongo

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, mongo=mongo)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
