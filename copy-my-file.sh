#!/bin/bash

VERSION="1.0"
DEFAULT_DIST="/Volumes/Transcend/"
SOURCE_LIST=("$HOME/workspace" "$HOME/.zshrc" "$HOME/@bin")

# Color definitions
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Validate path existence
validate_path() {
    local path="$1"
    local default="$2"
    local description="$3"

    if [ -z "$path" ]; then
        # Use default if no path provided
        echo "$default"
    elif [ ! -e "$path" ]; then
        # Error if path doesn't exist
        echo -e "${RED}Error: $description '$path' does not exist${NC}" >&2
        exit 1
    else
        # Use provided path if it exists
        echo "$path"
    fi
}

copy() {
    local source="$1"
    local dist="$2"

    # Validate destination path (use default if not provided)
    dist=$(validate_path "$dist" "$DEFAULT_DIST" "Destination path")


    if [ -n "$source" ]; then
        # Validate and use provided source path
        source=$(validate_path "$source" "" "Source path")
        echo "Copying $source to $dist"
        if [ -d "$source" ]; then
            cp -R "$source" "$dist"
            echo -e "${YELLOW}Copied directory $source to $dist${NC}"
        else
            cp "$source" "$dist"
            echo -e "${YELLOW}Copied file $source to $dist${NC}"
        fi
    else
        # Use SOURCE_LIST if no source provided
        for source in "${SOURCE_LIST[@]}"; do
            echo "Copying $source to $dist"
            if [ -e "$source" ]; then
                if [ -d "$source" ]; then
                    cp -R "$source" "$dist"
                    echo -e "${YELLOW}Copied directory $source to $dist${NC}"
                else
                    cp "$source" "$dist"
                    echo -e "${YELLOW}Copied file $source to $dist${NC}"
                fi
            fi
        done
    fi
}

copy "$1" "$2"