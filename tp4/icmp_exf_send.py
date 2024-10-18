from scapy.all import *
from sys import argv

send( fragment(IP(dst=argv[1])/ICMP()/(argv[2])) )