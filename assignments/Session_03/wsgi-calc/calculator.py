import re
import sys


def Instruction():
    page = """
<h1>"Python Calculator Project"</h1>

<p> <font face="Arial", font size="+2">
Addition<br></font>
<font face="Arial", font size="+1">
expected format:<br>
/addition/##/##/## where ## is a number - One to many numbers can be provided<br>
click the example ->   <a href="/addition/4/5">/addition/4/5</a><br><br></font>

<p> <font face="Arial", font size="+2">
Subtraction<br></font>
<font face="Arial", font size="+1">
expected format:<br>
/subtraction/##/##/## where ## is a number - One to many numbers can be provided<br>
Each number is subtracted from the prior number to produce the final value<br>
click the example ->   <a href="/subtraction/15/5">/subtraction/15/5</a><br><br></font>

<p> <font face="Arial", font size="+2">
Multiplication<br></font>
<font face="Arial", font size="+1">
expected format:<br>
/multiplication/##/##/## where ## is a number - One to many numbers can be provided<br>
click the example ->   <a href="/multiplication/3/8/2">/multiplication/3/8/2</a><br><br></font>

<p> <font face="Arial", font size="+2">
Division<br></font>
<font face="Arial", font size="+1">
expected format:<br>
/division/##/##/## where ## is a number - One to many numbers can be provided<br>
The numbers are divided in the order provided<br>
Any "divide by zero" events will prompt an exception<br>
click the example ->   <a href="/division/20/5/3">/division/20/5/3</a><br><br></font>
"""
    return page.format()


def addition(*args):
    page = """
<h1>Calculator - Addition</h1>
<p> <font face="Arial", font size="+1">
Operands provided: {0}<br><br>
Sum of operands: {1}<br><br><br><br><br>
</font></p>
<a href="/"><font face="Arial", font size="+1">
Return to Instruction Page
</font></a>
"""
    comma = ','
    operands = comma.join(args)  #puts the info returned into a string
    operands = operands.lstrip('/').split('/')  # strip off the first "/" and then split all the operands into a list
    operands = [v for v in operands if v]  #comprehension to delete any empty strings
    operands = list(map(int, operands))

    #sum of operands
    total = sum(operands)

    return page.format(operands, total)

def subtraction(*args):
    page = """
<h1>Calculator - Subtraction</h1>
<p> <font face="Arial", font size="+1">
Operands provided: {0}<br>
Operands are subtracted in the order provided<br><br>
Difference  of operands: {1}<br><br><br><br><br>
</font></p>
<a href="/"><font face="Arial", font size="+1">
Return to Instruction Page
</font></a>
"""
    comma = ','
    operands = comma.join(args)  #puts the info returned into a string
    operands = operands.lstrip('/').split('/')  # strip off the first "/" and then split all the operands into a list
    operands = [v for v in operands if v]  #comprehension to delete any empty strings
    operands = list(map(int, operands))

    #subtraction of values
    counter =0
    for operand in operands:
        if counter == 0:
            final_value = operand
        else:
            final_value = final_value - operand
        counter += 1
    try:
        final_value
    except NameError:
        final_value = 0
    return page.format(operands, final_value)

def multiplication(*args):
    page = """
<h1>Calculator - Multiplication</h1>
<p> <font face="Arial", font size="+1">
Operands provided: {0}<br><br>
Result of operand multiplication: {1}<br><br><br><br><br>
</font></p>
<a href="/"><font face="Arial", font size="+1">
Return to Instruction Page
</font></a>
"""
    comma = ','
    operands = comma.join(args)  #puts the info returned into a string
    operands = operands.lstrip('/').split('/')  # strip off the first "/" and then split all the operands into a list
    operands = [v for v in operands if v]  #comprehension to delete any empty strings
    operands = list(map(int, operands))

    #multiplication of values
    counter =0
    for operand in operands:
        if counter == 0:
            final_value = operand
        else:
            final_value = final_value * operand
        counter += 1
    try:
        final_value
    except NameError:
        final_value = 0

    return page.format(operands, final_value)

def division(*args):
    page = """
<h1>Calculator - Division</h1>
<p> <font face="Arial", font size="+1">
Operands provided: {0}<br>
Operands are divided in the order provided<br>
Attempts to divide by zero will trigger an error<br><br>
Result of operand division: {1}<br><br><br><br><br>
</font></p>
<a href="/"><font face="Arial", font size="+1">
Return to Instruction Page
</font></a>
"""
    comma = ','
    operands = comma.join(args)  #puts the info returned into a string
    operands = operands.lstrip('/').split('/')  # strip off the first "/" and then split all the operands into a list
    operands = [v for v in operands if v]  #comprehension to delete any empty strings
    operands = list(map(int, operands))

    #division of values
    counter =0
    for operand in operands:
        if counter == 0:
            final_value = operand
        else:
            final_value = final_value / operand
        counter += 1
    try:
        final_value
    except NameError:
        final_value = 0

    return page.format(operands, final_value)

def resolve_path(path):
    urls = [(r'^$', Instruction),
                (r'^addition([\-?/\d+]*)$', addition),
                (r'^subtraction([\-?/\d+]*)$', subtraction),
                (r'^multiplication([\-?/\d+]*)$', multiplication),
                (r'^division([\-?/\d+]*)$', division)
                ]
    matchpath = path.lstrip('/')
    for regexp, func in urls:
        match = re.match(regexp, matchpath)
        if match is None:
            continue
        args_string = match.groups([])
        return func, args_string
    # we get here if no url matches
    raise NameError


def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        func, args = resolve_path(path)
        body = func(*args)
        status = "200 OK"
    except ZeroDivisionError:
        status = "400 Bad Request"
        body = "<h1>Bad Request - Division by Zero</h1>"
    except NameError as e:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except Exception as e:  # as e give a more verbose stack trace and error explanation
        print(e)
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body.encode('utf8')]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)

    # Respond to requests until process is killed
    srv.serve_forever()

    # Alternative: serve one request, then exit
    #srv.handle_request()