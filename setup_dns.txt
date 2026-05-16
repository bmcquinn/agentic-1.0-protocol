#!/bin/bash

# Configuration - Replace these with your actual details
API_TOKEN="your_cloudflare_api_token"
ZONE_ID="your_cloudflare_zone_id"
DOMAIN="yourdomain.dev"

# GitHub Pages Target IPs
GH_IPS=("185.199.108.153" "185.199.109.153" "185.199.110.153" "185.199.111.153")
GH_CNAME="bmcquinn.github.io"

echo "Starting DNS configuration for $DOMAIN..."

# 1. Create A Records for the Apex Domain
for ip in "${GH_IPS[@]}"; do
    echo "Adding A record pointing to $ip..."
    curl -s -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
         -H "Authorization: Bearer $API_TOKEN" \
         -H "Content-Type: application/json" \
         --data "{\"type\":\"A\",\"name\":\"@\",\"content\":\"$ip\",\"ttl\":120,\"proxied\":false}" \
         | grep -q '"success":true' && echo "✓ Success" || echo "✗ Failed"
done

# 2. Create CNAME Record for www
echo "Adding CNAME record for www -> $GH_CNAME..."
curl -s -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
     -H "Authorization: Bearer $API_TOKEN" \
     -H "Content-Type: application/json" \
     --data "{\"type\":\"CNAME\",\"name\":\"www\",\"content\":\"$GH_CNAME\",\"ttl\":120,\"proxied\":false}" \
     | grep -q '"success":true' && echo "✓ Success" || echo "✗ Failed"

echo "DNS setup process complete."
