#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models import User, Blog, Comment
import orm
import asyncio
import time
from orm import Model, StringField, BooleanField, FloatField, TextField


def test(loop):

    yield from orm.create_pool(loop=loop, user='root', password='password', db='mysql')
    u = User(name='Test', email='tset@example.com', passwd='12345', admin=False, image='about:blank')
    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()