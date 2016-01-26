The program "calculator.py" sets up a little wsgi server and allows the user
to add, subtract, multiply, or divide numbers.

Once "calculator.py" is running in a bash shell the server can
be accessed from a browser at 127.0.0.1:8080.

In addition to simple error handling, the program does addition,
subtraction, multiplication, and division.
The user can provide one or more numbers into the calculator.  If no
number is provided the program will indicate an empty list with 
a result of 0.  If a 0 value is provided to the division operation
a Divide by Zero error will be displayed.
The program will show the list of operands provided and the value
of the operation.
Additionally there is a hyperlink to return to the introductory 
instruction page.

Independently there is a tests.py file that does a static test of the program.
