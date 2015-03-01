#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

import MySQLdb

db=MySQLdb.connect(db='mblank', user='mblank', passwd='PRXUyh03')

def start_html():
    print("Content-type: text/html")
    print
    print("<html><head></head><body>")

def end_html():
    print("</body></html>")


#value='PBCLOp17'


######################## burn wound
#This block returns all burn-wound samples with a string-formatted query for the sample name. However, it returns 
#an empty set when accessed through html. Running the query through shell, it does return the expected result.
#it seems as if the form does not forward what is entered.
exprsqlbw='SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Isolate="burn wound" AND Strain= %s LIMIT 5'
cursor=db.cursor()
if form.has_key('PA'):
    value=form['PA'].value
cursor.execute(exprsqlbw,('PA'))
#else:
#    cursor.execute(exprsqlbw)
bwresult=cursor.fetchall()

#cursor.execute(sql,form['Pseudomonas_table'].value)

#start_html()
#print bwresult
#end_html()

######################## murine tumor model
exprsqlmtm="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Isolate='murine tumor model' LIMIT 1"
cursor=db.cursor()
if form.has_key('title'):
    value=form['title'].value
else:
    cursor.execute(exprsqlmtm)
mtmresult=cursor.fetchall()

#start_html()
#print mtmresult
#end_html()

######################## plant model
exprsqlpm="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Isolate='plant model' LIMIT 1"
cursor=db.cursor()
if form.has_key('title'):
    value=form['title'].value
else:
    cursor.execute(exprsqlpm)
pmresult=cursor.fetchall()

#start_html()
#print pmresult
#end_html()

######################## in vitro biofilm (control)
exprsqlivbc="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Isolate='in vitro biofilm (control)' LIMIT 1"
cursor=db.cursor()
if form.has_key('title'):
    value=form['title'].value
else:
    cursor.execute(exprsqlivbc)
ivbcresult=cursor.fetchall()

#start_html()
#print ivbcresult
#end_html()

######################## in vitro planktonic (control)
exprsqlivpc="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Isolate='in vitro planktonic (control)' LIMIT 1"
cursor=db.cursor()
if form.has_key('title'):
    value=form['title'].value
else:
    cursor.execute(exprsqlivpc)
ivpcresult=cursor.fetchall()

#start_html()
#print ivpcresult
#end_html()

start_html()
print "<h1>Gene ID, Gene Title, Strain, Isolate, Expression Value</h1>"
print "<h3>Top 30 expression values in isolate: burn wound</h3>"
print bwresult
print "<h3>Top 30 expression values in isolate: murine tumor model</h3>"
print mtmresult
print "<h3>Top 30 expression values in isolate: plant model</h3>"
print pmresult
print "<h3>Top 30 expression values in isolate: in vitro biofilm (control)</h3>"
print ivbcresult
print "<h3>Top 30 expression values in isolate: in vitro planktonic (control)</h3>"
print ivpcresult
end_html()