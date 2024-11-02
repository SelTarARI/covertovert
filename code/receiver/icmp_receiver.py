import scapy

# Implement your ICMP receiver here
from scapy.all import *

def receive_icmp(packet):
    # Check if the packet is an ICMP echo request
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:  # Type 8 is ICMP echo request
        print("Received ICMP request:")
        # Print the source IP address
        packet.show()

if __name__ == "__main__":
    # Sniff for ICMP packets
    sniff(filter="icmp", prn=receive_icmp, count=1)