SCRIPTDIR?=/usr/bin

all:
	@echo "Vault is a shell script, so there is nothing to do. Try \"make install\" instead."

install:
	@[ -f vault ] && sudo cp vault ${SCRIPTDIR} || true
	@[ -f ${SCRIPTDIR}/vault ] && sudo chmod 100 ${SCRIPTDIR}/vault || true

uninstall:
	@[ -f ${SCRIPTDIR}/vault ] && sudo rm ${SCRIPTDIR}/vault || true