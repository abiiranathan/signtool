# Scripts for code signing and verification using GNU gpg
### Relies on python-gpg & fs packages

#### Credits to digital ocean
https://www.digitalocean.com/community/tutorials/how-to-verify-code-and-encrypt-data-with-python-gnupg-and-python-3

# Create executable and put them to path
> chmod +x copy2path.py
> ./copy2path

Let’s start by creating detached signatures for all of the files. To do this, execute the
signdetach script from within the current folder:

> signdetach

With the signatures in place, it’s possible to move on to encrypting our files. To do this,
execute the encryptfiles script:

> encryptfiles

# Decryption of files
## To decrypt the files, run the decryptfiles script from within the current folder:
> cd encrypted/ && ls -l


# Verify detached file (should be run from 'decrypted' files folder)
> cd decrypted
> verifydetach


# Run the python script if the signature is valid after decryption
> verifyfile script.py
