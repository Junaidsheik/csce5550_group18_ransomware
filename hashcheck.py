import hashlib

hashcheck = r"" #file location to check the hash
hasher = hashlib.sha256()
with open(hashcheck,'rb') as open_file:
    content = open_file.read()
    hasher.update(content)
print ("sha256 checksum of the file is: " + hasher.hexdigest())

