import os
import logging
import datetime
import socket

LOG_DIR = 'NetTools.logs'
LOG_FILE = datetime.datetime.now().strftime("NetTools_Log-%m_%d_%y_%H%M.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(filename=os.path.join(LOG_DIR, LOG_FILE), level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M %p')
logging.info("NetTools Log - " +
             datetime.datetime.now().strftime("%m_%d_%y %H:%M"))
hostname = socket.gethostname()
ipa = socket.gethostbyname(socket.gethostname())

def remove_dot(ip_address):
    return ip_address.replace(".", "")


def convert_to_binary(ip_address):
    binary = ""
    for octet in ip_address.split("."):
        binary += f"{int(octet):08b}"
        binary += " "
    return binary.strip()


def check_same_network(ip1, ip2, subnet):
    ip1_binary = remove_dot(convert_to_binary(ip1))
    ip2_binary = remove_dot(convert_to_binary(ip2))
    subnet_binary = remove_dot(convert_to_binary(subnet))

    same_network = True
    for i in range(len(subnet_binary)):
        if subnet_binary[i] == "1":
            if ip1_binary[i] != ip2_binary[i]:
                same_network = False
                break

    same_network_str = "The two IP addresses are in the same network" if same_network else "The two IP addresses are not in the same network"
    logging.info(f"The IP of this computer is: {ipa}")
    logging.info(f"IP address 1: {ip1}")
    logging.info(f"IP address 1 Binary: {convert_to_binary(ip1)}")
    logging.info(f"IP address 2: {ip2}")
    logging.info(f"IP address 2 Binary: {convert_to_binary(ip2)}")
    logging.info(f"Subnet: {subnet}")
    logging.info(f"Subnet Binary: {convert_to_binary(subnet)}")
    logging.info(same_network_str)

    return same_network
