#!/usr/bin/python
import MySQLdb
#Incomplete outline script for a database interacting class to represent a gene.

#A non-functional working version of models.py in order to test its functionality
#This file is the intermediate between an HTML form an an SQL query. If it was functional, I would be incorporated
#in the python CGI script. Since this script is currently not functional, the queries were hardcoded into the CGI script

class DBHandler():
    '''The static database connection - avoids overuse of resources'''
    connection=None
    dbname='mblank'
    dbuser='mblank'
    dbpassword='PRXUyh03'

    def __init__(self):
        '''initialising database'''
        if DBHandler.connection == None:
            DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)
            #Testing if database is connected and establish connection in case it wasn't.

    def cursor(self):
        return DBHandler.connection.cursor()

class Genes():
    '''A class that describes an individual gene'''
    Gene_Symbol=''
    Gene_Title=''
    Gene_ID=''
    probelist=[] #Each Gene can have several probes

    def __init__(self,Gene_ID):
        '''Init method for Gene'''
        db=DBHandler()
        self.Gene_ID=Gene_ID
        cursor=db.cursor()
        sql='SELECT Gene_ID, Gene_Title, Gene_Symbol FROM Genes WHERE Gene_ID=%s'
        cursor.execute(sql,(Gene_ID,)) #query database #get result and populate the class fields.
        result=cursor.fetchone()
        self.Gene_Title =result[0]
        self.Gene_Symbol=result[1]
        return result

print("Done!")
