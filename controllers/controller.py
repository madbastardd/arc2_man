import configparser

from serialysers.jsonSerialyser import JsonSerialyser
from serialysers.pickleSerialyser import PickleSerialyser
from serialysers.yamlSerialyser import YamlSerialyser
from services.matchFactory import *
from services.matchesService import *
from controllers.database import DBConnection

class MatchesController(object):
    """
    Controller witch connect console view and matches services
    """

    def __init__(self):
        self.view = ConsoleView()
        self.factory = MatchFactory()
        self.service = MatchesService()

    def navigation(self):
        """
        Main function for navigation in program
        :return:
        """
        inp = ""
        matches = self.factory.getAllMatches()
        serialyser = self._getSerialiseMethod()
        while (True):
            self.view.showMenu()
            inp = self.view.inputFromConsole()
            if (inp == '1'):
                self.view.showMatches(self.service.getMatchByCountry(matches, "England"))
            elif (inp == '2'):
                self.view.showMatches(self.service.getMatchByCountry(matches, "Spain"))
            elif (inp == '3'):
                self.view.showMatches(self.service.getMatchByCountry(matches, "Ukraine"))
            elif (inp == '4'):
                self.view.printMessage("Enter team name:")
                teamName = self.view.inputFromConsole()
                matchesTeam = self.service.getMatchByTeam(matches, teamName)
                if (not matchesTeam):
                    self.view.printMessage("Unknown team name")
                else:
                    self.view.showMatches(matchesTeam)
            elif (inp == '5'):
                self.service.addMatch(matches)
            elif (inp == '6'):
                matches = DBConnection.clear_all()
            elif (inp == '7'):
                self.view.showMatches(matches)

            elif (inp == '8'):
                serialyser.saveMatches(matches)
                exit()
            else:
                self.view.printMessage("Please try again")

    def _getSerialiseMethod(self):
        """
        Choose serialisation method from config file
        :return:
        """
        parser = configparser.ConfigParser()
        parser.read("property.cfg")
        method = parser["serialize_method"]['method']
        if method == "pickle":
            return PickleSerialyser()
        elif method == "yaml":
            return YamlSerialyser()
        elif method == "json":
            return JsonSerialyser()
