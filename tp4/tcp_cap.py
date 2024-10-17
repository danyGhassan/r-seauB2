from scapy.all import sniff

def print_it_please(packet):
        packet_source_ip = packet['IP'].src
        packet_dest_ip = packet['IP'].dst
        port_src = packet['TCP'].sport  
        port_dst = packet['TCP'].dport 
        print("TCP SYN ACK reçu !")
        print(f"- Adresse IP source : {packet_source_ip}")
        print(f"- Adresse IP destination : {packet_dest_ip}")
        print(f"- Port source : {port_src}")
        print(f"- Port destination : {port_dst}")

sniff(filter="tcp or udp", prn=print_it_please, count=1)
