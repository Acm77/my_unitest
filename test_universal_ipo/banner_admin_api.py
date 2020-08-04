#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import unittest
import requests
from urlparse import urljoin
from common import utils
from my_unitest.my_test_style import MyTestRunner
from my_unitest.base_test_case import BaseTestCase


class TestUniversalIpoBannerAdminApi(BaseTestCase):
    base_url = 'http://127.0.0.1:8001'
    url = urljoin(base_url, '/backend-activity-admin/api/v1/admin/universal_ipo/banner')

    # 需配置的数据
    banner_id = 10
    template_id = 11

    def test_post(self):
        banner_info = dict(
            template_id=self.template_id,
            cn_banner_url="https://pic.17qq.com/uploads/wfpmhnnhsy.jpeg",
            en_banner_url="https://pic.17qq.com/uploads/dgkhmppmlv.jpeg",
            start_time=utils.current_time(),
            end_time=utils.current_time(),
        )
        res = requests.post(self.url, data=banner_info)
        self.assertEqual(u'{"error_msg": "", "is_succ": true}', res.text)

    def test_get(self):
        res = requests.get(self.url, params={'template_id': self.template_id})
        self.assertIn('https://pic.17qq.com/uploads/wfpmhnnhsy.jpeg', res.text)

    def test_put(self):
        banner_info = dict(
            banner_id=self.banner_id,
            cn_banner_url="https://pic.17qq.com/uploads/wfpmhnnhsy.jpeg",
            en_banner_url="https://pic.17qq.com/uploads/dgkhmppmlv.jpeg",
            start_time=utils.current_time(),
            end_time=utils.current_time(),
        )
        res = requests.put(self.url, data=banner_info)
        self.assertEqual(u'{"error_msg": "", "is_succ": true}', res.text)

    def test_patch(self):
        res = requests.patch(self.url, data={'banner_id': self.banner_id, 'status': 0})
        self.assertEqual(u'{"error_msg": "", "is_succ": true}', res.text)

    def test_delete(self):
        res = requests.delete(self.url, params={'banner_id': self.banner_id, 'archive': 0})
        self.assertEqual(u'{"error_msg": "", "is_succ": true}', res.text)


if __name__ == '__main__':
    unittest.main(testRunner=MyTestRunner())
