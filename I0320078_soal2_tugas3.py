print("++++++++++++++++++++++++++++++++++++++++++")
print("==== Identitas Diri dengan Dictionary ====")
print("++++++++++++++++++++++++++++++++++++++++++")

#Pembuatan dictionary
identitasku = {"Nama" :"Pravanasta Rian Setiawan",
			"Hobi 1":"Berenang", "Hobi 2":"Membaca", "Hobi 3":"Coding",
			"Sosmed 1":"instagram: @pravanasta125", "Sosmed 2":"twitter: @Wong_sepelee", "Sosmed 3":"Whatsapp: 082264373272",
			"Lagu favorit 1":"A Whole New World", "Lagu Favorit 2":"Alone", "Lagu favorit 3":"Balonku",
			"Makanan favorit 1":"Indomie", "Makanan favorit 2":"Soto", "Makanan favorit 3":"Kaliyo"}

#Print Identitas
print(identitasku)

# Mengubah Isi Hobi
identitasku["Hobi 1"] = "Tidur"

# Mengubah Isi Sosmed
identitasku["Sosmed 3"] = "Line: pravanasta21"

# Menghapus Makanan Favorit
del identitasku["Makanan favorit 1"]
del identitasku["Makanan favorit 2"]

# Menambah Hobi
identitasku["Hobi 4"] = "Belajar"

# Menampilkan Output Baru
print("Hasil identitas setelah diubah")
print(identitasku)

print("++++++++++++++++++++++++++++++++++++++++++")
print("===============  Selesai  ================")
print("++++++++++++++++++++++++++++++++++++++++++")