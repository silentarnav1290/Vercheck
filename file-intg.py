import hashlib

inp_file = input(r"Enter the file with full path: ")
ver_file = input(r"Enter the sha256 hash verification file downloaded from the software website or provided with file(Full path): ")

with open(inp_file, 'rb') as op_file:
    content = op_file.read()
    sha256 = hashlib.sha256()
    sha256.update(content)

print("Result!\n")
print("{}:{}".format(sha256.name, sha256.hexdigest()))

with open(ver_file, 'r') as op_file2:
    content2 = op_file2.read()
    print("Verification hash: ", content2)
if content2 == sha256.hexdigest():
    print("[*]Hashes matched\n[+]File is authentic and without any corruption !!!")
else:
    print("[!]Hashes did not match\n[-]File is not authentic and may be corrupted !!!")