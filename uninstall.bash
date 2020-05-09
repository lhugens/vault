#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        printf '%s\n' "This is a linux-gnu system."
        SCRIPTDIR=/usr/local/bin
elif [[ "$OSTYPE" == "darwin"* ]]; then
        printf '%s\n' "This is a macOS system."
        SCRIPTDIR=/usr/local/bin
fi

[ -f ${SCRIPTDIR}/vault ] && sudo rm ${SCRIPTDIR}/vault || true

printf '%s\n' "Script removed from "${SCRIPTDIR}""
