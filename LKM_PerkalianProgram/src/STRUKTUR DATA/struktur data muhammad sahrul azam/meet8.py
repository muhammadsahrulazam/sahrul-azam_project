# perbandingan lanjutan

# +++++3-------9+++++
masukanuser = float(input("Masukkan bilangan (kurang dari 3 atau lebih dari 9): "))

# ----- cekk kurang dari 3
kurDar = (masukanuser < 3)
print ("kurang dari 3 =", kurDar)

# ------ cek lebih dari 9
lebDar = (masukanuser > 9)
print ("lebih dari 9 =", lebDar)

betul = kurDar or lebDar
print ("pengecekan final :",betul)

# 4 14
# +++++4-------14+++++
masukanuser = float(input("Masukkan bilangan (kurang dari 4 atau lebih dari 14): "))

# ----- cekk kurang dari 4
kurDar = (masukanuser < 4)
print ("kurang dari 4 =", kurDar)

# ------ cek lebih dari 14
lebDar = (masukanuser > 14)
print ("lebih dari 14 =", lebDar)

betul = kurDar or lebDar
print ("pengecekan final :",betul)