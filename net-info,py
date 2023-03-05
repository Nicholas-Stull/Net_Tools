import os
from net_tools import calc_net,ipa
import ipaddress

ipa1 = input("Enter IP address: ")
subnet = input("Enter the subnet mask: ")

result = calc_net(ipa1,subnet)
print(f"\nInputed IP: {ipa1}")
print("\nNetmask",result["netmask"])
print("\nNetwork Address:",result["network_address"])
print("\nBroadcast Address:",result["broadcast_address"])
print("\nFirst IP:",result["first_ip"])
print("\nLast IP:",result["last_ip"])
