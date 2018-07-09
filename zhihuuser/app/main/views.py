#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22 20:20:44
# @Author  : wushilong
# @Email   : 1320185818@qq.com | longofo.wu@gmail.com
# @Link    : http://longofo.cc


from . import main
from flask import render_template, request, g, jsonify, current_app, url_for
from .. import mongo
from .. myfunc import get_user_data
from ..myclass import MongoPaginate


# @main.before_app_request
# def before_request():
#     g.top_user = mongo.db.user.find().sort(
#         [("follower_count", -1)]).limit(20)


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    users = mongo.db.user.find().sort(
        [("follower_count", -1)]).skip(
        (page - 1) * current_app.config['PAGE_SIZE'] * 2).limit(
        current_app.config['PAGE_SIZE'] * 2)
    users = [user for user in users]

    pagination = MongoPaginate(
        page=page, per_page=current_app.config['PAGE_SIZE'] * 2, count=mongo.db.user.count())
    return render_template('main/index.html', users=users, pagination=pagination)


@main.route('/search')
def search():
    q = request.args.get('q', '#')
    page = request.args.get('page', 1, type=int)
    query = mongo.db.user.find({"$text": {"$search": q}})
    users = query.sort(
        "follower_count", -1).skip(
        (page - 1) * current_app.config['PAGE_SIZE']).limit(
        current_app.config['PAGE_SIZE'])
    count = query.count()

    pagination = MongoPaginate(
        page=page, per_page=current_app.config['PAGE_SIZE'], count=count)
    return render_template('main/search.html', users=users, pagination=pagination, q=q)


@main.route('/top')
def top():
    top_user = mongo.db.user.find().sort(
        [("follower_count", -1)]).limit(current_app.config['PAGE_SIZE'] + 2)
    users_info = [{'headline': get_user_data(user['headline']),
                   'avatar_url': get_user_data(user['avatar_url']),
                   'name': get_user_data(user['name']),
                   'follower_count': get_user_data(user['follower_count']),
                   'url_token':get_user_data(user['url_token'])}
                  for user in top_user]
    return jsonify(users_info)


@main.route('/userCount')
def get_user_count():
    user_count = mongo.db.user.count()
    return jsonify(user_count)
