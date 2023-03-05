import os
from net_tools import check_same_network, convert_to_binary,ipa


#if __name__ == '__main__':
ipa1 = input("Enter IP address 1: ")
ipa2 = input("Enter IP address 2: ")
subnet = input("Enter subnet: ")
same_network = check_same_network(ipa1, ipa2, subnet)

print(f"The IP of this computer is: {ipa}")
print(f"IP address 1: {ipa1}")
print(f"IP address 1 Binary: {convert_to_binary(ipa1)}")
print(f"IP address 2: {ipa2}")
print(f"IP address 2 Binary: {convert_to_binary(ipa2)}")
print(f"Subnet: {subnet}")
print(f"Subnet Binary: {convert_to_binary(subnet)}")
print( f"The two IP addresses are on the same network: {same_network}")
