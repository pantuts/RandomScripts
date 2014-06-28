# Copy and save it as wgetIP.sh
#!/usr/bin/sh
wget --quiet ifconfig.me
ip=$(cat index.html | grep "ip_address\"" | sed s/\>/\ /g | awk '{print $5}' | cut -d '<' -f 1 && rm index*)
echo "IP: " ${ip}
# End
