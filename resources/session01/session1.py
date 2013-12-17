import socket


def get_constants(prefix):
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix))


def get_address_info(host, port):
    families = get_constants('AF_')
    types = get_constants('SOCK_')
    protocols = get_constants('IPPROTO_')
    for response in socket.getaddrinfo(host, port):
        fam, typ, pro, nam, add = response
        print 'family: ', families[fam]
        print 'type: ', types[typ]
        print 'protocol: ', protocols[pro]
        print 'canonical name: ', nam
        print 'socket address: ', add
        print


def print_address_constants():
    addrs = get_constants('INADDR')
    for val, name in addrs.items():
      hexval = hex(val)
      packed = socket.inet_aton(hexval)
      addr = socket.inet_ntoa(packed)
      tmpl = '{0: >24}: {1: <10} {2: <16}'
      print tmpl.format(name, hexval, addr)