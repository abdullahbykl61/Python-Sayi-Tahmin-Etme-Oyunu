import random
number=random.randint(1,100)
sayac=0
tahminsayı=int(input("Kaç hakta bilebilirsin.\n"))
hak=tahminsayı
while hak>0:
    hak=hak-1
    tahmin=int(input("Tahmini giriniz.\n"))
    if(tahmin>number):
        print("Aşağı inin.\n")
        sayac=sayac+1
    elif(tahmin<number):
        print("Yukarı çıkın.\n")
        sayac=sayac+1
    else:
        print("Doğru tahmin.\n")
        sonuc=100-(sayac*(100/tahminsayı))
        print(f"Puanın: {sonuc}")
        break
    if hak==0:
        print("Hakkınız bitti.\n")        



