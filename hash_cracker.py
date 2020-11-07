import hashlib, os, sys, time
from colorama import Fore, Back, Style, init
from tqdm import tqdm
from passlib.handlers.windows import lmhash, nthash
init()
usage = Fore.YELLOW + """
              Usage :                    |            Available HASH : 
  Arg1 -- The hash's algorithm           |          MD5 ----------- md5
  Arg2 -- The hash you wants to crack    |       SHA256 ----------- sha256
  Arg3 -- The path to the wordlist       |       SHA512 ----------- sha512
                                                   NT --------------- Nt
                                                   LM --------------- Lm
                                                   
  Example : python3 <hash_type> <your_hash> <path_to_the_wordlist>
  Example : python3 <hash_type> <your_hash> #select the default wordlist (rockyou) 
""" + Fore.RESET

class bruteforcing:
    def md5(UA):
        t1 = time.time()
        global counter
        print("[*] Attacking md5 hash",UA, "by bruteforce.")
        for line in tqdm(file,total=len(list(open(path_to_WL,"rb"))),unit="pass"):
            line = line.replace("\n","")
            guess = hashlib.md5(line.encode()).hexdigest()
            counter += 1
            bruteforcing.final(UA,line,counter,guess,t1)

    def sha256(UA):
        t1 = time.time()
        global counter
        print("[*] Attacking Sha256 hash",UA,"by bruteforce.")
        for line in tqdm(file,total=len(list(open(path_to_WL,"rb"))),unit="pass"):
            line = line.replace("\n","")
            guess = hashlib.sha256(line.encode()).hexdigest()
            counter += 1
            bruteforcing.final(UA,line,counter,guess,t1)

    def sha512(UA):
        t1 = time.time()
        global counter
        print("[*] Attacking sha512 hash", UA, "by bruteforce.")
        for line in tqdm(file,total=len(list(open(path_to_WL,"rb"))),unit="pass"):
            line = line.replace("\n","")
            guess = hashlib.sha512(line.encode()).hexdigest()
            counter += 1
            bruteforcing.final(UA,line,counter,guess,t1)

    def final(UA,line,counter,guess,t1):
        if guess == UA:
            HR,tt = utilitaries.hashratebf(t1)
            print("\n[*] The corresponding string to",UA,"is "+Fore.RED+line+Fore.RESET)
            print("[*] Found in "+Fore.RED,tt,"seconds",Fore.RESET,"and",Fore.RED,counter,"hash tested",Fore.RESET)
            print("[+] HashRate in",sys.argv[1],":"+Fore.YELLOW,HR,"/s"+Fore.RESET)
            exit()


class windows:
    def ntH(UA):
        t1 = time.time()
        global counter
        print("[*] Attacking NT hash : {}".format(UA))
        for line in tqdm(file,total=len(list(open(path_to_WL,"rb"))),unit="pass"):
            line = line.replace("\n","")
            guess = nthash.hash(line.encode())
            counter += 1
            bruteforcing.final(UA,line,counter,guess,t1)

    def lmH(UA):
        t1 = time.time()
        global counter
        print("[*] Attacking LM hash : {}".format(UA))
        for line in tqdm(file,total=len(list(open(path_to_WL,"rb"))),unit="pass"):
            line = line.replace("\n","")
            guess = lmhash.hash(line.encode())
            counter += 1
            bruteforcing.final(UA,line,counter,guess,t1)



class utilitaries:
    def define_mode():
        if sys.argv[1] == "md5" or sys.argv[1] == "MD5":
            bruteforcing.md5(UserHash)
        if sys.argv[1] == "sha256" or sys.argv[1] == "SHA256":
            bruteforcing.sha256(UserHash)
        if sys.argv[1] == "sha512" or sys.argv[1] == "SHA512":
            bruteforcing.sha512(UserHash)
        if sys.argv[1] == "nt" or sys.argv[1] == "NT" or sys.argv[1] == "Nt":
            windows.ntH(UserHash)
        if sys.argv[1] == "lm" or sys.argv[1] == "LM" or sys.argv[1] == "Lm":
            windows.lmH(UserHash)
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def hashratebf(t1):
        t2 = time.time()
        tt = t2 - t1
        try :
            HR = counter/tt
        except:
            HR = "Too short interval to properly mesuring hashrate"
        return HR,tt

counter = 0
if len(sys.argv) < 3:
    utilitaries.clear()
    print(usage)
elif len(sys.argv) == 3:
    utilitaries.clear()
    UserHash = sys.argv[2]
    print("selecting default wordlist (rockyou)...")
    path_to_WL = "rockyou.txt"
    file = open(path_to_WL,"r",errors='ignore')
    utilitaries.define_mode()
else:
    utilitaries.clear()
    UserHash = sys.argv[2]
    path_to_WL = sys.argv[3]
    file = open(path_to_WL,"r",errors='ignore')
    utilitaries.define_mode()
