from controllers.controller import MatchesController
from controllers.database import DBConnection
import configparser

parser = configparser.ConfigParser()
parser.read("property.cfg")
DBConnection.connectToDB(parser['database']['name'])
controller = MatchesController()
controller.navigation()
