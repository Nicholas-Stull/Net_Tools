# import os,logging,datetime,socket,ipaddress
import os
import logging
import datetime
import socket
import ipaddress

# Set up logging
# Create a directory to store the log files
LOG_DIR = 'NetTools.logs'
# Create a log file with the current date and time
LOG_FILE = datetime.datetime.now().strftime("NetTools_Log-%m_%d_%y_%H%M.log")
os.makedirs(LOG_DIR, exist_ok=True)  # Create the directory if it doesn't exist

logging.basicConfig(filename=os.path.join(LOG_DIR, LOG_FILE), level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M %p')  # Create the log file configuration
logging.info("NetTools Log - " +
             datetime.datetime.now().strftime("%m_%d_%y %H:%M"))  # Log the current date and time
# Get the IP address of the computer
ipa = socket.gethostbyname(socket.gethostname())
# Log the IP address of the computer
logging.info(f"The IP of this computer is: {ipa}")

# ------------------------------------------------------------------------------------------------------------------------  

__author__ = "Nicholas Stull"
__version__ = "1.0.1"
__email__ = "Nicholasp.stull@gmail.com"
__githubs__ = "http://www.github.com/Nicholas-Stull"
__status__ = "Development"

# ------------------------------------------------------------------------------------------------------------------------

def remove_dot(ip_address):
    return ip_address.replace(".", "")

#------------------------------------------------------------------------------------------------------------------------
def convert_to_binary(ip_address):
    binary = ""
    for octet in ip_address.split("."):
        binary += f"{int(octet):08b}"
        binary += " "
    return binary.strip(), 


#------------------------------------------------------------------------------------------------------------------------

def check_same_network(ipa1, ipa2, subnet):
    ipa1_binary = remove_dot(convert_to_binary(ipa1))
    ipa2_binary = remove_dot(convert_to_binary(ipa2))
    subnet_binary = remove_dot(convert_to_binary(subnet))

    same_network = True
    for i in range(len(subnet_binary)):
        if subnet_binary[i] == "1":
            if ipa1_binary[i] != ipa2_binary[i]:
                same_network = False
                break

    same_network_str = "The two IP addresses are in the same network" if same_network else "The two IP addresses are not in the same network"
    #logging ip address 1, ip address 2, subnet, subnet binary, and same network str
    logging.info(f"IP address 1: {ipa1}")
    logging.info(f"IP address 1 Binary: {convert_to_binary(ipa1)}")
    logging.info(f"IP address 2: {ipa1}")
    logging.info(f"IP address 2 Binary: {convert_to_binary(ipa1)}")
    logging.info(f"Subnet: {subnet}")
    logging.info(f"Subnet Binary: {convert_to_binary(subnet)}")
    logging.info(same_network_str)

    return same_network

#------------------------------------------------------------------------------------------------------------------------

def calc_net(ipa1,subnet):
    # Create an IPv4Network object with the given IP address and subnet mask
    network = ipaddress.IPv4Network((ipa1, subnet), strict=False)

    # Extract the desired information from the network object
    ip = str(network.network_address)
    netmask = str(network.netmask)
    network_address = str(network.network_address)
    broadcast_address = str(network.broadcast_address)
    first_ip = str(network[1])
    last_ip = str(network[-2])
    #logging ip address 1, netmask, network address, broadcast address, first ip, and last ip 
    logging.info(f"Inputed IP: {ipa1}")
    logging.info(f"Netmask: {netmask}")
    logging.info(f"Network Address: {network_address}")
    logging.info(f"broadcast_address: {broadcast_address}")
    logging.info(f"first IP: {first_ip}")
    logging.info(f"Last IP: {last_ip}")

    # Return the information as a dictionary
    return { 
        "ip": ip,
        "netmask": netmask,
        "network_address": network_address,
        "broadcast_address": broadcast_address,
        "first_ip": first_ip,
        "last_ip": last_ip
    }


#------------------------------------------------------------------------------------------------------------------------
# End of net_tools.py
__Quote_of_the_program__ = "People have an enormous tendency to resist change. They love to say, 'We've always done it this way.' I try to fight that."
__Who_Said_It__ = "Grace Hopper"
__Year__ = "1986"
__Source__ = "https://www.goodreads.com/quotes/1010-people-have-an-enormous-tendency-to-resist-change-they"
__More_Quotes__ = "https://www.goodreads.com/quotes/tag/change"
__More_Programming_Quotes__ = "https://www.defprogramming.com/random/"
# ------------------------------------------------------------------------------------------------------------------------