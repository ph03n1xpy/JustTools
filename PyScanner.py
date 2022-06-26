#!/usr/bin/env python

import scapy.all as scapy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-ip", dest ="ip", help="Target IP")
args = parser.parse_args()
ip = args.ip

print("\n [!] TOOL IS UNDERDEVELOPMENT. RESULTS MAY NOT BE ACCURATE!")

print("\nScanning.... :)\n")

if not ip:
    error = input("IP range is not provided, do you want the tool to automatically grep and use the IP range? [Y/n] ")
    if error == "Y" or error == "y":
        interface = input("Enter Interface name - ")
        print("Automatic IP range feature is underdevelopment, please enter the IP range mannually using -ip option, for example: -ip 192.168.1.1/24.")
    else:
        parser.error("IP range is required, for eg. 192.168.1.1/24 . Use --help for more info")
        exit()

broadcast_mac = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
target_ip = scapy.ARP(pdst=ip)
final_packet = broadcast_mac/target_ip
ans = scapy.srp(final_packet, timeout=5, verbose=False)[0]

num = 0

print("─"*50)
print("   S.No.\tIP\t      MAC Address")
for elements in ans:
    num = num + 1
    print("─"*50)
    print(f"    {num}      {elements[1].psrc}\t   {elements[1].hwsrc}")

print("─"*50)
