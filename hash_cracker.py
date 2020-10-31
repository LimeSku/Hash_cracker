import hashlib, os, sys, time, threading

usage = """
Usage :                                               Available HASH : 
  Arg1 -- The hash's algorithm                          MD5 -- md5
  Arg2 -- The hash you wants to crack                   SHA256 -- sha256
  Arg3 -- The path to the wordlist                      SHA512 -- sha512

  Example : python3 <hash_type> <your_hash> <path_to_the_wordlist> 
"""

def md5_decrypt(UA):
    t1 = time.time()
    counter = 0
    print("[*] Attacking md5 hash",UA, " by bruteforce.")
    for line in file:
        line = line.replace("\n","")
        md5_hash = hashlib.md5(line.encode()).hexdigest()
        counter += 1
        if md5_hash == UA:
            t2 = time.time()
            tt = t2 - t1
            HR = counter/tt
            print("[*] The corresponding string to",UA,"is",line)
            print("[*] Found in ",tt, "seconds and ",counter,"hash tested")
            print("[++] HashRate : ",HR,"/s" )
            break


def sha256_decrypt(UA):
    t1 = time.time()
    counter = 0
    print("[*] Attacking Sha256 hash",UA,"by bruteforce.")
    for line in file:
        line = line.replace("\n","")
        sha256_hash = hashlib.sha256(line.encode()).hexdigest()
        counter += 1
        if sha256_hash == UA:
            t2 = time.time()
            tt = t2 - t1
            HR = counter/tt
            print("[*] The corresponding string to",UA,"is",line)
            print("[*] Found in ",tt, "seconds and ",counter,"hash tested")
            print("[++] HashRate : ",HR,"/s" )
            break

def sha512_decrypt(UA):
    t1 = time.time()
    counter = 0
    print("[*] Attacking sha512 hash", UA, "by bruteforce.")
    for line in file:
        line = line.replace("\n","")
        sha512_hash = hashlib.sha512(line.encode()).hexdigest()
        counter += 1
        if sha512_hash == UA:
            t2 = time.time()
            tt = t2 - t1
            HR = counter/tt
            print("[*] The corresponding string to",UA,"is",line)
            print("[*] Found in ",tt, "seconds and ",counter,"hash tested")
            print("[++] HashRate in",sys.argv[1],":",HR,"/s" )
            break

if len(sys.argv) < 4:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(usage)
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    UserHash = sys.argv[2]
    path_to_WL = sys.argv[3]
    file = open(path_to_WL,"r",errors='ignore')
    if sys.argv[1] == "md5" or sys.argv[1] == "MD5":
        md5_decrypt(UserHash)
    if sys.argv[1] == "sha256" or sys.argv[1] == "SHA256":
        sha256_decrypt(UserHash)
    if sys.argv[1] == "sha512" or sys.argv[1] == "SHA512":
        sha512_decrypt(UserHash)
