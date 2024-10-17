from scapy.all import *
ether=Ether(dst="cc:00:f1:3e:b6:f5")#la box de chez moi
ip=IP(dst="1.1.1.1")
udp=UDP(sport=RandShort(),dport=53)
dns_requete=DNS(rd=1,qd=DNSQR(qname="ynov.com",qtype="A"))
packet = ether/ip/udp/dns_requete

answers, unanswered_packets = srp(packet, timeout=10)

print(f"UDP : {answers[0]}")
