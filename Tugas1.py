def tarifParkir():
    masuk = float(input ("Waktu Masuk Parkir : "))
    keluar = float(input ("Waktu Keluar Parkir : "))
    durasi = keluar - masuk
    bayar = float
               
    print ("====Tarif Parkir====")
    print("Waktu Masuk : ", masuk)
    print ("Waktu Keluar ", keluar)
    if keluar > masuk and keluar - masuk > 2:
        durasi = keluar - 2 - masuk 
        bayar = 5000 + (2000*durasi)
    else :
        keluar < masuk and keluar - masuk < 2
        bayar = 5000

    print ("Biaya Parkir : Rp ", bayar)
tarifParkir()