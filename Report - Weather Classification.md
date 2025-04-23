# Laporan Proyek Machine Learning Terapan - Zid Irsyadin Sartono Wijaogy

## Domain Proyek

### Latar Belakang

**Kualitas udara** adalah salah satu indikator penting yang mempengaruhi kesehatan masyarakat, lingkungan, dan kualitas hidup secara keseluruhan. Di banyak kota besar, termasuk Jakarta, polusi udara menjadi masalah yang semakin meningkat. Salah satu cara untuk mengukur kualitas udara adalah dengan menggunakan **Air Quality Index (AQI)**, yang memberikan gambaran tentang seberapa bersih atau tercemarnya udara di suatu daerah.

Jakarta, sebagai ibu kota Indonesia, mengalami masalah polusi udara yang signifikan. Kota ini memiliki tingkat polusi yang sangat tinggi, yang dapat berdampak pada kesehatan masyarakat. Menurut laporan dari **Jakarta Rendah Emisi**, kualitas udara di Jakarta telah memburuk dalam beberapa tahun terakhir, sebagian besar disebabkan oleh **kendaraan bermotor**, **industri**, dan **aktivitas pembakaran lahan** yang menyebabkan peningkatan polutan seperti **PM10**, **PM2.5**, **NO2**, **SO2**, dan **CO**. Seperti contoh hasil dari platform Jakarta Rendah Emisi:
![Sumber Polusi](image.png)
[Image Source](https://rendahemisi.jakarta.go.id/assets/content/20211112163532_ind.jpg)

Dalam konteks ini, **Air Quality Index (AQI)** menjadi alat yang penting untuk memantau kualitas udara di Jakarta secara real-time. AQI membantu masyarakat memahami seberapa baik atau buruk kualitas udara yang mereka hirup dan dapat menjadi panduan untuk tindakan preventif, seperti menghindari kegiatan di luar ruangan ketika polusi udara berada pada tingkat yang berbahaya.

### Mengapa Masalah Ini Harus Diselesaikan?

Masalah kualitas udara di Jakarta perlu segera diselesaikan karena dampaknya yang luas terhadap kesehatan masyarakat dan kualitas hidup secara keseluruhan. Berdasarkan laporan dari **World Health Organization (WHO)**, **Polusi udara** adalah keberadaan satu atau lebih kontaminan di atmosfer, seperti debu, asap, gas, kabut, bau, dan uap, dalam jumlah dan durasi yang dapat membahayakan kesehatan manusia. Polusi udara sering kali terjadi akibat aktivitas manusia, seperti pembakaran bahan bakar fosil, industri, serta kendaraan bermotor. 

Paparan terhadap polusi udara dapat terjadi melalui saluran pernapasan. Ketika kita menghirup polutan ini, hal tersebut dapat menyebabkan peradangan, stres oksidatif, imunosupresi, dan mutagenesis pada sel-sel tubuh kita. Efek ini berpengaruh pada organ-organ vital seperti paru-paru, jantung, otak, dan organ lainnya, yang akhirnya dapat menyebabkan berbagai penyakit.

#### Organ Apa Saja yang Terpengaruh oleh Polusi Udara?

Polusi udara dapat mempengaruhi hampir semua organ dalam tubuh. Beberapa polutan udara yang berukuran sangat kecil dapat menembus aliran darah melalui paru-paru dan menyebar ke seluruh tubuh, menyebabkan peradangan sistemik dan bahkan meningkatkan risiko kanker. Organ-organ yang paling terpengaruh oleh polusi udara termasuk:

- **Paru-paru**: Polusi udara dapat menyebabkan penyakit pernapasan seperti asma, bronkitis kronis, dan penyakit paru obstruktif kronik (PPOK).
- **Jantung**: Paparan jangka panjang terhadap polusi udara dapat menyebabkan peningkatan risiko penyakit jantung koroner dan stroke.
- **Otak**: Polusi udara juga dapat mempengaruhi fungsi otak, dengan bukti yang menunjukkan hubungan dengan penurunan kognitif dan gangguan neurologis.
- **Sistem reproduksi**: Beberapa penelitian juga menunjukkan bahwa polusi udara dapat berisiko terhadap kesehatan reproduksi, termasuk meningkatkan risiko kelahiran prematur dan berat badan lahir rendah.

#### Penyakit Apa Saja yang Terkait dengan Paparan Polusi Udara?

Polusi udara merupakan faktor risiko utama untuk **kematian dini** serta berbagai penyakit. Beberapa penyakit yang secara kuat terkait dengan paparan polusi udara meliputi:

1. **Stroke**  
2. **Penyakit jantung iskemik**  
3. **Penyakit paru obstruktif kronik (PPOK)**  
4. **Kanker paru-paru**  
5. **Pneumonia**  
6. **Katarak** (khusus untuk polusi udara dalam rumah)

Selain itu, ada bukti yang menunjukkan hubungan polusi udara dengan peningkatan risiko **hasil kehamilan yang buruk**, seperti **berat badan lahir rendah** dan **kecil untuk usia kehamilan**, serta **penyakit diabetes**, **gangguan kognitif**, dan **penyakit neurologis**.

### Relevansi Proyek

Proyek ini bertujuan untuk membangun sistem yang dapat memprediksi dan mengklasifikasikan tingkat polusi udara di Jakarta menggunakan data **Air Quality Index (AQI)** yang mencakup berbagai polutan. Dengan menggunakan data dari berbagai stasiun pemantauan AQI di Jakarta, proyek ini bertujuan untuk memberikan informasi yang lebih cepat dan lebih akurat mengenai kondisi kualitas udara di Jakarta, yang pada gilirannya dapat membantu dalam pengambilan keputusan berbasis data untuk kebijakan lingkungan dan kesehatan masyarakat.

### Referensi

- [INDEKS STANDAR PENCEMAR UDARA (ISPU) SEBAGAI INFORMASI MUTU UDARA AMBIEN DI INDONESIA](https://ditppu.menlhk.go.id/portal/read/indeks-standar-pencemar-udara-ispu-sebagai-informasi-mutu-udara-ambien-di-indonesia)
- [Mencari Sumber Polusi di Udara melalui Source Apportionment](https://rendahemisi.jakarta.go.id/article/37/mencari-sumber-polusi-di-udara-melalui-source-apportionment)
- [Air Pollution - WHO](https://www.who.int/health-topics/air-pollution#tab=tab_1)


## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pernyataan Masalah 1
- Pernyataan Masalah 2
- Pernyataan Masalah n

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution statement. Misalnya, menggunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan atau melakukan improvement pada baseline model dengan hyperparameter tuning.
    - Solusi yang diberikan harus dapat terukur dengan metrik evaluasi.

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai data yang Anda gunakan dalam proyek. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

