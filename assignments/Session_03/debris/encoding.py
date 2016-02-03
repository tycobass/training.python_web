hello = 'Hello, world!'
rabbits = hello.encode('utf-8')
print ('Encoded version of "Hello, world - ', rabbits, '(byte string)\n')

turtles = rabbits.decode('utf-8')
print ('Decoded version of "Hello, world - ', turtles, '(unicode)\n')