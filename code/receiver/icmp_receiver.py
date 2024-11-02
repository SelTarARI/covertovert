import scapy

# Implement your ICMP receiver here
def receive_icmp(packet):
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:  # Type 8 is ICMP echo request
        print("Received ICMP request:")
        packet.show()

if __name__ == "__main__":
    # Sniff for ICMP packets
    sniff(filter="icmp", prn=receive_icmp, count=1)