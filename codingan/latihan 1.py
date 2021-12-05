a = {'Bayu': 628763737637, 'Amel': 6283635656}
print("# Kontak Awal")
print("------------------------------")
print("     Nama    |  Nomor Telpon  ")
print("------------------------------")
print("     Bayu     |  628763737637", "\n     Amel    |  6283635656")
print("------------------------------")

# Menampilkan kontak Bayu
print("\n# Menampilkan Kontak Bayu")
print("------------------------------")
print("     Nama    |  Nomor Telpon  ")
print("------------------------------")
print("     Bayu     |  ", a['Bayu'])
print("------------------------------")

# Menambah kontak
print("\n# Menambahkan Kontak Rahmat")
a["Rahmat"] = "62853625652"
print("------------------------------")
print("     Nama    |  Nomor Telpon  ")
print("------------------------------")
print("     Bayu     |  ", a['Bayu'])
print("     Amel    |  ", a['Amel'])
print("     Rahmat    |  ", a['Rahmat'])
print("------------------------------")

# Mengubah kontak Amel
print("\n# Mengubah Kontak Amel")
a['Amel'] = "6283635656"
print("------------------------------")
print("     Nama    |  Nomor Telpon  ")
print("------------------------------")
print("     Bayu     |  ", a['Bayu'])
print("     Amel    |  ", a['Amel'])
print("     Rahmat    |  ", a['Rahmat'])
print("------------------------------")

# Menampilakan semua nama
print("\n# Menampilkan Semua Nama")
print(a.keys())

# Menampilkan semua nomor
print("\n# Menampilkan Semua Nomor")
print(a.values())

# Menampilkan daftar nama dan nomornya
print("\n# Menampilkan Daftar Nama dan Nomornya")
print(a.items())

# Hapus kontak Dina
print("\n# Menghapus Kontak Amel")
del a["Amel"]
print("------------------------------")
print("     Nama    |  Nomor Telpon  ")
print("------------------------------")
print("     Bayu     |  ", a['Bayu'])
print("     Rahmat    |  ", a['Rahmat'])
print("------------------------------")
