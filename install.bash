#!/usr/bin/bash

she() { 
echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
}

[ -d ~/.local/bin ] || { mkdir ~/.local ;  mkdir ~/.local/bin ; }

cp vault ~/.local/bin/. &&

cd ~/.local/bin &&

python3 -m venv vault-venv &&

vault-venv/bin/pip install --upgrade pip &&

vault-venv/bin/pip install pycrypto &&

abspath=$(she vault-venv/bin/python3) &&

echo "#!$(echo "$abspath" )" | cat - vault > temp && mv temp vault &&

chmod u+r+x vault && 

cd - &&

cat addtopath.txt

