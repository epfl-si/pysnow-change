# -*- coding:utf-8 -*-

"""
(c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2018.
"""
import unittest
import os
from pysnow_change_epfl.change_utils import check_sciper, check_pwd, get_changelog_info


class TestChangeUtils(unittest.TestCase):

    def test_check_sciper(self):
        if os.environ.get("SCIPER") is not None:
            del os.environ["SCIPER"]
        self.assertRaises(Exception, lambda: check_sciper())
        os.environ["SCIPER"] = "111s"
        self.assertRaises(Exception, lambda: check_sciper())
        os.environ["SCIPER"] = "1234567"
        self.assertRaises(Exception, lambda: check_sciper())
        os.environ["SCIPER"] = "abcdef"
        self.assertRaises(Exception, lambda: check_sciper())
        os.environ["SCIPER"] = "abcdefg"
        self.assertRaises(Exception, lambda: check_sciper())
        os.environ["SCIPER"] = "123456"

    def test_check_pwd(self):
        if os.environ.get("SNOW_CHG_PWD") is not None:
            del os.environ["SNOW_CHG_PWD"]
        self.assertRaises(Exception, lambda: check_pwd())

    def test_get_changelog_info(self):
        version_number, description, impact_category = get_changelog_info(
            'test-CHANGELOG.md')
        self.assertEqual(version_number, "v2.0.1", 'incorrect version')
        self.assertEqual(description, "\n  - Rewrite code\n  - Move to " +
                         "david-dm (watching deps)\n\n",
                         'incorrect description')
        self.assertEqual(impact_category, "Minor", 'incorrect impact category')


if __name__ == '__main__':
    unittest.main()
