#!/bin/bash

# Script to collect logs from various devices in the home networking lab

# Define the devices and their log file locations
declare -A devices
devices=(
    ["router"]="/var/log/router.log"
    ["switch"]="/var/log/switch.log"
    ["access_point"]="/var/log/access_point.log"
    ["server"]="/var/log/server.log"
)

# Directory to store collected logs
log_dir="./collected_logs"
mkdir -p "$log_dir"

# Collect logs from each device
for device in "${!devices[@]}"; do
    log_file="${devices[$device]}"
    if [ -f "$log_file" ]; then
        cp "$log_file" "$log_dir/${device}_log_$(date +%Y%m%d_%H%M%S).log"
        echo "Collected logs from $device"
    else
        echo "Log file for $device not found: $log_file"
    fi
done

echo "Log collection completed."