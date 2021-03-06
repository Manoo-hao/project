#!/usr/bin/python
import MySQLdb
#Incomplete outline script for a database interacting class to represent a gene.

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
        sql='SELECT Gene_Title, Gene_Symbol from Genes where Gene_ID=%s'
        cursor.execute(sql,(Gene_ID,)) #query database #get result and populate the class fields.
        result=cursor.fetchone()
        self.Gene_Title =result[0] #returns array for fetchone, for fetchall returns array of arrays, hence change to [0][0]
        self.Gene_Symbol=result[1] #returns array for fetchone, for fetchall returns array of arrays, hence change to [0][1]

        #now fetch the probes..
        probesql='SELECT Gene_ID from Probes where Gene_ID=%s'
        cursor.execute(probesql,(Gene_ID,))

        #fill in the blanks yourself
        for result in cursor.fetchall():
            self.probelist.append(result[0])

    def get_expression(self, Sample_ID):
        db=DBHandler()
        cursor=db.cursor()
        sql='SELECT Expression_value where ID_REF=%s AND Sample_ID=%s'

print("Done!")
            
'''Retrieve expression values for a given experiment for this gene'''
#TODO
