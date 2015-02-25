#!/usr/local/bin/python
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()


form = cgi.FieldStorage() #stores information submitted to the form #DM duplicate of line 5

#DM what happens if you try printing out the value of Pseudomonas_table?
import MySQLdb #import SQL database
sql="SELECT * FROM Strains WHERE Strain= %s" #query
db=MySQLdb.connect(db='mblank', user='mblank', passwd='PRXUyh03') #establish connection with SQL database
cursor=db.cursor() #define cursor
cursor.execute(sql,form['Pseudomonas_table'].value) #cursor queries using form value ('Pseudomonas_table' is the name of the form in html)
result=cursor.fetchall() #fetches results
result # takes the value in result but does nothing with it. Try printing it so it gets returned to the calling page.

#The code repeats from here on with the only difference that the 'isolates' condition changes.

#query for isolate 'burn wound'
exprsqlbw="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Strain=%s AND Isolate='burn wound' AND Expression_value>'13' ORDER BY Expression_value DESC LIMIT 30"
db=MySQLdb.connect(db='mblank', user='mblank', passwd='PRXUyh03')
cursor=db.cursor()
cursor.execute(exprsqlbw,form['Pseudomonas_table'].value)
bwresult=cursor.fetchall()
bwresult


#query for isolate 'murine tumor model'
mtmsql="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Strain=%s AND Isolate='murine tumor model' AND Expression_value>'13' ORDER BY Expression_value DESC LIMIT 30"
cursor.execute(mtmsql,form['Pseudomonas_table'].value)
mtmresult=cursor.fetchall()
mtmresult


#query for 'plant model'
pmsql="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Strain=%s AND Isolate='plant model' AND Expression_value>'13' ORDER BY Expression_value DESC LIMIT 30"
cursor.execute(pmsql,form['Pseudomonas_table'].value)
pmresult=cursor.fetchall()
pmresult


#query for 'in vitro biofilm (control)'
ivbcsql="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Strain=%s AND Isolate='in vitro biofilm (control)' AND Expression_value>'13' ORDER BY Expression_value DESC LIMIT 30"
cursor.execute(ivbcsql,form['Pseudomonas_table'].value)
ivbcresult=cursor.fetchall()
ivbcresult


#query for 'in vitro planktonic (control)'
ivpcsql="SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Strain=%s AND Isolate='in vitro planktonic (control)' AND Expression_value>'13' ORDER BY Expression_value DESC LIMIT 30"
cursor.execute(ivpcsql,form['Pseudomonas_table'].value)
ivpcresult=cursor.fetchall()
ivpcresult



print "Content-Type: text/html" # HTML is following
print # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

#Prints the respective submitted value in the form
for k in form.keys():
    print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k])

print "<table>"
print "<b>Gene ID, Gene Title, Strain, Isolate, Expression Value</b>"
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
print "<table>"

print "</body></html>"
