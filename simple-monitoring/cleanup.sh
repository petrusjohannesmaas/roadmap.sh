#!/bin/bash
echo "Removing Netdata..."
sudo systemctl stop netdata
sudo apt remove --purge netdata -y
sudo yum remove netdata -y
echo "Cleanup complete!"