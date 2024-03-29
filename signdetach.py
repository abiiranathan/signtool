import os
import gnupg
from fs import open_fs
from getpass import getpass
gpg = gnupg.GPG(gnupghome="/home/nabiizy/.gnupg")
home_fs = open_fs(".")

passphrase = getpass('GNUPG Passphrase: ')

if os.path.exists("signatures/"):
    print("Signatures directory already created")
else:
    home_fs.makedir(u"signatures")
    print("Created signatures directory")

files_dir = []

files = [f for f in os.listdir(".") if os.path.isfile(f)]
for f in files:
    files_dir.append(f)


for x in files_dir:
    with open(x, "rb") as f:
        try:
            stream = gpg.sign_file(f, passphrase=passphrase, detach=True, output=files_dir[files_dir.index(x)] + ".sig")
            os.rename(files_dir[files_dir.index(x)] + ".sig", "signatures/" + files_dir[files_dir.index(x)] + ".sig")
            print(x + " ", stream.status)
        except Exception as e:
            print(e)
