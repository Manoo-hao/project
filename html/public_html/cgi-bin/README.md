#CGI scripts

All files in here are python scripts, using CGI modules. These scripts take the input of a html-form and transform them
into a query that is able to interrogate an SQL database and to return the information.
All scripts here are a work in progress with queryscript4 being the most functional one.
The queries were adapted to what was orginally planned in order to get a more easily accessible result when running the
script.

It was planned to return the 30 most highly expressed genes depending on the strain entered in the form. This number was
altered to 5 and 1 respectively.

In the first block string formatting was used for more flexible handling of the form. A form that returns a static result
is not of much use to an end-user, especially when interrogating a database which contains a wealth of information. In
all the blocks but the first the string formatting symbol was omitted in order to show the user that the database is in
fact consulted when running a query, even though the result returned is always the same.

As mentioned in the report, ideally the amount of top/bottom hits that are returned should also be specifiable by the
user. However, since already one string formatting symbol caused trouble, I was hesitant to attempt incorporating a
second one. The syntax for multiple string formatting symbols would not be notably different, but the correct order of
input would become important. This was planned to be solved with dropdown menus akin to the restriction enzyme selection
in reexercise.html.
