#!/bin/bash
# Simple load generator to trigger HPA scaling

SERVICE_URL="http://localhost:30007/health"

echo "Starting load test on $SERVICE_URL"
echo "Press CTRL+C to stop"

while true; do
  curl -s $SERVICE_URL > /dev/null
  sleep 0.01
done
