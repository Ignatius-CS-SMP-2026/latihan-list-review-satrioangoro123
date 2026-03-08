# NAMA  : Satrio Angoro
# KELAS : 9A
# ---------------------------------------------------------
# LATIHAN: REVIEW LIST PYTHON
#Diberikan sebuah data acak nilai ujian siswa. Buatlah program yang mengurutkan data tersebut 
#dari nilai tertinggi ke terendah. Kemudian, pisahkan 3 nilai tertinggi sebagai penerima beasiswa, 
#dan hapus nilai terendah (nilai di bawah 60) karena dianggap tidak lulus. 
#Gunakan data awal berikut: nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
# ---------------------------------------------------------

# OUTPUT
#Data nilai asli: [75, 55, 90, 85, 45, 95, 80] 
#Data setelah diurutkan (Descending): [95, 90, 85, 80, 75, 55, 45] 
#Tiga nilai tertinggi (Penerima Beasiswa): [95, 90, 85] 
#Daftar nilai yang lulus: [95, 90, 85, 80, 75]
# ---------------------------------------------------------

# Tulis kodemu di bawah ini:
print("/n===Nilai Ujian Siswa===")
nilai = [75, 55, 90, 85, 45, 95, 80]

print("Data nilai asli :", nilai)
nilai.sort(reverse=True)
print("Data setelah diurutkan:", nilai)
data = [:3]
print("Tiga nilai tertinggi (penerima beasiswa):", data)
nilai_user = []
for n in nilai:
    if n >= 60:
        nilai_user.append(n)

print("Daftar nilai yang lulus:", nilai_user)
