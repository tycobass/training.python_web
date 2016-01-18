import socket
import sys
import os
import mimetypes


def response_ok(body=b"this is a pretty minimal response", mimetype=b"text/plain"):
    """returns a basic HTTP response"""
    resp = []
    ####import pdb; pdb.set_trace()    ###import debugger
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
    #return b"404 Not Found"   Why is this different - should I be modifying the test??????
    return b"HTTP/1.1 404 Not Found"


def parse_request(request):
    first_line = request.split("\r\n", 1)[0]
    method, uri, protocol = first_line.split()
    if method != "GET":
        raise NotImplementedError("We only accept GET")
    return uri


def resolve_uri(uri):
    """This method should return appropriate content and a mime type"""
    #####print('\n!!!!!!! resolve_uri =', uri, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    home_directory = 'webroot'
    relative_uri = home_directory + uri
    #####print('\n!!!!!!! relative_uri =', relative_uri, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    """ What am I?  Several tests to determine whether the URI points to:
    - a directory
    - a file
        - if a file is it:
            - text
            - executable
            - graphics
    """
    contents = "not yet filled"
    mimetype = "no mimetype assigned"

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

    testmime = mimetypes.guess_type(relative_uri)[0]
    print('\n!!!!!!! mimevalue', testmime, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # uri is a file, determine the mimetype and read the file
    #######
    text_types = ['.txt', '.html']
    for text_type in text_types:
        if text_type in relative_uri:
            #####print('\n!!!!!!! found a', text_type, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if text_type == '.txt': mimetype = b'text/plain'
            if text_type == '.html': mimetype = b'text/html'   #######  not bytes????????????????
            f = open(relative_uri, 'rb')
            contents = f.read()
            f.close()
            ####print('\n!!!!!!! con tents of file = ', contents, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # test to determine it the URI is a type of executable file
    #######
    executable_types = ['.py', '.pl']
    for executable_type in executable_types:
        if executable_type in relative_uri:
            ####print('\n!!!!!!! found a ', executable_type, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if executable_type == '.py': mimetype = b'text/x-python'
            if executable_type == '.pl': mimetype = b'text/x-script.perl'
            f = open(relative_uri, 'rb')
            contents = f.read()
            f.close()
            #####print('\n!!!!!!! contents of file = ', contents, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # test to determine it the URI is a type of image file
    #######
    image_types = ['.jpg', '.png']
    for image_type in image_types:
        ############print('\n!!!!!!! image type ', image_type, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if image_type in relative_uri:
            ####print('\n!!!!!!! found a ', image_type, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if image_type == '.jpg': mimetype = b'image/jpeg'
            if image_type == '.png': mimetype = b'image/png'
            #####print('\n!!!!!!! success found = ', image_type, mimetype, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            ## How do I retrieve image body????
            ###contents = 'filled' #just to keep from falling through to lost and found area - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            f = open(relative_uri, 'rb')
            contents = f.read()
            f.close()
            #####print('\n!!!!!!! contents of file = ', contents, file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # lost and found
    ####
    if contents == "not yet filled":
        contents = "just a bunch of fill"
        mimetype = b"image/rabbits"
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
