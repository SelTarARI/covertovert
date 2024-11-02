import scapy

# Implement your ICMP sender here
from scapy.all import *

def send_icmp():
    # Send ICMP packet to
    packet = IP(dst="172.18.0.3", ttl=1) / ICMP()
    send(packet)
    print("ICMP packet sent")

if __name__ == "__main__":
    send_icmp()