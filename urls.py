#!/usr/bin/env python
# -*- coding:utf-8 -*-


from controllers.CreateHandlers import MyTestHandler, CreateProjectHandler
from controllers.UeditHandlers import *

urls = list()

testUrls = [(r'/index', MyTestHandler), ]

createUrls = [
    (r'/CreateProject', CreateProjectHandler),
    (r'/UeditIndex.html', UeditIndexHandler),
    (r'/upload/', RemotePictureHandler),
]

urls += testUrls + createUrls
