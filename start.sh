#!/bin/bash

set -e -u -o pipefail

python_wrapper() {
    local PYTHON

    if command -v python3; then
        PYTHON=python3
    elif command -v python; then
        PYTHON=python
    elif command -v py; then
        PYTHON=py
    else
        echo 'Python is not installed'
        exit 1
    fi

    $PYTHON "$@"
}

setup() {
    rm -rf '.venv'

    python_wrapper -m venv .venv

    # shellcheck disable=SC1091
    source .venv/bin/activate || source .venv/Scripts/activate

    pip install -r requirements.txt
}

# shellcheck disable=SC2154
trap 'rv=$?; deactivate &>/dev/null; exit $rv' EXIT

setup &>/dev/null

python_wrapper ▚ "$@" # Byt ▚ till ditt skripts namn.
