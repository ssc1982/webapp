#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models import User, Blog, Comment
import orm


def test():

    #yield from orm.create_pool(loop=u.save, user='root', password='password', database='mysql')

    u = User(name='Test', email='tset@example.com', passwd='12345', image='about:blank')
    yield from u.save()
    yield from orm.create_pool(loop=u.save, user='root', password='password', database='mysql')

for x in test():
    pass
