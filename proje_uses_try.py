from kütüphane import *
print("""
****************************************
KÜTÜPHANE PROGRAMINA HOŞGELDİNİZ. 
YAPILABİLECEK İŞLEMLER :
1-) KİTAPLARI GÖSTER
2-) KİTAP ARA
3-) KİTAP EKLE
4-) KİTAP SİL
5-) BASKI YÜKSELT
Q-)ÇIKMAK İÇİN Q YADA q TUŞUNA BASINIZ.
****************************************

""")
kütüphane=Kütüphane()
while True:
    print("""YAPILABİLECEK İŞLEMLER :
1-) KİTAPLARI GÖSTER
2-) KİTAP ARA
3-) KİTAP EKLE
4-) KİTAP SİL
5-) BASKI YÜKSELT
Q-)ÇIKMAK İÇİN Q YADA q TUŞUNA BASINIZ.""")
    islem=input("yapmak istedğiniz işlemi tuşlayınız : ")
    if(islem=="q" or islem=="Q"):
        print("programdan çıkış gerçekleştiriliyor")
        print("yine bekleriz.....")
        break
    elif(islem=="1"):
        print("seçilen işlem kitapların gösterilmesidir.")
        kütüphane.kitapları_goster()
    elif(islem=="2"):
        print("aramak istediğiniz kitabın ismini küçük harflerle yazınız.")
        ara=input("kitap adı : ")
        print("kitap aranıyor")
        time.sleep(2)
        kütüphane.kitap_sorgula(ara)
    elif(islem=="3"):
        print("lütfen sisteme eklemek istediğiniz kitabın bilgilerini aşağıda belirtilen sıraya göre yazınız.")
        print("isim\nyazar\nyayınevi\ntür\nbaskı\ntarih")
        print("tarih kitabı sisteme kayıt ettiğiniz yada bitirdiğiniz yıl olarak ifade edilmelidir.")
        print("lütfen baskıyı yalnız sayı olarak ifade ediniz.")
        isim=input("isim : ")
        yazar=input("yazar : ")
        yayınevi=input("yayınevi : ")
        tür=input("tür : ")
        baskı=int(input("baskı : "))
        tarih=int(input("tarih : "))
        yeni_kitap=Kitap(isim,yazar,yayınevi,tür,baskı,tarih)
        print("kitabınız ekleniyor...")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("kitap başarı ile eklendi")
    elif(islem =="4"):
        print("lütfen kitap ismini küçük harflerler yazınız.")
        isim=input("silmek istediğin kitabın ismi : ")
        cevap=input("ARE U SURE (Y/N),(E/N),(y/n),(e/h) : ")
        if(cevap=="y" or cevap=="Y" or cevap=="E" or cevap=="e"):
            print("kitap silme işlemi gerçekleşiyor")
            print("lütfen bekleyiniz....")
            time.sleep(10)
            print("işleminiz devam etmekte lütfen sisteminiz başından ayrılmayınız.")
            print("...........>>>>>>>>>>>>>>>............>>>>>>>>>>>>>")
            time.sleep(1)
            print(">>>>>>>>>>>>>>>............>>>>>>>>>>>>>...........")
            kütüphane.kitap_sil(isim)
            print("istediğiniz kitap veri tabanından temizleniştir.")
    elif(islem=="5"):
        print("baskısını yükseltmek istediğiniz kitabın ismini küçük harkler ile giriniz.")
        isim=input("kitap adı : ")
        time.sleep(5.8)
        kütüphane.kitap_sil(isim)
        print("baskı yükseltildi.")
    else:
        print("geçersiz işlem girişi yaptınız.")
        print("lütfen sistemi yeniden başlatın")
