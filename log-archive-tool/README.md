# Log Archive Tool

### **Project Structure**
```
log-archive/
├── log-archive.sh  # Bash script
├── README.md       # Documentation
└── archives/       # Directory where archived logs will be stored
```

---

## Overview
This Bash-based CLI tool archives logs by compressing them into a `.tar.gz` file and storing them in a dedicated `archives` directory. It ensures old logs are stored efficiently while keeping your system clean.

## Features
- Accepts the log directory as an argument.
- Compresses logs using `tar.gz`.
- Stores archives in a designated folder.
- Logs the archive creation date and time.

## Requirements
- Unix-based system (Linux/macOS)
- Bash shell
- `tar` command available

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/petrusjohannesmaas/roadmap.sh/
   cd log-archive-tool
   ```

2. Make the script executable:
   ```bash
   chmod +x log-archive.sh
   ```

## Usage
Run the script with the desired log directory:
```bash
./log-archive.sh /var/log
```
Example output:
```
Logs archived successfully: archives/logs_archive_20240816_100648.tar.gz
```

## Advanced Features
Want to enhance the tool? Here are some ideas:
- Schedule automatic archiving via `cron`.
- Send email notifications upon completion.
- Upload archives to remote storage (via `scp` or `rsync`).
