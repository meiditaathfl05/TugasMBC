def tarifParkir(waktuParkir):
    tarifParkir = 5000
    masuk = input ("Waktu Masuk Parkir")
    keluar = input ("Waktu Keluar Parkir")
    durasi = keluar - masuk
    bayar 
               
    print ("====Tarif Parkir====")
    print("Waktu Masuk : ", masuk)
    print ("Waktu Masuk ", keluar)
    if keluar > masuk and keluar - masuk > 2:
        durasi = keluar-2-masuk 
        bayar = tarifParkir + (2000*durasi)
    elif keluar < masuk  and keluar - masuk < 2:
        bayar = 5000
    else :
        durasi = 24 - masuk - 2 - keluar
        bayar = 5000 + (2000*durasi)
    print ("Biaya Parkir : Rp ", bayar)
