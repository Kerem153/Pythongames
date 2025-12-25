import time

# Para
para = 100

# Galeri
galeri_ismi = None
galeri_var = False

# Slotlar
slot_a = "bos"
slot_b = "bos"
slot_c = "bos"
slot_d = "bos"
slot_e = "bos"

# ÜRÜNLER
# 1. Ürün
car1 = "Fiat Doblo"
car1_buy = 100
car1_sell = 150
car1_no = 53946

# 2. Ürün (YENİ)
car2 = "Mercedes-Benz"
car2_buy = 150
car2_sell = 250
car2_no = 85383

def slotlar_dolu_mu():
    return slot_a != "bos" and slot_b != "bos" and slot_c != "bos" and slot_d != "bos" and slot_e != "bos"

# OYUN
while True:
    x = input("Sistem > ")

    if x == "create":
        if galeri_var:
            print("Zaten galeriniz var.")
        else:
            galeri_ismi = input("Galeri ismi: ")
            galeri_var = True
            print("Galeri oluşturuldu")

    elif x == "info":
        if galeri_var:
            print(f"Galeri: {galeri_ismi}")
            print(slot_a)
            print(slot_b)
            print(slot_c)
            print(slot_d)
            print(slot_e)
        else:
            print("Galerin yok")

    elif x == "buy":
        if not galeri_var:
            print("Galerin yok")
            continue

        if slotlar_dolu_mu():
            print("Tüm slotlar dolu")
            continue

        print(f"Paran: {para}")
        print(f"{car1} | Aliş: {car1_buy} | Kod: {car1_no}")
        print(f"{car2} | Aliş: {car2_buy} | Kod: {car2_no}")

        try:
            kod = int(input("Ürün kodu: "))
        except:
            print("Hatali giriş")
            continue

        if kod == car1_no:
            urun = car1
            fiyat = car1_buy
        elif kod == car2_no:
            urun = car2
            fiyat = car2_buy
        else:
            print("Ürün yok")
            continue

        if para < fiyat:
            print("Yetersiz bakiye")
            continue

        slot = input("Slot (1-5): ")

        if slot == "1" and slot_a == "bos":
            slot_a = urun
        elif slot == "2" and slot_b == "bos":
            slot_b = urun
        elif slot == "3" and slot_c == "bos":
            slot_c = urun
        elif slot == "4" and slot_d == "bos":
            slot_d = urun
        elif slot == "5" and slot_e == "bos":
            slot_e = urun
        else:
            print("Slot dolu")
            continue

        para -= fiyat
        print("Satin alindi")

    elif x == "sell":
        if not galeri_var:
            print("Galerin yok")
            continue

        slot = input("Slot (1-5): ")

        def sat(urun):
            global para
            if urun == car1:
                para += car1_sell
            elif urun == car2:
                para += car2_sell

        if slot == "1" and slot_a != "bos":
            sat(slot_a)
            slot_a = "bos"
        elif slot == "2" and slot_b != "bos":
            sat(slot_b)
            slot_b = "bos"
        elif slot == "3" and slot_c != "bos":
            sat(slot_c)
            slot_c = "bos"
        elif slot == "4" and slot_d != "bos":
            sat(slot_d)
            slot_d = "bos"
        elif slot == "5" and slot_e != "bos":
            sat(slot_e)
            slot_e = "bos"
        else:
            print("Slot boş")
            continue

        print("Araç satildi")

    elif x == "money":
        print(f"Paran: {para}")

    elif x == "exit":
        print("Çikiliyor...")
        time.sleep(1)
        break

    else:
        print("Geçersiz komut")
