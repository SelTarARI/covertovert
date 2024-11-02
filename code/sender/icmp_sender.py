import scapy

# Implement your ICMP sender here
def send_icmp():
    # Replace 'receiver_container_ip' with the actual IP address of the receiver container
    packet = IP(dst="receiver_container_ip", ttl=1) / ICMP()
    # Send the packet
    send(packet)
    print("ICMP packet sent")

if __name__ == "__main__":
    send_icmp()