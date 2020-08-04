#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import unittest
import requests
from urlparse import urljoin
from my_unitest.my_test_style import MyTestRunner
from my_unitest.base_test_case import BaseTestCase


class TestUniversalIpoGossipAdminApi(BaseTestCase):
    base_url = 'http://127.0.0.1:8001'
    url = urljoin(base_url, '/backend-activity-admin/api/v1/admin/universal_ipo/gossip')

    # 需配置的数据
    gossip_id = 4
    template_id = 11

    def test_post(self):
        gossip_info = dict(
            template_id=self.template_id,
            sort=1,
            content='我是正文',
        )
        res = requests.post(self.url, data=gossip_info)
        self.assertEqual(u'{"error_msg": "", "is_succ": true}', res.text)

    def test_get(self):
        res = requests.get(self.url, params={'template_id': self.template_id})
        self.assertIn(u'我是正文', res.text)

    def test_delete(self):
        res = requests.delete(self.url, params={'gossip_id': self.gossip_id})
        self.assertEqual(u'{"error_msg": "", "is_succ": true}', res.text)


if __name__ == '__main__':
    unittest.main(testRunner=MyTestRunner())
