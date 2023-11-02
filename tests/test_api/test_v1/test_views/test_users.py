#!/usr/bin/python3
"""Test for api v1 Flask App"""

from api.v1.app import app
import pep8
import unittest


class TestAppDocs(unittest.TestCase):
    """class for testing Falsk App Docs"""

    def test_doc_file(self):
        """...documentation for the file"""
        actual = app.__doc__
        self.assertIsNotNone(actual)
        self.assertIsNotNone(app.route.__doc__)

    def test_pep8_app(self):
        """.. states.py conforms to PEP8 style"""
        pep8s = pep8.StyleGuide(quiet=True)
        errors = pep8s.check_files(['api/v1/views/states.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)


if __name__ == '__main__':
    unittest.main()
