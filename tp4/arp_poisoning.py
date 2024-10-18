from scapy.all import *


send(ARP(op="who-has",pdst="10.1.1.4",hwsrc="de:ad:be:ef:ca:fe"))
