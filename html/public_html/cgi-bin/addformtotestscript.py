#!/usr/local/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

#if 'name' in form:
#        print"<tr><td>name</td><td>%s</td></tr>"% form['name'].value

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k])

sql="SELECT expression from expression e inner join gene ge on e.gene_id=g.gne_id where gene_id=%s" # make sql query that we want to run

db=mysql.connect(...)
cursor=db.cursor()
cursor.execute(sql,form[geneid].value)

#gene=Gene(form[geneid].value) if class is used
#gene.getExpression() if class is used #gives back list ( (experiment,expression),...)

#print "<table><tr><th>Sample</th><th>expression</th><tr>"
#for exp in results:
#    print "<tr><td>%s</td><td>%s</td></tr>"%exp

#print "</table>"

#brings back table with results depending on query.

print "</body></html>"