# 4.16 무한 while 순환문을 이터레이터로 치환

CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


def reader(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(data)


import sys
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)

# nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
# root:0:0:System Administrator:/var/root:/bin:sh
# daemon:*:1:1:System Services:/var/root:/usr/bin/false
# _uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
# ...
