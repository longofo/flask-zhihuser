#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22 20:20:44
# @Author  : wushilong
# @Email   : 1320185818@qq.com | longofo.wu@gmail.com
# @Link    : http://longofo.cc

from flask import Blueprint


main = Blueprint('main', __name__)

from . import views, errors
