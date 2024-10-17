from scapy.all import *

def dns_sniffer(packet):
    if packet.haslayer(DNSRR):
        nomDeDomaine = packet[DNSQR].qname.decode('utf-8')
        if 'ynov.com' in nomDeDomaine:
            ip_address = packet[DNSRR].rdata
            print(ip_address)

sniff(filter="udp port 53", prn=dns_sniffer, store=0)