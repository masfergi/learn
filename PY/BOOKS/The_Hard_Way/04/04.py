mobil = 100
mobil_di_angkasa = 4.0
pengendara = 30
penumpang = 90
mobil_tidak_ditumpangi = mobil - mobil_di_angkasa
mobil_ditumpangi = pengendara
kepadatan_mobil = mobil_ditumpangi * mobil_di_angkasa
penumpang_rata_rata = penumpang / mobil_ditumpangi

print("ada", mobil, "mobil tersedia.")
print("Hanya ada", pengendara, "pengendara tersedia")
print("Akan ada", mobil_tidak_ditumpangi, "mobil kosong hari ini")
print("Kita dapat mengantarkan", kepadatan_mobil, "orang hari ini")
print("Kita punya", penumpang, "penumpang")
print("kita butuh", penumpang_rata_rata, "penumpang di tiap mobil")