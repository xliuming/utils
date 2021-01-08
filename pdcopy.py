#!/usr/bin/python
# -*-coding:utf-8-*-
import base64
import sys

buffer = []
for line in sys.stdin:
    buffer.append(line)

content = ''.join(buffer)
print('\033]52;c;' +base64.b64encode(content.encode()).decode()+'\007')
