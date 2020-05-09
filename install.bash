#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        printf '%s\n' "This is a linux-gnu system."
        SCRIPTDIR=/usr/local/bin
elif [[ "$OSTYPE" == "darwin"* ]]; then
        printf '%s\n' "This is a macOS system."
        SCRIPTDIR=/usr/local/bin
fi


[ -f vault ] && sudo cp vault ${SCRIPTDIR} || true

[ -f ${SCRIPTDIR}/vault ] && sudo chmod 100 ${SCRIPTDIR}/vault || true

printf '%s\n' "Script location: "${SCRIPTDIR}/vault""
