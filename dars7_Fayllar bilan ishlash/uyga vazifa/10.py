def lotin_harf_soni(fayl_nomi):
    with open(fayl_nomi, 'r') as fayl:
        matn = fayl.read()
        harf_soni = 0
        for belgi in matn:
            if belgi.isalpha():
                harf_soni += 1
    return harf_soni
kod = "#include <iostream> int main() { return 0; }"
with open("kod.txt", 'w') as fayl:
    fayl.write(kod)
print("Lotin harflar soni:", lotin_harf_soni("kod.txt"))
