# looping baru akan berhenti jika kondisi sudah terpenuhi
# 

#** <=================================================================> **#
#** <=================================================================> **#


# penggunaan kata kunci break
for i in range(10):
    print("selamat datang ke", i)
    if i == 5:
        break # looping akan berhenti jika nilai variable i sama dengan 5


print()


# penggunaan kata kunci continue
for i in range(15):
    i += 1
    
    if i % 2 == 0:
        continue

    print("perulangan angka ganjil", i)


print()

# kombinasi break dan continue
for i in range(10):
    if i == 3:
        print("Iterasi ke-3, lanjutkan ke iterasi berikutnya.")
        continue

    if i == 6:
        print("Iterasi ke-6, hentikan loop.")
        break

    print("Iterasi ke-", i)
