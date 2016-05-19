import sys
from models.model import Match
from views.view import ConsoleView
from controllers.database import DBConnection
import MySQLdb as mdb

class MatchesService(object):
    """
    Class implements actions with matches
    """


    def getMatchByCountry(self, matches, countryName):
        """
        Find all matches in selected country
        :param matches:
        :param countryName:
        :return:
        """
        res = []
        for m in matches:
            if m.country == countryName:
                res.append(m)
        return res

    def getTeamID(self, team):
        query = """SELECT idteam
                        FROM teams
                        WHERE name = '{0}';
                    """.format(team)

        DBConnection.cur.execute(query)

        return DBConnection.cur.fetchone()[0]

    def getCountryID(self, country):
        query = """SELECT id
                    FROM countries
                    WHERE name = '{0}';
                """.format(country)

        DBConnection.cur.execute(query)

        return DBConnection.cur.fetchone()[0]

    def newCountry(self, country):
        query = """INSERT INTO countries(name)
                        VALUES('{0}')
            """.format(country)

        DBConnection.cur.execute(query)

        DBConnection.con.commit()

    def newTeam(self, team):
        query = """INSERT INTO teams(name)
                        VALUES('{0}')
            """.format(team)

        DBConnection.cur.execute(query)

        DBConnection.con.commit()

    def getMatchByTeam(self, matches, teamName):
        """
        Find all matches in selected team
        :param matches:
        :param teamName:
        :return:
        """
        res = []
        for m in matches:
            if m.team1 == teamName or m.team2 == teamName:
                res.append(m)
        return res

    def addMatch(self, matches):
        """
        Function add match to list of matches
        :param matches:
        :return:
        """
        view = ConsoleView()
        view.printMessage("Enter country: ")
        country = view.inputFromConsole()
        view.printMessage("Enter first team name: ")
        team1 = view.inputFromConsole()
        view.printMessage("Enter second team name: ")
        team2 = view.inputFromConsole()
        view.printMessage("Enter first team score: ")
        res1 = view.inputFromConsole()
        view.printMessage("Enter second team score: ")
        res2 = view.inputFromConsole()
        view.printMessage("Enter day: ")
        day = view.inputFromConsole()
        view.printMessage("Enter month: ")
        month = view.inputFromConsole()
        view.printMessage("Enter year: ")
        year = view.inputFromConsole()

        try:
            countryID = self.getCountryID(country)
        except:
            self.newCountry(country)
            countryID = self.getCountryID(country)

        try:
            team1ID = self.getTeamID(team1)
        except:
            self.newTeam(team1)
            team1ID = self.getTeamID(team1)

        try:
            team2ID = self.getTeamID(team2)
        except:
            self.newTeam(team2)
            team2ID = self.getTeamID(team2)

        query = """INSERT INTO games(country, first, second, firstres, secondres, playdate)
                  VALUES('{0}', '{1}', '{2}', {3}, {4}, '{5}-{6}-{7}')
        """.format(countryID, team1ID, team2ID, res1, res2, year, month, day)

        DBConnection.cur.execute(query)

        DBConnection.con.commit()

        matches.append(Match(country, team1, team2, res1, res2, [day, month, year]))


