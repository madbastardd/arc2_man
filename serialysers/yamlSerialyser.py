from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class YamlSerialyser(object):

    def loadMatches(self, fileName='matches.yaml'):
        """
        Load objects from file
        :param fileName:
        :return:
        """
        with open(fileName, 'rt') as f:
            matches = load(f, Loader=Loader)
            return matches

    def saveMatches(self, matches,  fileName='matches.yaml'):
        """
        Save objects to file
        :param matches:
        :param fileName:
        :return:
        """
        with open(fileName, 'wt') as f:
            dump(matches, f, Dumper=Dumper)