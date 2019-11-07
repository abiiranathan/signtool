#!/usr/bin/env python3

from fs import open_fs
import gnupg
import sys

gpg = gnupg.GPG(gnupghome='/home/nabiizy/.gnupg')
home_fs = open_fs('.')
try:
    script_to_run = sys.argv[1]
except IndexError:
    raise SystemExit(f'Usage: python3 {sys.argv[0]} script.py')


with open("../../signatures/" + script_to_run + ".sig", "rb") as f:
    verify = gpg.verify_file(f, script_to_run)
    print(script_to_run + " ", verify.status)
    if verify.status == "signature valid":
        print("Signature valid, launching script...")
        exec(open(script_to_run).read())
    else:
        print("Signature invalid or missing, ")
        print("aborting script execution")
