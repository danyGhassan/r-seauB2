# TP4 SECU : Exfiltration
## I. Getting started Scapy
### 🌞 ping.py
[ping.py](/tp4/ping.py)

```
danyg@danygThinkPad:~/projets/r-seauB2/tp4$ sudo python3 ping.py
Begin emission:
Finished sending 1 packets.
..*
Received 3 packets, got 1 answers, remaining 0 packets
Pong reçu : QueryAnswer(query=<Ether  dst=20:16:b9:2a:02:70 src=28:7f:cf:99:86:8a type=IPv4 |<IP  frag=0 proto=icmp src=10.33.79.176 dst=10.33.79.113 |<ICMP  type=echo-request |>>>, answer=<Ether  dst=28:7f:cf:99:86:8a src=20:16:b9:2a:02:70 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=28 id=25241 flags= frag=0 ttl=64 proto=icmp chksum=0x64e5 src=10.33.79.113 dst=10.33.79.176 |<ICMP  type=echo-reply code=0 chksum=0x0 id=0x0 seq=0x0 |>>>)
```

### 🌞 tcp_cap.py
[tcp_cap.py](/tp4/tcp_cap.py)

```
danyg@danygThinkPad:~/projets/r-seauB2/tp4$ sudo python3 tcp_cap.py 
TCP SYN ACK reçu !
- Adresse IP source : 104.18.29.67
- Adresse IP destination : 10.33.79.176
- Port source : 443
- Port destination : 41236
```

### 🌞 dns_cap.py

[dns_cap.py](/tp4/tcp_cap.py)

```
danyg@danygThinkPad:~/projets/r-seauB2/tp4$ sudo python3 dns_cap.py 
172.67.74.226
```
### 🌞 dns_lookup.py
[dns_lookup.py](/tp4/dns_lookup.py)

```
anyg@danygThinkPad:~/projets/r-seauB2/tp4$ sudo python3 dns_lookup.py 
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
UDP : QueryAnswer(query=<Ether  dst=cc:00:f1:3e:b6:f5 type=IPv4 |<IP  frag=0 proto=udp dst=1.1.1.1 |<UDP  sport=46089 dport=domain |<DNS  rd=1 qd=<DNSQR  qname='ynov.com.' qtype=A |> |>>>>, answer=<Ether  dst=28:7f:cf:99:86:8a src=cc:00:f1:3e:b6:f5 type=IPv4 |<IP  version=4 ihl=5 tos=0x60 len=102 id=48817 flags=DF frag=0 ttl=56 proto=udp chksum=0xbf29 src=1.1.1.1 dst=192.168.1.162 |<UDP  sport=domain dport=46089 len=82 chksum=0x29f4 |<DNS  id=0 qr=1 opcode=QUERY aa=0 tc=0 rd=1 ra=1 z=0 ad=0 cd=0 rcode=ok qdcount=1 ancount=3 nscount=0 arcount=0 qd=<DNSQR  qname='ynov.com.' qtype=A qclass=IN |> an=<DNSRR  rrname='ynov.com.' type=A rclass=IN ttl=300 rdlen=4 rdata=104.26.11.233 |<DNSRR  rrname='ynov.com.' type=A rclass=IN ttl=300 rdlen=4 rdata=172.67.74.226 |<DNSRR  rrname='ynov.com.' type=A rclass=IN ttl=300 rdlen=4 rdata=104.26.10.233 |>>> ns=None ar=None |>>>>)
```

## II. ARP Poisoning

### 🌞 arp_poisoning.py
[arp_poisoning.py](/tp4/arp_poisoning.py)
- ce code modifie seulement la MAC , je n'ai pas reussi a faire l'IP également

## II. Exfiltration ICMP

### 🌞 icmp_exf_send.py
[icmp_exf_send.py](/tp4/icmp_exf_send.py)
- on peut voir sur wireshark que nous avons exfiltrer le caractère

### 🌞 icmp_exf_receive.py
[icmp_exf_receive.py](/tp4/icmp_exf_receive.py)

```
danyg@danygThinkPad:~/projets/r-seauB2/tp4$ sudo python3 icmp_exf_receive.py 
k
```

## III. Exfiltration DNS

### 🌞 dns_exfiltration_send.py