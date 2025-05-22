#!/bin/bash

echo "Generating CPU load..."
for i in {1..4}; do yes > /dev/null & done

echo "Generating Disk I/O..."
dd if=/dev/zero of=tempfile bs=1M count=1024 status=progress

echo "System load test initiated, check Netdata for metrics."

# Cleanup and stop CPU load after timeout
sleep 60
killall yes
rm tempfile
