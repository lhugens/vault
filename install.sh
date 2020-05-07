#!/bin/bash

SCRIPTDIR=/usr/bin

[ -f vault ] && sudo cp vault ${SCRIPTDIR} || true

[ -f ${SCRIPTDIR}/vault ] && sudo chmod 100 ${SCRIPTDIR}/vault || true