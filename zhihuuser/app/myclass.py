#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22 20:20:44
# @Author  : wushilong
# @Email   : 1320185818@qq.com | longofo.wu@gmail.com
# @Link    : http://longofo.cc


class MongoPaginate(object):
    def __init__(self, page, per_page, count):
        self.page = page
        self.prev_num = page - 1
        self.next_num = page + 1
        self.per_page = per_page
        self.pages = int(count / self.per_page) + \
            1 if count % self.per_page else int(
                count / self.per_page)

    @property
    def has_prev(self):
        return False if self.page == 1 else True

    @property
    def has_next(self):
        return False if self.page == self.pages else True

    def iter_pages(self):
        if self.page <= 5:
            for p in range(1, self.page + 1):
                yield p
        else:
            yield 1
            yield 2

        if self.page > 5:
            yield '...'
            yield self.page - 2
            yield self.page - 1
            yield self.page

        if self.pages - self.page > 4:
            yield self.page + 1
            yield self.page + 2
            yield '...'

        if self.pages - self.page <= 4:
            for p in range(self.page + 1, self.pages + 1):
                yield p
        else:
            yield self.pages - 1
            yield self.pages
