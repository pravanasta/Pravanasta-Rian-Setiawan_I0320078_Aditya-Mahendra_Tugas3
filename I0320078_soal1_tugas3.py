print("++++++++++++++++++++++++++++++++++++++++++")
print("=======  Program List Nama Teman  ========")
print("++++++++++++++++++++++++++++++++++++++++++")

# Menampilkan list 10 teman
list_teman = ['Hana', 'Hilmy', 'Harry', 'Narista', 'Vika', 'Rafli', 'Vian', 'Ojat', 'Hani', 'Alam']

# menampilkan list indeks nomor 4, 6, dan 7
print("List teman pada indeks keempat: ",list_teman[4])
print("List teman pada indeks keenam: ",list_teman[6])
print("List teman pada indeks ketujuh: ",list_teman[7])

# Mengganti nama teman di list nomor 3, 5, dan 9
list_teman[3] = 'Agus'
list_teman[5] = 'Ahnaf'
list_teman[9] = 'Nauval'

# Menambah 2 teman
list_teman.append('Ano')
list_teman.append('Rengga')

# Menampilkan semua teman dengan pengulangan
for friend in list_teman:
    print(friend, "adalah temanku")

# Menampilkan panjang list
panjang_list_teman = len(list_teman)
print("Jumlah teman saya: ",panjang_list_teman )

print("++++++++++++++++++++++++++++++++++++++++++")
print("===============  Selesai  ================")
print("++++++++++++++++++++++++++++++++++++++++++")