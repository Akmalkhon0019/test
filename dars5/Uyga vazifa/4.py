def vazifa(nol):
    return len(nol) - len(nol.lstrip('0'))
sonlar = ['1000', '001', '000123456789', '0000']
for nol_bor in sonlar:
    print(f"{nol_bor} sonining boshida: {vazifa(nol_bor)} ta nol bor")
