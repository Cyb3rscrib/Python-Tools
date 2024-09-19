### ARP Poisoning Script - README

---

## Overview
This Python script performs **ARP poisoning** using the `Scapy` library to intercept and manipulate traffic between a **target** device and a **gateway** (typically a router) on a local network. This technique is commonly used in **Man-in-the-Middle (MITM)** attacks, where the attacker spoofs the ARP responses, causing the target and gateway to associate the attacker's MAC address with their respective IPs.

**WARNING**: This script should only be used for educational purposes in a controlled environment. **Do not use** this script on networks without explicit permission, as it is illegal and unethical to perform ARP poisoning attacks on unauthorized systems.

---

## Features
- Intercepts network traffic between a target device and a gateway by sending malicious ARP packets.
- Continuously poisons the ARP cache of both the target and the gateway to maintain the attack.
- Resolves MAC addresses of the target and the gateway automatically.

---

## Prerequisites

1. **Python 3.x**: Ensure Python 3 is installed.
2. **Scapy**: The script requires the `Scapy` library for packet manipulation.
   - You can install it using `pip`:
     ```bash
     pip install scapy
     ```
3. **Administrator/Root Access**: The script needs to be run with elevated privileges, as it directly interacts with network interfaces.

---

## Usage

1. Clone or download the script.
   
2. Update the following variables in the script to match your target and gateway:
   ```python
   target_ip = "192.168.0.100"  # Replace with the target device's IP address
   gateway_ip = "192.168.0.1"   # Replace with the gateway's IP address
   ```

3. Ensure you have the necessary permissions to run the script on the local network.

4. **Run the script with elevated privileges**:
   - On Linux/macOS, use `sudo`:
     ```bash
     sudo python3 arp_poison.py
     ```
   - On Windows, open a terminal as an administrator and run:
     ```bash
     python arp_poison.py
     ```

---

## Code Structure

### 1. ARP Poisoning Function:
```python
def arp_poison(target_ip, target_mac, gateway_ip, gateway_mac):
```
- This function sends ARP reply packets to both the target and the gateway to poison their ARP caches. It continuously sends spoofed ARP packets every second to maintain the attack.

### 2. Get MAC Address Function:
```python
def get_mac(ip):
```
- This function sends an ARP request to resolve the MAC address of a given IP address on the local network.

### 3. Main Function:
```python
def main():
```
- The main function initializes the target and gateway IP addresses, retrieves their MAC addresses, and starts the ARP poisoning attack.

---

## Important Notes

- **Legal & Ethical Considerations**: ARP poisoning is an attack technique and should only be used in controlled environments such as labs where you have explicit permission to perform such actions. Unauthorized use on real networks is illegal and unethical.

- **Network Impact**: This script will disrupt network traffic between the target and gateway. It may cause loss of internet connectivity, slowdowns, or crashes depending on the network configuration. 

- **Testing**: Ensure you're in an isolated environment like a virtual lab or a test network before running this script.

---

## Disclaimer

This tool is provided for educational purposes only. The use of this tool to compromise systems without permission is illegal. The developer is not responsible for any misuse or damage caused by this script.

---

## License

This project is licensed under the MIT License.

--- 

Feel free to modify the script for testing, but always use it responsibly.
