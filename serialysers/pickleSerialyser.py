import pickle


class PickleSerialyser(object):

    def loadMatches(self, fileName='matches.pickle'):
        """
        Load objects from file
        :param fileName:
        :return:
        """
        with open(fileName, 'rb') as f:
            matches = pickle.load(f)
            return matches

    def saveMatches(self, matches, fileName='matches.pickle'):
        """
        Save objects to file
        :param matches:
        :param fileName:
        :return:
        """
        with open(fileName, 'wb') as f:
            pickle.dump(matches, f)
