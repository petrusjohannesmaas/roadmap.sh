# Linux SSH Server Setup

## Project Overview
This project is designed to help users understand and configure SSH access on a remote Linux server. It covers setting up SSH keys, configuring aliases, and implementing basic security measures.

## Requirements
- A remote Linux server or Virtual Machine (AWS, DigitalOcean, etc.)
- Two SSH key pairs
- Ability to SSH into the server using each key
- Optional: Fail2Ban setup for security

### Future improvements:
- Add more security measures
- Add email notifications for fail2ban

## Setup Guide

### 1. Register a Linux Server
Choose a provider such as DigitalOcean or AWS and set up a basic Linux server.

### 2. Generate and Add SSH Keys
Run the following commands:
```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_tester1
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_tester2
ssh-copy-id -i ~/.ssh/id_ed25519_tester1 user@server-ip
ssh-copy-id -i ~/.ssh/id_ed25519_tester2 user@server-ip
```
### 3. Test SSH Access
```bash
ssh -i ~/.ssh/id_ed25519_tester1 user@server-ip
ssh -i ~/.ssh/id_ed25519_tester2 user@server-ip
```

### 4. Configure SSH Alias
Modify `~/.ssh/config` to simplify SSH commands:
```
Host myserver
    HostName server-ip
    User user
    IdentityFile ~/.ssh/id_ed25519_tester1
Host myserver-alt
    HostName server-ip
    User user
    IdentityFile ~/.ssh/id_ed25519_tester2
```
Now, connect using:
```bash
ssh myserver
ssh myserver-alt
```

### 5. (Optional) Fail2Ban
To install and configure **Fail2Ban** for the first time on a **Debian** server, follow these steps:

---

## ✅ Step 1: Update your package list

```bash
sudo apt update
```

---

## ✅ Step 2: Install Fail2Ban

```bash
sudo apt install fail2ban -y
```

This installs the Fail2Ban service and dependencies.

---

## ✅ Step 3: Copy the default config to a local config

You should never modify the default `jail.conf`. Instead, create a local override:

```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

Fail2Ban uses `jail.local` to override settings.

---

## ✅ Step 4: Edit the jail.local configuration

Open the config file:

```bash
sudo nano /etc/fail2ban/jail.local
```

Look for the `[DEFAULT]` section. You can configure:

```ini
[DEFAULT]
# Ban IP for 10 minutes
bantime = 10m

# Wait 10 minutes before retrying
findtime = 10m

# Ban after 5 failed attempts
maxretry = 5

# Ban IPs using iptables
backend = systemd
banaction = iptables-multiport

# Notification email
destemail = you@example.com
sender = fail2ban@example.com
mta = sendmail
action = %(action_mwl)s
```

### Common Jail Example (SSH):

```ini
[sshd]
enabled = true
port    = ssh
logpath = %(sshd_log)s
backend = systemd
```

---

## ✅ Step 5: Restart and enable Fail2Ban

```bash
sudo systemctl restart fail2ban
sudo systemctl enable fail2ban
```

---

## ✅ Step 6: Check Fail2Ban status

```bash
sudo fail2ban-client status
```

To check a specific jail (like sshd):

```bash
sudo fail2ban-client status sshd
```

---

## 🔒 Additional Tips:

* Make sure your firewall (e.g., `ufw`) is active and only allows the necessary ports.
* You can add custom jails for services like Nginx, Postfix, Dovecot, etc.
* Logs are typically stored in `/var/log/fail2ban.log`.

## Testing Fail2Ban with SSH

You can **test Fail2Ban** by simulating repeated failed login attempts to a service it protects—commonly SSH.

#### 🚨 Caution

If you’re testing from **your main workstation**, you may lose SSH access. Always have:

* **Console access** via hosting panel or physical machine
* Or test from **a VM or Docker container**


### **1. Confirm SSH Jail Is Enabled**

Check if SSH protection is active:

```bash
sudo fail2ban-client status sshd
```

Look for:

* `Status: active`
* `Currently banned: 0`
* `Total banned: X`

If it’s not enabled, make sure the `[sshd]` section in `/etc/fail2ban/jail.local` has `enabled = true`.

---

### **2. Trigger Fail2Ban (from another machine or localhost)**

Simulate multiple failed SSH login attempts using a nonexistent user:

```bash
ssh fakeuser@your_server_ip
```

When prompted for a password, just press enter or type anything.

Repeat this **5+ times** (or however many are set in `maxretry`).

> If you’re using the **same machine** to test, you can run:

```bash
for i in {1..6}; do ssh fakeuser@localhost; done
```

---

### **3. Check if IP is banned**

Run this on the server:

```bash
sudo fail2ban-client status sshd
```

Look for your IP under "Banned IP list".

---

### **4. Check the Fail2Ban Log**

```bash
sudo tail -f /var/log/fail2ban.log
```

You’ll see log entries for:

* Detected failed attempts
* Banning action
* IP address blocked

---

### ✅ Unban Your IP (if needed)

If you locked yourself out or want to reset:

```bash
sudo fail2ban-client set sshd unbanip YOUR.IP.ADDRESS
```

## Outcome
After completing this setup, you will be able to SSH securely into your server using both keys.

---