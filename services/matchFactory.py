import sys
from models.model import Match
from controllers.database import DBConnection


class MatchFactory(object):
    """
    Class produce list of match from hardcoded list
    """

    def __init__(self):
        self.matches = []

        query = """SELECT countries.name,
                        teams1.name as first,
                        teams2.name as second,
                        games.firstres,
                        games.secondres,
                        games.playdate
                    FROM games, teams as teams1, teams as teams2, countries
                    WHERE games.country = countries.id AND
                        games.first = teams1.idteam AND
                        games.second = teams2.idteam;
                """

        DBConnection.cur.execute(query)

        rows = DBConnection.cur.fetchall()

        for row in rows:
            date = row[5]
            match = [row[0], row[1], row[2], row[3], row[4], [date.day, date.month, date.year]]
            self.matches.append(match)


    def getAllMatches(self):
        """
        Create classes from list
        :return:
        """
        res = []
        for m in self.matches:
            res.append(Match(m[0], m[1], m[2], m[3], m[4], m[5]))
        return res
    
