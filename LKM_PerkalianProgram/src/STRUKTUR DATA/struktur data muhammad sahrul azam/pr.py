# ---------5+++++++9-------12+++++++30------- 
# Meminta input dari pengguna
masukanuser = float(input("Masukkan bilangan: "))

# Memeriksa apakah bilangan kurang dari 5
kurDar5 = (masukanuser < 5)
print("kurang dari 5 =", kurDar5)

# Memeriksa apakah bilangan antara 5 dan 9 (inklusif)
antara5dan9 = (5 <= masukanuser <= 9)
print("antara 5 dan 9 (inklusif) =", antara5dan9)

# Memeriksa apakah bilangan antara 9 dan 12 (eksklusif)
antara9dan12 = (9 < masukanuser < 12)
print("antara 9 dan 12 (eksklusif) =", antara9dan12)

# Memeriksa apakah bilangan antara 12 dan 30 (inklusif)
antara12dan30 = (12 <= masukanuser <= 30)
print("antara 12 dan 30 (inklusif) =", antara12dan30)

# Memeriksa apakah bilangan lebih dari 30
lebDar30 = (masukanuser > 30)
print("lebih dari 30 =", lebDar30)

# Final check: apakah bilangan sesuai dengan salah satu kondisi yang diinginkan
betul = kurDar5 or antara5dan9 or antara9dan12 or antara12dan30 or lebDar30
print("pengecekan final =", betul)
