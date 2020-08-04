#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from my_unitest.console_color import ColorWritelnDecorator


class BaseTestCase(unittest.TestCase):
    color_write = ColorWritelnDecorator()

    def println(self, diy_str):
        self.color_write.yellow('[----PRINT----] %s' % diy_str)
        self.color_write.writeln()
