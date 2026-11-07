#importting needed modules
import subprocess as sp
from re import Pattern
from re import compile as re_comp

#this is a regex match for any IPv4 address and subnet formatted string
# this is not validation or verification, just location.
ip_addr_sub_re: Pattern = re_comp("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}/\\d{1,2}")
ip_addr_re:     Pattern = re_comp("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}")

def local_address():
    '''
    This function returns valid ip addresses returned from the "ip a" command
    
    This excludes 127.0.0.1 (local host), and 169.254.0.0/16 range
    '''
    # this is getting the raw output of the "ip a" command
    my_addr: sp.CompletedProcess = sp.run(["ip", "a"], capture_output = True, check=True)
    my_addr: str  = my_addr.stdout.decode()
    my_addr: list = my_addr.split("\n")

    # this is cathering all IPv4 addresses returned
    located_addrs: list = []

    for line in my_addr:
        located_addrs.extend(ip_addr_sub_re.findall(line))

    # this now narrows down the address ranges by removing
    #   home: 127.0.0.1
    #   fallback: 169.254.1.0-169.254.254.255

    good_addr: list = []

    for addr in located_addrs:
        if "127.0." in addr or "169.254." in addr:
            continue
        else:
            good_addr.append(addr)

    return good_addr


def local_network():
    '''
    Uses nmap to scan the local network looking for any hosts
    '''

    host_addrs = local_address()
    # now scaning the network for other ip's with a certain hostname
    nmap_base: list[str] = ["nmap", "-sn", "-R"]
    network_addrs: list[str] = []

    # scan each network that the pi is attached to
    for addr in host_addrs:
        # replace the last number in the address with 0
        # i.e. 192.168.8.106 -> 192.168.8.0
        new_addr: list[str]|str = addr.split(".")
        subnet:str = new_addr[-1].split("/")[1]
        new_addr[-1] = '0'
        new_addr = ".".join(new_addr)+"/"+subnet

        # new_addr is now correctly formatted for a nmap scan
        # i.e. 192.168.8.0/24

        # perform the scan and pullout the hostnames and the addresses
        new_nmap = nmap_base.copy()
        new_nmap.append(new_addr)
        network_addrs_raw: sp.CompletedProcess = sp.run(new_nmap, capture_output = True, check = True)
    
        # extracting the returned data and splitting it into a list of lines
        network_addrs_raw: list[str] = network_addrs_raw.stdout.decode().split("\n")
        network_addrs:     list[list[str]] = []
        for line in network_addrs_raw:
            if ip_addr_re.findall(line):
                print(line, line.split(" ")[-2:])

def net_scan():
    return local_network()

if __name__ == "__main__":
    local_network()
