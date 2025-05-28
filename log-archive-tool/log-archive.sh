#!/bin/bash

# Ensure a directory is provided
if [ $# -ne 1 ]; then
    echo "Usage: log-archive <log-directory>"
    exit 1
fi

LOG_DIR=$1
ARCHIVE_DIR="archives"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ARCHIVE_NAME="logs_archive_$TIMESTAMP.tar.gz"

# Create archive directory if not exists
mkdir -p "$ARCHIVE_DIR"

# Compress logs
tar -czf "$ARCHIVE_DIR/$ARCHIVE_NAME" "$LOG_DIR"

# Log the action
echo "$TIMESTAMP: Archived $LOG_DIR to $ARCHIVE_DIR/$ARCHIVE_NAME" >> "$ARCHIVE_DIR/archive_log.txt"

echo "Logs archived successfully: $ARCHIVE_DIR/$ARCHIVE_NAME"