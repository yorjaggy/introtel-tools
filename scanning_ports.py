# remember to have scapy installed
# pip install scapy

from scapy.all import *
dst_ip = '127.0.0.1'
max_range_port=4000
ans,unans=sr(IP(dst=dst_ip)/TCP(flags='S', dport=(1,max_range_port)))
ans.nsummary()