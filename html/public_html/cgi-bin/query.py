#!/usr/local/bin/python
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

'''change all comments'''

form = cgi.FieldStorage()#stores information submitted to the form
import MySQLdb #import SQL database
sql="SELECT Sample_ID, Strain FROM Strains WHERE Strain= %s" #query
db=MySQLdb.connect(db='mblank', user='mblank', passwd='PRXUyh03') #establish connection with SQL database
cursor=db.cursor() #define cursor
cursor.execute(sql,form[''].value) #cursor queries using form value ('' is the name of the form)
result=cursor.fetchall() #fetches results
result

#second query for PBCLOp10
exprsqlPBCLOp10="SELECT  FROM  WHERE Gene_ID= %s"
db=MySQLdb.connect(db='mblank', user='mblank', passwd='PRXUyh03')
cursor=db.cursor()
cursor.execute(exprsqlPBCLOp10,form[''].value)
exprresult=cursor.fetchall()
exprresult
PBCLOp10sql="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Strain='PBCLOp10' AND Expression_value>'13' ORDER BY Expression_value DESC LIMIT 30"
cursor.execute(PBCLOp10sql,form[''].value)
PBCLOp10result=cursor.fetchall()
PBCLOp10result

#second query for PBCLOp11
exprsqlPBCLOp11="SELECT  FROM  WHERE Gene_ID= %s"
db=MySQLdb.connect(db='mblank', user='mblank', passwd='PRXUyh03')
cursor=db.cursor()
cursor.execute(exprsqlPBCLOp11,form[''].value)
exprresult=cursor.fetchall()
exprresult
PBCLOp11sql="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Strain='PBCLOp11' AND Expression_value>'13' ORDER BY Expression_value DESC LIMIT 30"
cursor.execute(PBCLOp11sql,form[''].value)
PBCLOp11result=cursor.fetchall()
PBCLOp11result

#second query for PBCLOp17
exprsqlPBCLOp17="SELECT  FROM  WHERE Gene_ID= %s"
db=MySQLdb.connect(db='mblank', user='mblank', passwd='PRXUyh03')
cursor=db.cursor()
cursor.execute(exprsqlPBCLOp17,form[''].value)
exprresult=cursor.fetchall()
exprresult
PBCLOp17sql="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Strain='PBCLOp17' AND Expression_value>'13' ORDER BY Expression_value DESC LIMIT 30"
cursor.execute(PBCLOp17sql,form[''].value)
PBCLOp17result=cursor.fetchall()
PBCLOp17result

print "Content-Type: text/html" # HTML is following
print # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

for k in form.keys():
    print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k])

print "<table>"
print "<b>Gene ID, Gene Title, Strain, Isolate, Expression Value</b>"
print "<p><b>Top 30 expression values in PBCLOp10</b></p>"
print PBCLOp10result
print "<p><b>Top 30 expression values in PBCLOp11</b></p>"
print PBCLOp11result
print "<p><b>Top 30 expression values in PBCLOp17</b></p>"
print PBCLOp17result
#all results printed on the page
print "</body></html>"
print "<table>"

print "</body></html>"