# Meminta pengguna memasukkan bilangan
masukanuser = float(input("Masukkan bilangan (kurang dari 5, antara 9-12, atau lebih dari 30): "))

# Cek kurang dari 5
kurDar5 = (masukanuser < 5)
print("kurang dari 5 =", kurDar5)

# Cek antara 9 dan 12 (inklusif)
ant9_12 = (9 <= masukanuser <= 12)
print("antara 9 dan 12 =", ant9_12)

# Cek lebih dari 30
lebDar30 = (masukanuser > 30)
print("lebih dari 30 =", lebDar30)

# Pengecekan final apakah di luar interval 5-9 atau di dalam interval 9-12 atau lebih dari 30
betul = kurDar5 or ant9_12 or lebDar30
print("pengecekan final =", betul)
