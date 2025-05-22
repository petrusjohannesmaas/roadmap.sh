#!/bin/bash
echo "Installing Netdata..."
bash <(curl -Ss https://my-netdata.io/kickstart.sh)
echo "Starting Netdata..."
sudo systemctl enable netdata
sudo systemctl start netdata
echo "Allowing firewall access..."
sudo ufw allow 19999/tcp
echo "Netdata setup complete. Access it via: http://$(hostname -I | awk '{print $1}'):19999/"