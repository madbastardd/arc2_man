import unittest

from controllers.controller import MatchesController
from serialysers.jsonSerialyser import JsonSerialyser
from services.matchFactory import MatchFactory
from tests.string_support import *


class TestStringMethods(unittest.TestCase):

    def test_json(self):
        serialyser = JsonSerialyser()
        service = MatchFactory()
        m = service.getAllMatches()
        serialyser.saveMatches(m)

    def test_config(self):
        controller = MatchesController()
        obj = controller._getSerialiseMethod()
        res = isinstance(obj, JsonSerialyser)
        self.assertEqual(res, True, "OK")

    # def test_json_serialise(self):
    #     factory = MatchFactory()
    #     matches = factory.getAllMatches()
    #     JsonSerialyser().saveMatches(matches)
    #     out = getStringFromSerialyser(JsonSerialyser(), matches)
    #     with open('matches.json', 'rt') as f:
    #         for line in f:
    #             self.assertEqual(out.readLine(), line)





if __name__ == '__main__':
    unittest.main()