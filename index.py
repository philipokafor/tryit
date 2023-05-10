# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:12:29 2023

@author: okafop
"""
def app(request):
  return {"status": 200, "headers": {"Content-Type": "text/plain"}, "body": "Hello, World!"}