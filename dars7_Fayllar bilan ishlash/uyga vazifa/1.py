def rangli_matn(matn):
    natija = ""
    for belgi in matn:
        if belgi.isupper():
            natija += f"\033[91m{belgi}\033[0m"  
        elif belgi.isdigit():
            natija += f"\033[94m{belgi}\033[0m"
        elif belgi.islower():
            natija += f"\033[92m{belgi}\033[0m"
        else:
            natija += belgi
    return natija
matn = "FINAL! 14chi iyul soat 00:00da EVRO finali Angliya va Ispaniya o'rtasida bo'ladi."
print(rangli_matn(matn))