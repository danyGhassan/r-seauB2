from scapy.all import *
from sys import argv

send(IP(dst=argv[1])/UDP()/DNS(rd=1, qd=DNSQR(qname=f"{argv[2]}.akha.com")))
