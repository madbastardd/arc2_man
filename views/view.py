class ConsoleView(object):
    """
    Class shows info on console
    """


    def showMatches(self, matches):
        """
        Show list of match
        :param matches:
        :return:
        """
        if matches is None:
            return;
        for match in matches:
            print(
                "%s vs %s - %s:%s on %s/%s/%s in %s" %
                (match.team1, match.team2, match.res1, match.res2,
                 match.date[0], match.date[1], match.date[2], match.country))

    def showMenu(self):
        """
        Show menu cases
        """
        print("""
        1. England
        2. Spain
        3. Ukraine
        4. Select team
        5. Add match
        6. Clear matches
        7. Show all matches
        8. Exit
        """)

    def inputFromConsole(self):
        """
        Input from console
        :return:
        """
        return input()

    def printMessage(self, mes):
        print(mes)

