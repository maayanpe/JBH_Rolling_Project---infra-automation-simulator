#!/usr/bin/env bash

MACHINE="$1"
SERVICE="$2"
LOG_PATH="${LOG_PATH:-/dev/null}"   # default if not set

# log
log() {
  echo "$@"
  echo "$(date '+%F %T') $@" >> "$LOG_PATH"
}

# check input
if [ -z "$MACHINE" ] || [ -z "$SERVICE" ]; then
  log "Usage: $0 <machine_address> <service_name>"
  exit 1
fi

log "======================================"
log "Start installation"
log "Machine: $MACHINE"
log "Service: $SERVICE"
log "--------------------------------------"

# connect
log "Connecting to $MACHINE ..."
sleep 1
if [ $? -ne 0 ]; then
  log "ERROR: failed to connect to $MACHINE"
  exit 2
else
  log "Connected successfully to $MACHINE"
fi

# check service
log "Checking if $SERVICE is already installed ..."
sleep 1
if [ "$SERVICE" = "fail" ]; then
  log "ERROR: installation of $SERVICE failed"
  exit 3
else
  log "$SERVICE is not installed. Installing ..."
fi

# install
sleep 2
if [ $? -ne 0 ]; then
  log "ERROR: installation failed"
  exit 4
else
  log "$SERVICE installed successfully on $MACHINE."
fi

log "End installation"
log "======================================"
exit 0
