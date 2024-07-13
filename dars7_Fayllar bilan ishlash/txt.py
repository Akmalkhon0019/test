import re
from collections import defaultdict

def faylni_ishla(fayl_nomi):
    mac_andaza = re.compile(r'\b(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})\b')
    email_andaza = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')

    email_domenlar = defaultdict(int)

    with open(fayl_nomi) as fayl:
        mazmuni = fayl.read()

        mac_manzillar = mac_andaza.findall(mazmuni)
        print("Harf qatnashgan MAC manzillar:")
        for mac in mac_manzillar:
            if any(c.isalpha() for c in mac):
                print(mac)

        # Email manzillarini ajratish va domenlarni hisoblash
        email_manzillar = email_andaza.findall(mazmuni)
        print("\nEmail manzillar:")
        for email in email_manzillar:
            print(email)
            domen = email.split('@')[1]
            email_domenlar[domen] += 1

    print("\nEmail domenlarining soni:")
    for domen, son in email_domenlar.items():
        print(f"{domen}: {son}")

# Fayl nomi bilan funksiyani chaqiring
faylni_ishla("Bitiklar.txt")

