#!/usr/bin/python
import cgi #import modules
import cgitb
cgitb.enable() #enable bugfixing module
form = cgi.FieldStorage()

import MySQLdb

db=MySQLdb.connect(db='mblank', user='mblank', passwd='PRXUyh03')

def start_html():
'''default html start'''
    print("Content-type: text/html")
    print
    print("<html><head></head><body>")

def end_html():
'''default html end'''
    print("</body></html>")


#value='PBCLOp17'


######################## burn wound
#This block returns all burn-wound samples with a string-formatted query for the sample name. However, it returns 
#an empty set when accessed through html. Running the query through shell, it does return the expected result.
#it seems as if the form does not forward what is entered.
#When changing the query to something that takes the Gene_ID as opposed to a strain the form did work in a restricted way
#entering the URL http://ts-ug-dev.lifesci.dundee.ac.uk/~homes/mblank/public_html/cgi-bin/queryscript.py?(enter Gene_ID here) did return the expected result.
exprsqlbw='SELECT DISTINCT Genes.Gene_ID, Gene_Title, Strain, Isolate, Expression_value FROM Expression INNER JOIN Isolates ON Expression.Sample_ID=Isolates.Sample_ID INNER JOIN Strains ON Isolates.Sample_ID=Expression.Sample_ID INNER JOIN Probes ON Probes.ID_REF=Expression.ID_REF INNER JOIN Genes ON Genes.Gene_ID=Probes.Gene_ID WHERE Isolate="burn wound" AND Strain= %s LIMIT 5'
cursor=db.cursor() #initiate cursor and store it in variable cursor
if form.has_key('PA'): #refer to form with key PA. See form in index.html in public_html folder
    value=form['PA'].value #store what was entered in the form in the variable value
cursor.execute(exprsqlbw,('PA')) #execute cursor to interrogate database with query under exprsqlbw and value entered in form
#else:
#    cursor.execute(exprsqlbw)
bwresult=cursor.fetchall() #fetch all returned results in variable bw result. Will be printed at the end of the script

#cursor.execute(sql,form['Pseudomonas_table'].value)

#start_html()
#print bwresult
#end_html()

#The rest of the script is an interation of the first block, hence the comments made above are also valid for the blocks below.


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

start_html() #call function defined above to start html.
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
end_html()#call function defined above to start html.
