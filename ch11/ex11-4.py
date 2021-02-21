# 11.4 CIDR 주소로 IP 주소 생성

import ipaddress
net = ipaddress.ip_network('123.45.67.64/27')
net
# IPv4Network('123.45.67.64/27')
for a in net:
    print(a)

# 123.45.67.64
# 123.45.67.65
# 123.45.67.66
# 123.45.67.67
# 123.45.67.68
# ...
# 123.45.67.95

net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
net6
# IPv6Network('12:3456:78:90ab:cd:ef01:23:30/125')
for a in net6:
    print(a)

# 12:3456:78:90ab:cd:ef01:23:30
# 12:3456:78:90ab:cd:ef01:23:31
# 12:3456:78:90ab:cd:ef01:23:32
# 12:3456:78:90ab:cd:ef01:23:33
# 12:3456:78:90ab:cd:ef01:23:34
# 12:3456:78:90ab:cd:ef01:23:35
# 12:3456:78:90ab:cd:ef01:23:36
# 12:3456:78:90ab:cd:ef01:23:37


net.num_addresses
# 32
net[0]
# IPv4Address('123.45.67.64')
net[1]
# IPv4Address('123.45.67.65')
net[-1]
# IPv4Address('123.45.67.95')
net[-2]
# IPv4Address('123.45.67.94')


a = ipaddress.ip_address('123.45.67.69')
a in net
# True
b = ipaddress.ip_address('123.45.67.123')
b in net
# False


inet = ipaddress.ip_interface('123.45.67.73/27')
inet.network
# IPv4Network('123.45.67.64/27')
inet.ip
# IPv4Address('123.45.67.73')



# 토론

a = ipaddress.ip_address('127.0.0.1')
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect((a, 8080))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: str, bytes or bytearray expected, not IPv4Address
s.connect((str(a), 8080))
