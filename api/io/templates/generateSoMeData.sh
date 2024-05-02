#!/bin/bash

# Script to generate social media data without the need to query the API all the time.
# Useful during development to save money on API calls.

# Get the directory of the script
SCRIPT_DIR="$(dirname "$0")"
# Get the path to the .env file to retrieve the API Bearer token
source "$SCRIPT_DIR/../../.env"

# Define the API endpoint
API_URL="https://nubela.co/proxycurl/api/v2/linkedin"

# Public identifiers for LinkedIn, Twitter, and Facebook
LINKED_IN_PUBLIC_IDENTIFIER=""
TWITTER_PUBLIC_IDENTIFIER=""
FACEBOOK_PUBLIC_IDENTIFIER=""

# Check if the API token is set
if [[ -z "$PROXY_CURL_TOKEN" ]]; then
    echo "API token is not set. Exiting script."
    exit 1
fi

# Function to perform curl operations
perform_curl() {
    local service_name="$1"
    local identifier="$2"
    local service_url="$3"

    # Check if the identifier is provided
    if [[ -z "$identifier" ]]; then
        echo "Public identifier for $service_name is missing. Skipping."
        return
    fi

    # Construct the profile URL
    local profile_url="$service_url/$identifier/"

    # Perform the curl request
    curl -G \
         -H "Authorization: Bearer $PROXY_CURL_TOKEN" \
         $API_URL \
         -o "${service_name}_example.json" \
         --data-urlencode "${service_name}_profile_url=$profile_url" \
         --data-urlencode "use_cache=if-present" \
         --data-urlencode "fallback_to_cache=on-error"
}

# Perform LinkedIn API request
perform_curl "linkedin" "$LINKED_IN_PUBLIC_IDENTIFIER" "https://linkedin.com/in"

# Perform Twitter API request
perform_curl "twitter" "$TWITTER_PUBLIC_IDENTIFIER" "https://twitter.com"

# Perform Facebook API request
perform_curl "facebook" "$FACEBOOK_PUBLIC_IDENTIFIER" "https://facebook.com"
