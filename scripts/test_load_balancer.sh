#!/usr/bin/env bash
set -euo pipefail
URL=${1:-http://localhost:18080}
COUNT=${2:-10}

echo "Testing $COUNT requests against $URL" >&2
for i in $(seq 1 "$COUNT"); do
  curl -s "$URL" | grep -o 'web[0-9]' || echo 'no-match'
  sleep 0.2
done | sort | uniq -c
