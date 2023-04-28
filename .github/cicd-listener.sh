#!/bin/bash

# Get GitHub's webhook IP addresses
GITHUB_IP_ADDRESSES=$(curl -s https://api.github.com/meta | jq -r '.hooks | join(" ")')

while true; do
  # Listen for incoming connections on port 6402 and get the client IP address
  connection=$(nc -l -p 6402)
  client_ip=$(echo "$connection" | head -1 | awk '{print $2}')
  request=$(echo -ne "HTTP/1.1 200 OK\r\n\r\n" | nc -w 1 "$client_ip" 6402)

  # Check if the client IP address is in the list of GitHub's IP addresses
  if [[ " $GITHUB_IP_ADDRESSES " =~  $client_ip  ]]; then
    # Check for requests on the "/github" route
    if [[ "$request" =~ /github ]]; then
      # Perform git pull in git directory
      cd /Helmet-Heroes-Wiki && git pull
      # Run docker-compose up --build
      docker-compose up --build
    fi
  else
    echo "Request not from GitHub's IP addresses by: $client_ip"
  fi
done
