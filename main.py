import os
from net_tools import check_same_network, convert_to_binary,ipa

#if __name__ == '__main__':
ip1 = input("Enter IP address 1: ")
ip2 = input("Enter IP address 2: ")
subnet = input("Enter subnet: ")
same_network = check_same_network(ip1, ip2, subnet)

print(f"The IP of this computer is: {ipa}")
print(f"IP address 1: {ip1}")
print(f"IP address 1 Binary: {convert_to_binary(ip1)}")
print(f"IP address 2: {ip2}")
print(f"IP address 2 Binary: {convert_to_binary(ip2)}")
print(f"Subnet: {subnet}")
print(f"Subnet Binary: {convert_to_binary(subnet)}")
print( f"The two IP addresses are on the same network: {same_network}")
