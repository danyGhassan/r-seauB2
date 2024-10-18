from scapy.all import *
import sys


def icmp_recieve(packet):
    if packet.haslayer(ICMP) : 
        data= bytes(packet[ICMP]).decode(errors='ignore')
        if len(data) < 20:
            print(data)
            sys.exit(0)
sniff(filter="icmp", prn=icmp_recieve, store=0) 
