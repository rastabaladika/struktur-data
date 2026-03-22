import matplotlib.pyplot as plt

nilai = []

for i in range(10):
    n = int(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
    nilai.append(n)

print("\nData nilai mahasiswa:", nilai)


nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)

print("Nilai tertinggi:", nilai_tertinggi)
print("Nilai terendah:", nilai_terendah)


rata_rata = sum(nilai) / len(nilai)
print("Rata-rata nilai:", rata_rata)


lulus = 0
for n in nilai:
    if n >= 60:
        lulus += 1

tidak_lulus = len(nilai) - lulus

print("Jumlah mahasiswa lulus:", lulus)
print("Jumlah mahasiswa tidak lulus:", tidak_lulus)


label = ["Tertinggi", "Terendah"]
data = [nilai_tertinggi, nilai_terendah]

plt.figure()
plt.bar(label, data)
plt.title("Grafik Nilai Tertinggi dan Terendah")
plt.ylabel("Nilai")
plt.show()

