## About

Vault is a password-storage utility. It stores passwords using the AES encryption protocol, which can later be decrypted and read by the vault owner.

## WARNING

I'm in no way an expert in shell scripting or cryptography. However, I'll try to update this script regularly and make it more robust and safe. 
I hope this script will eventually be analysed by security experts so that it can be used with more confidence.

## Instalation

Clone the repository, hop into the repo's directory and run install.sh:

```
$ git clone https://github.com/lhugens/vault && cd vault && sh install.sh
```

To remove the program, just run `sh uninstall.sh`.

## Usage

There are five usage commands, which you can see by running `sudo vault help`:

```
$ sudo vault help
Usage: sudo vault [OPTION]
        
     init       Create vault in current directory.
     add        Add entry to vault. 
     get        Get entry from vault.
     remove     Remove existing entry.
     help       Show this text.
     version    Show version information.

```