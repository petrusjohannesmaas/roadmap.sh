# Dummy Systemd Service

This is a guide on how to create your own systemd service

### **1. Create the Dummy Script**
Create a file called `dummy.sh` and add the following content:

```bash
#!/bin/bash

while true; do
  echo "$(date) | Dummy service is running..." >> /var/log/dummy-service.log
  sleep 10
done
```

Save the file and make it executable:

```bash
chmod +x dummy.sh
```

Copy the file to the proper directory:
```sh
sudo mv dummy.sh /usr/local/bin/dummy.sh
```

### **2. Create the Systemd Service File**
Create a new systemd service file:

```bash
sudo vi /etc/systemd/system/dummy.service
```

Add the following content:

```ini
[Unit]
Description=Dummy service
After=network.target

[Service]
ExecStart=/usr/local/bin/dummy.sh
Restart=always
User=root
StandardOutput=append:/var/log/dummy-service.log
StandardError=append:/var/log/dummy-service.log

[Install]
WantedBy=multi-user.target
```

Also make sure to set the log file permissions properly to avoid systemd errors:

```sh
sudo touch /var/log/dummy-service.log
sudo chmod 644 /var/log/dummy-service.log
```


### **3. Reload Systemd and Enable the Service**
Run these commands to apply the changes:

```bash
sudo systemctl daemon-reload
sudo systemctl enable dummy
```

### **4. Manage the Service**
You can interact with the service using:

```bash
sudo systemctl start dummy     # Start the service
sudo systemctl stop dummy      # Stop the service
sudo systemctl enable dummy    # Enable the service to start on boot
sudo systemctl disable dummy   # Disable the service
sudo systemctl status dummy    # Check the service status
```

### **5. Check Logs**
Check your log file:

```bash
cat /var/log/dummy-service.log
```

### **6. Ensure the Service Auto-Restarts**
If the service crashes, `Restart=always` ensures it restarts.

---
