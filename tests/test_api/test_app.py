#!/usr/bin/python3
""" Unit Test for api v1 Flask App"""

import unittest
import pep8
import doctest
from api.v1.app import app


class TestAppDocs(unittest.TestCase):
    """Class for testing Flask App Docs"""


    def test_doc_file(self):
        """...documentation for the file"""
        actual = app.__doc__
        self.assertIsNotNone(actual)

    def test_all_function_docs(self):
        """... tests for ALL DOCS for all functions in app file"""
        self.assertIsNotNone(app.__doc__)
        self.assertIsNotNone(app.teardown_appcontext.__doc__)
        self.assertIsNotNone(app.errorhandler.__doc__)

    def test_pep8_app(self):
        """... app.py conforms to PIP8 style"""
        pep8style = pep8.StyleGuide(quite=True)
        errors = pep8style.check_files(['api/v1/app.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)


class TestFlaskApp(unittest.TestCase):
    """Class for testing the App methods"""

    @classmethod
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_404_error_handler(self):
        response = self.app.get('/nonexistent-route')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"error": "Not found"})


if __name__ == "__main__":
    unittest.main()
