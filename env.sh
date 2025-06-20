#!/bin/bash
# Environment variables for macOS/Linux systems

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# User home directory
HOME_DIR="$HOME"

# System paths
PATH="$PATH:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
if [ -d "/opt/homebrew/bin" ]; then  # Homebrew on Apple Silicon
    PATH="/opt/homebrew/bin:$PATH"
fi

# Temporary directories
TMPDIR="${TMPDIR:-/tmp}"
TEMPDIR="${TEMPDIR:-/tmp}"

# Application directories
APPLICATIONS_DIR="/Applications"
if [ "$(uname)" = "Linux" ]; then
    APPLICATIONS_DIR="/usr/share/applications"
fi

# System information
OS_NAME="$(uname -s)"
OS_ARCH="$(uname -m)"
HOSTNAME="$(hostname)"

# Export all variables
export SCRIPT_DIR HOME_DIR PATH TMPDIR TEMPDIR APPLICATIONS_DIR OS_NAME OS_ARCH HOSTNAME

# Safety check to prevent recursive sourcing
if [ -z "$ENV_SH_LOADED" ]; then
    export ENV_SH_LOADED=1
else
    echo "Warning: env.sh already loaded" >&2
fi
