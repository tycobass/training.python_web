import socket
import sys
import os
import mimetypes


def response_ok(body=b"this is a pretty minimal response", mimetype=b"text/plain"):
    """returns a basic HTTP response"""
    resp = []
    resp.append(b"HTTP/1.1 200 OK")
    resp.append(b"Content-Type: " + mimetype)
    resp.append(b"")
    resp.append(body)
    return b"\r\n".join(resp)


def response_method_not_allowed():
    """returns a 405 Method Not Allowed response"""
    resp = []
    resp.append("HTTP/1.1 405 Method Not Allowed")
    resp.append("")
    return "\r\n".join(resp).encode('utf8')


def response_not_found():
    """returns a 404 Not Found response"""
    return b"HTTP/1.1 404 Not Found"


def parse_request(request):
    first_line = request.split("\r\n", 1)[0]
    method, uri, protocol = first_line.split()
    if method != "GET":
        raise NotImplementedError("We only accept GET")
    return uri


def resolve_uri(uri):
    """This method should return appropriate content and a mime type"""
    home_directory = 'webroot'
    relative_uri = home_directory + uri

    """ What am I?  Several tests to determine whether the URI points to:
    """
    contents = "not yet filled"

    # test to determine it the URI is a directory
    #######
    try:
        contents = os.listdir(relative_uri)
        comma = ','
        contents = comma.join(contents)
        contents = contents.encode('utf-8')
        mimetype = b'text/plain'
    except:
        pass

    # uri is a file, determine the mimetype and read the file
    #######
    if contents == "not yet filled":
        mimetype = mimetypes.guess_type(relative_uri)[0]
        mimetype = mimetype.encode()
#############################################################################
#Note to Cris - the mimetypes function returns a text/plain mimetype for a .py file rather than the
# text/x-python that the test was expecting
##################################
        f = open(relative_uri, 'rb')
        contents = f.read()
        f.close()

    return contents, mimetype

def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    sock.bind(address)
    sock.listen(1)

    try:
        while True:
            print('waiting for a connection', file=log_buffer)
            conn, addr = sock.accept()  # blocking
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)
                request = ''
                while True:
                    data = conn.recv(1024)
                    request += data.decode('utf8')
                    if len(data) < 1024:
                        break

                try:
                    uri = parse_request(request)
                except NotImplementedError:
                    response = response_method_not_allowed()
                else:
                    try:
                        content, mime_type = resolve_uri(uri)
                    except NameError:
                        response = response_not_found()
##########################################################################################
#Note to Cris - the search for the missing file triggered a FileNotFoundError rather than a NameError exception
# so I added the additional exception handling
######################################
                    except FileNotFoundError:
                        response = response_not_found()
                    else:
                        response = response_ok(content, mime_type)
                print('sending response', file=log_buffer)
                conn.sendall(response)
            finally:
                conn.close()

    except KeyboardInterrupt:
        sock.close()
        return


if __name__ == '__main__':
    server()
    sys.exit(0)
