import calendar
import time

print("-----SELAMAT DATANG DI APLIKASI KALENDER DAN WAKTU-----")
print("1. Lihat Waktu Sekarang")
print("2. Lihat Kalender Berdasarkan Bulan")
print("3. Lihat Kalender 1 Tahun")
pilih=input("Silahkan masukkan no pilihan:")

if pilih =="1":
    localtime = time.localtime(time.time())
    print ("Waktu lokal saat ini :", localtime)
elif pilih == "2":
    kbulanini = int(input("Masukkan bulan[angka] :"))
    ktahunini = int(input("Masukkan tahun[angka] :"))
    cal = calendar.month(ktahunini,kbulanini)
    print ("Dibawah ini adalah kalender:", cal)
elif pilih == "3":
    jtahun = int(input("Masukkan tahun [angka] :"))
    call = calendar.calendar(jtahun,w=2,l=1,c=6)
    print ("Dibawah ini adalah kalender pertahun:", call)
else:
    print ("Fitur belum tersedia")