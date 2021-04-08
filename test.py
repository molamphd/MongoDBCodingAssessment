import unittest
from flatten import flatten_json

class TestFlatten(unittest.TestCase):

    def testEmptyInput(self):
        emptyInput = {}
        self.assertEqual(flatten_json(emptyInput), {})

    def testSingleInput(self):
        singleInput = {"a": 1}
        self.assertEqual(flatten_json(singleInput), {"a": 1})

    def testEmptyKey(self):
        emptyKey = {"a": None}
        self.assertEqual(flatten_json(emptyKey), {"a": None})

    def testNested(self):
        jsonObject = {"a": 1, "b": True, "c": {"d": 3, "e": "test"}}
        self.assertEqual(flatten_json(jsonObject), {'a': 1, 'b': True, 'c.d': 3, 'c.e': 'test'})

    def testDoublyNested(self):
        jsonObject = {"a": 1, "b": True, "c": { "d": { "w": 25, "e": "test"}}}
        self.assertEqual(flatten_json(jsonObject), {'a': 1, 'b': True, 'c.d.w': 25, 'c.d.e': 'test'})


