## About

Vault is a password-storage utility. It stores passwords using the AES encryption protocol, which can later be decrypted and read by the vault owner. \
The password are stored in a JSON file, '.vault', which looks like this: \
{"e74932441851f29e0fa953edd69e3ddda5a7d565fad3f9a86954afbd5c6d78d4": "fc613b4dfd6736a7bd268c8a0e74ed0d1c04a959f59dd74ef2874983fd443fc9", \
 "e43c4043d4c7f3ef3c8d21bea0ae53b8ab2a984dfe67fbdbdd6820bd21cb538a": "7bd80ff06bcbd8bd6032b940fd1c344b49eb402fa4c72ab55e2aab9600a877d2", \
 "c3b0bdba6a395a49478d84b784afbc87cd6443e959955d007fdb91dde7b590d2": "6bdcefbeeecf2c47e3ab05496a7fdeadcd72de52561035d286b2ca56b9f97cef"}

## WARNING

I'm in no way an expert in shell scripting or cryptography. However, I'll try to update this script regularly and make it more robust and safe. 
I hope this script will eventually be analysed by security experts so that it can be used with more confidence.

## Installation

Clone the repository, hop into the repo's directory and run `bash install.bash`, like so:

```
git clone https://github.com/lhugens/vault && cd vault && bash install.bash && cd -
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
$ vault --help
usage: vault [-h] option

positional arguments:
  option      (a)dd, (l)ist, (s)earch, (g)et, (r)emove, session

optional arguments:
  -h, --help  show this help message and exit
```
