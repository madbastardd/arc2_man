import MySQLdb as mdb
import psycopg2 as pdb
import sqlite3
import sys


class DBConnection:
    con = None
    cur = None

    @staticmethod
    def connectToDB(database):
        '''
        connect to database
        :param database: string
        :return: nothing
        '''
        if DBConnection.con is not None:
            return None

        try:
            if database == 'MySQL':
                DBConnection.con = mdb.connect('localhost', 'root', '', 'football')
                DBConnection.cur = DBConnection.con.cursor()

                DBConnection.cur.execute("""CREATE TABLE IF NOT EXISTS `countries` (
                                      `id` int(11) NOT NULL AUTO_INCREMENT,
                                      `name` varchar(45) NOT NULL,
                                      PRIMARY KEY (`id`)
                                    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;""")
                DBConnection.cur.execute("""CREATE TABLE IF NOT EXISTS `games` (
                                              `id` int(11) NOT NULL,
                                              `country` int(11) NOT NULL,
                                              `first` int(11) NOT NULL,
                                              `second` int(11) NOT NULL,
                                              `firstres` int(11) NOT NULL,
                                              `secondres` int(11) NOT NULL,
                                              `playdate` datetime NOT NULL,
                                              PRIMARY KEY (`id`)
                                            ) ENGINE=InnoDB DEFAULT CHARSET=latin1;""")
                DBConnection.cur.execute("""CREATE TABLE IF NOT EXISTS `teams` (
                                              `idteam` int(11) NOT NULL AUTO_INCREMENT,
                                              `name` varchar(45) NOT NULL,
                                              PRIMARY KEY (`idteam`)
                                            ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;""")
                DBConnection.con.commit()
                elif database == 'PSQL':
					DBConnection.con = pdb.connect("dbname='template1' user='postgres' host='localhost' password='1111'")
					DBConnection.cur = DBConnection.con.cursor()

					DBConnection.cur.execute("""CREATE TABLE IF NOT EXISTS countries (
											id SERIAL PRIMARY KEY,
											name varchar(45) NOT NULL
											);""")
					DBConnection.cur.execute("""CREATE TABLE IF NOT EXISTS games (
											id SERIAL PRIMARY KEY,
											country int NOT NULL,
											first int NOT NULL,
											second int NOT NULL,
											firstres int NOT NULL,
											secondres int NOT NULL,
											playdate date NOT NULL
											);""")
					DBConnection.cur.execute("""CREATE TABLE IF NOT EXISTS teams (
											idteam SERIAL PRIMARY KEY,
											name varchar(45) NOT NULL
											)""")
					DBConnection.con.commit()
        except mdb.Error as e:

            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

    @staticmethod
    def clear_all():
        '''
        clear tables
        :return: []
        '''
        DBConnection.cur.execute("""DELETE FROM games""")
        DBConnection.cur.execute("""DELETE FROM countries""")
        DBConnection.cur.execute("""DELETE FROM teams""")

        DBConnection.con.commit()

        return []

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        destructor
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: nothing
        '''
        if DBConnection.con is not None:
            DBConnection.con.close()