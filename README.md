## About

Vault is a password-storage utility. It stores passwords using the AES encryption protocol, which can later be decrypted and read by the vault owner.

## WARNING

I'm in no way an expert in shell scripting or cryptography. However, I'll try to update this script regularly and make it more robust and safe. 
I hope this script will eventually be analysed by security experts so that it can be used with more confidence.

## Installation

Clone the repository, hop into the repo's directory and run `bash install.bash`, like so:

```
$ git clone https://github.com/lhugens/vault && cd vault && bash install.bash && cd -
```

To remove the program, just run `bash uninstall.bash`.

## Add the script to $PATH

For convenience, add the ~/.local/bin directory, where the script resides, to your $PATH. \
One way to do this is to add the following line to your shell config file (eg. ~/.bashrc):

```
export PATH="$HOME/.local/bin${PATH:+:${PATH}}"
```

## Dependencies

It uses the PyCrypto package, which is installed in the python virtual environment "vault-venv". This setup is automatically done by install.bash. Both the script and the environment are stored in ~/.local/bin

## Usage

The vault can be open in a session, where the user can perform several actions sequentialy without needing to retype the vault key. It can also just perform one action (eg. "vault add").

```
$ vault session
key: 
options: (a)dd, (r)emove, (q)uit, (o)ptions
--------------------
option:

```
