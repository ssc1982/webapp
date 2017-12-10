#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aiohttp
import asyncio
import json

from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.router.add_get('/', hello)
web.run_app(app, host='127.0.0.1')
for resource in app.router.resource():
    print(resource)