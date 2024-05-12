import time

while True:
    print("""

    [1] Toplama
    [2] Çıkarma
    [3] Çarpma
    [4] Bölme
    [5] Üs Alma
    [6] Mod Alma
    [Y] Çıkış
    """)

    try:
        sec = input("Yapmak İstediğiniz İşlemi Seçiniz: ")
        sayi1 = int(input("Sayı Giriniz: "))
        sayi2 = int(input("Sayı Giriniz: "))

        if sec == '1':
            sonuc = sayi1 + sayi2
        elif sec == '2':
            sonuc = sayi1 - sayi2
        elif sec == '3':
            sonuc = sayi1 * sayi2
        elif sec == '4':
            sonuc = sayi1 / sayi2
        elif sec == '5':
            sonuc = sayi1 ** sayi2
        elif sec == '6':
            sonuc = sayi1 % sayi2
        else:
            print("Hatalı Giriş!")

        print(f"{sayi1} ve {sayi2}'nin sonucu {sonuc}")

        cikis = input("Çıkış Yapmak İstermisiniz(Y/N):").upper()
        if cikis == 'Y':
            print("Çıkış Yapılıyor!")
            exit()
        elif cikis == "N":
            print("Devam Ediliyor")


    except NameError:
        print("Sadece 1 İla 6 arası rakam girebilirsiniz, 3 Saniye Sonra Tekrar Deneyiniz!")
        time.sleep(3)


    except ValueError:
        print("Lütfen sadece sayı yazınız!")
        time.sleep(6)
