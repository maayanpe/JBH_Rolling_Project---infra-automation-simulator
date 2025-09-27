#!/usr/bin/env bash

# פרמטרים מהיוזר
MACHINE="$1"
SERVICE="$2"

# בדיקה שקיבלנו פרמטרים
if [ -z "$MACHINE" ] || [ -z "$SERVICE" ]; then
  echo "Usage: $0 <machine_address> <service_name>"
  exit 1
fi

echo "======================================"
echo "Start installation simulation"
echo "Machine: $MACHINE"
echo "Service: $SERVICE"
echo "--------------------------------------"

# כאן אנחנו רק מדמים, לא באמת מתקינים
echo "Connecting to $MACHINE ..."
sleep 1
echo "Checking if $SERVICE is already installed on $MACHINE ..."
sleep 1
echo "$SERVICE is not installed. Simulating installation ..."
sleep 2
echo "$SERVICE installed successfully on $MACHINE (simulation)."

echo "End installation simulation"
echo "======================================"
exit 0
