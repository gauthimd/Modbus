#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import datetime, time, random

while True:
  now1 = datetime.datetime.now()
  time.sleep(random.randint(1,3))
  now2 = datetime.datetime.now()
  delta = now2 - now1
  print(delta)

