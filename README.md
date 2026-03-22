# 1. Penjelasan Konsep Array Menghitung Nilai 10 Mahasiswa

  Pada praktik program pengolahan nilai mahasiswa di atas, konsep array diterapkan menggunakan list Python untuk menyimpan 10 nilai mahasiswa dalam satu variabel bernama nilai. Setiap nilai yang diinput pengguna dimasukkan ke dalam array menggunakan perulangan, sehingga data tersimpan secara terstruktur dan berurutan. Dengan adanya array ini, program dapat dengan mudah melakukan berbagai operasi seperti mencari nilai tertinggi dan terendah menggunakan fungsi max() dan min(), menghitung rata-rata dengan menjumlahkan seluruh elemen lalu membaginya dengan jumlah data, serta menentukan jumlah mahasiswa yang lulus berdasarkan kondisi tertentu (nilai ≥ 60) melalui iterasi. Selain itu, array juga memudahkan dalam pengolahan data secara keseluruhan tanpa harus menggunakan banyak variabel terpisah, sehingga program menjadi lebih efisien, sederhana, dan mudah dikembangkan

# 2. Screenshots Hasil Eksekusi
<img width="779" height="945" alt="Screenshot 2026-03-22 164851" src="https://github.com/user-attachments/assets/92c875db-3c19-451a-b175-ccda17ca51b1" />

# 3. Analisis Kompleksitas
1. Input nilai mahasiswa sebanyak 10 kali seperti,
    for i in range(10):
    nilai.append(n)
2. Mencari Nilai Tertinggi dan Terendah,
   max(nilai) = tertinggi
   min(nilai) =  terendah
3. menghitung rata rata dengan menjumlahkan nilai lalu dibagi dengan jumlah mahasiswa,
   sum(nilai) / len(nilai)
4. menghitung jumlah lulus,
   for n in nilai:
    if n >= 60:
        lulus += 1
5. Menampilkan grafik batang,
   plt.bar

# 4. Refleksi Pembelajaran
Melalui praktik pembuatan program pengolahan nilai mahasiswa menggunakan array (list) di Python, saya memperoleh pemahaman yang lebih mendalam tentang bagaimana struktur data array dapat digunakan untuk menyimpan dan mengelola banyak data secara efisien dalam satu variabel, sehingga program menjadi lebih ringkas dan mudah dikelola dibandingkan menggunakan variabel terpisah. Saya juga memahami peran indeks dalam mengakses data serta pentingnya perulangan untuk memproses setiap elemen secara sistematis. Selain itu, saya belajar mengimplementasikan operasi dasar seperti mencari nilai maksimum dan minimum, menghitung rata-rata, serta menentukan jumlah mahasiswa yang lulus menggunakan percabangan, yang membantu saya memahami penerapan logika pemrograman dalam kasus nyata. Saya juga menyadari bahwa sebagian besar proses memiliki kompleksitas waktu O(n), sehingga efisiensi program bergantung pada jumlah data yang diolah. Dalam praktik ini, saya mendapatkan pengalaman dalam menyajikan hasil baik dalam bentuk grafik maupun teks, termasuk mengubah grafik menjadi persentase yang tetap informatif, sehingga menambah pemahaman saya tentang fleksibilitas penyajian output. Secara keseluruhan, praktik ini meningkatkan kemampuan teknis saya dalam Python, melatih pola pikir logis dan sistematis, serta mendorong saya untuk mengembangkan program lebih lanjut dengan fitur yang lebih kompleks di masa depan.
