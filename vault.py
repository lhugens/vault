
from os       import urandom, getcwd, path
from hashlib  import sha256
from base64   import b64encode, b64decode
from json     import load, dump
from re       import search
from binascii import unhexlify
from argparse import ArgumentParser
from getpass  import getpass
from sys      import exit

from Crypto        import Random
from Crypto.Cipher import AES

class aestring:
    def __init__(self, bkey): 
        self.bkey = bkey
    
    def pad(self, s):
        bs = AES.block_size
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    
    def unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
    
    def encrypt(self, plain):
        plain = self.pad(plain)
        iv = urandom(16)
        cipher = AES.new(self.bkey, AES.MODE_CBC, iv)
        bstr = iv + cipher.encrypt(plain.encode())
        return bstr.hex()
    
    def decrypt(self, enc):
        enc = unhexlify(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.bkey, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

class session:
    def __init__(self):
        self.vname = '.vault'
        self.check_vault()
                
    def check_vault(self):
        if (not path.exists(self.vname)) or (not path.isfile(self.vname)):
            self.keygen(getpass('New key: '))
            self.dic = { sha256(urandom(16)).hexdigest() : self.hexkey }

            with open(self.vname, 'w') as outfile:
                dump(self.dic, outfile)

            self.aes = aestring(self.bkey)

        else:
            with open(self.vname) as json_file:
                self.dic = load(json_file)

            self.keygen(getpass('key: '))
            self.auth()
            self.aes = aestring(self.bkey)

    def keygen(self, key):
        self.hexkey = sha256(key.encode()).hexdigest()
        key = key + self.hexkey
        self.bkey   = sha256(key.encode()).digest()

    def auth(self):
        lst = list(self.dic.values())
        if self.hexkey != lst[0]:
            print('Wrong key')
            exit()
    
    def dump(self):
        lst = list(self.dic.keys())
        for entry in lst[1:]:
            print(self.aes.decrypt(entry))
            
    def search(self, s):
        lst = list(self.dic.keys())
        results = []
        for i in range(1,len(lst)):
            entry = self.aes.decrypt(lst[i])
            if search(s, entry) != None:
                results.append(entry)
        return results
            
    def add(self, entry, passwd):
        self.dic[self.aes.encrypt(entry)] = self.aes.encrypt(passwd)
    
    def remove(self, j):
        lst = list(self.dic.keys())
        del self.dic[lst[j]]
    
    def get(self, j):
        lst = list(self.dic.values())
        return self.aes.decrypt(lst[j])
            
    def save(self):
        with open(self.vname, 'w') as outfile:
            dump(self.dic, outfile)

def a_add():
    entry_plain = input('Entry name: ')
    sesh.add(entry_plain, getpass('Password: '))
    sesh.save()

def a_get():
    ss = input('Search: ')
    if ss != '':
        results = sesh.search(ss)
        size = len(results)
        if size != 0:
            for i in range(size):
                print('{} {}'.format(str(i+1), results[i]))
            j = input('Number: ')
            try:
                j = int(j)
                print('The password is : ',sesh.get(j))
            except:
                print('Input is not an integer.')
        else:
            print('No matches found')
    else:
        print('Empty search string.')

def a_remove():
    ss = input('Search: ')
    if ss != '':
        results = sesh.search(ss)
        size = len(results)
        if size != 0:
            for i in range(size):
                print('{} {}'.format(str(i+1), results[i]))
            j = input('Number: ')
            try:
                j = int(j)
                sesh.remove(j)
                sesh.save()
            except:
                print('Input is not an integer.')
    else:
        print('Empty search string.')

def a_options():
    print('options: (a)dd, (g)et, (r)emove, (q)uit, (o)ptions')


parser = ArgumentParser()
parser.add_argument("option", help = 'options') 
args = parser.parse_args()

if args.option in ['add', 'get', 'remove', 'session']:
    sesh = session()
    
    if args.option == 'add':
        a_add()

    if args.option == 'get':
        a_get()
                
    if args.option == 'remove': 
        a_remove()

    if args.option == 'session': 
        a_options()
        while True:
            print('--------------------')
            option = input('option: ')
            
            if option in ['a', 'add']:
                print(' ')
                a_add()

            elif option in ['g', 'get']:
                print(' ')
                a_get()
                        
            elif option in ['r', 'remove']:
                print(' ')
                a_remove()
            
            elif option in ['o', 'options']:
                a_options()

            elif option in ['q', 'quit']:
                exit()

            else:
                print('Not an option. ')

else:
    exit()
