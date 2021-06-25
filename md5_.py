#!/usr/bin/python

import hashlib

md5_hash = input(" [*] MD% kodni kiriting ")
#parol_list = str(urlopen("https://github.com/iryndin/10K-Most-Popular-Passwords/blob/master/passwords.txt").read(), 'utf-8')
parol_list = open("parol.txt", 'r')

for parol in parol_list.readlines():
        parol = parol.strip("\n")

        hash_tahmin = hashlib.md5(bytes(parol, 'utf-8')).hexdigest()
        if hash_tahmin == md5_hash:
                print(" [2] parol topildi: "+ parol)
                quit()
        else:
                print("  [%%] keyingisi !! hash togri kelmadi: "+ hash_tahmin )
print("[parol topilmadi // oxshashlik yoq parol listda!!!!!]")
