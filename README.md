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

## Usage

There are five usage commands, which you can see by running `sudo vault help`:

```
$ sudo vault help
Usage: sudo vault [OPTION]
        
     init       Create vault in current directory.
     add        Add entry to vault. 
     get        Get entry from vault.
     list       List vault entries.
     remove     Remove existing entry.
     destroy    Completely remove vault in current directory.
     session    Open vault and perform several actions.
     help       Show this text.
     version    Show version information.

```

## Transition vault to python

Ideas:
* use pycrypto to generate hash of masterkey and encrypted vesions of the passwords.
* install pycrypto inside a python virtualenv, stored in a folder according to the XDG Base Directory Specification, store the script in /usr/local/bin, and at the top use a shebang that specifies the python interpreter of the virtualenv.
* store the passwords in a .json file, facilitating user backups.
* add the option of generating strong passwords.
