#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22 20:20:44
# @Author  : wushilong
# @Email   : 1320185818@qq.com | longofo.wu@gmail.com
# @Link    : http://longofo.cc

from flask import render_template,request,jsonify
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        response = jsonify({'error':'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'),404

@main.app_errorhandler(500)#如果使用errorhandler修饰器,那么只有蓝本中的错误才能触发处理程序。要想在全局触发错误处理程序，必须使用app_errorhandler
def internal_server_error(e):
    if request.accept_mimetypes.accept_json and \
        not request.accept_mimetypes.accept_html:
        response = jsonify({'error':'Internal Server Error'})
        response.status_code = 500
        return response
    return render_template('500.html'),500