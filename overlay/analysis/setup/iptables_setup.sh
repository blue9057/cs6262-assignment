#!/bin/bash
sudo iptables -t nat -F
sudo iptables -F
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo iptables -A FORWARD -i enp0s3 -o br0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i br0 -o enp0s3 -p tcp -s 192.168.133.2 ! -d 128.61.240.187 -j DROP
sudo iptables -A FORWARD -i br0 -o enp0s3 -j ACCEPT
sudo iptables -A OUTPUT -s 192.168.133.2 -d  128.61.240.187 -j ACCEPT
sudo iptables -A OUTPUT -p tcp -s 192.168.133.2 ! -d 192.168.133.0/24 -j DROP
source /home/analysis/tools/network/iptables-rules
