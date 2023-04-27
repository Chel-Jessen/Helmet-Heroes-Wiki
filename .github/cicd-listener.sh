#!/bin/bash

while true; do
  # Listen for incoming connections on port 6402
  request=$(echo -ne "HTTP/1.1 200 OK\r\n\r\n" | nc -l -p 6402)

  # Check for requests on the "/github" route
  if [[ "$request" =~ /github ]]; then
    # Perform git pull in git directory
    cd /Helmet-Heroes-Wiki && git pull
    # Run docker-compose up --build
    docker-compose up --build
  fi
done