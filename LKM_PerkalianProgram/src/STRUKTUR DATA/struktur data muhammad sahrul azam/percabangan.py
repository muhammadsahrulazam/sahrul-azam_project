# Contoh percabangan menggunakan if, elif, else

# Mendapatkan input dari pengguna
nilai = float(input("Masukkan nilai Anda: "))

# Memeriksa kondisi nilai
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

# Menampilkan hasil
print(f"Nilai Anda {nilai} mendapat grade {grade}")