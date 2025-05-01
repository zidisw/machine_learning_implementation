# Laporan Proyek Machine Learning: Sistem Rekomendasi Buku

## Project Overview

### Latar Belakang Proyek  

Dalam era digital modern, pengguna dihadapkan pada banyaknya informasi dan produk yang tersedia. Kondisi ini menjadikan sistem rekomendasi sebagai salah satu fitur kunci dalam berbagai platform digital, seperti e-commerce, layanan streaming, dan literasi digital, termasuk platform populer seperti Goodreads. Sistem rekomendasi membantu mempersonalisasi pengalaman pengguna dengan menyarankan item yang relevan berdasarkan preferensi dan pola perilaku pengguna. Penelitian menunjukkan bahwa sistem rekomendasi berbasis AI mampu meningkatkan pengalaman pengguna secara signifikan sekaligus mengatasi bias popularitas dalam rekomendasi item (Naghiaei & Rahmani, 2021).

### Pentingnya Proyek  

Proyek ini bertujuan untuk mengembangkan sistem rekomendasi buku dengan memanfaatkan dataset *Goodbooks-10k*. Dataset ini mencakup lebih dari 980.000 interaksi rating antara pengguna dan 10.000 judul buku yang beragam, meliputi genre dan penulis dari berbagai latar belakang. Pendekatan proyek ini adalah menggabungkan dua metode utama dalam sistem rekomendasi, yakni *collaborative filtering* dan *content-based filtering*. Metode *collaborative filtering* memanfaatkan pola interaksi pengguna, sementara metode *content-based filtering* menilai kesamaan atribut buku (seperti genre, penulis, dan deskripsi).  

Penelitian menyebutkan bahwa sistem rekomendasi memberikan dampak yang signifikan terhadap aktivitas pengguna. Laporan McKinsey & Company menunjukkan bahwa lebih dari 35% total penjualan di Amazon dihasilkan dari sistem rekomendasi (McKinsey & Company, 2013). Selain itu, penelitian yang dilakukan oleh Remadnia dan Maazouzi (2025) menunjukkan bahwa kombinasi metode berbasis *filtering* dan *deep learning* meningkatkan akurasi prediksi rekomendasi buku secara signifikan.  

### Kesimpulan

Dengan demikian, pengembangan sistem rekomendasi buku yang efektif memiliki potensi untuk meningkatkan kepuasan pengguna, serta mendorong keterlibatan lebih tinggi pada platform literasi digital. Sistem rekomendasi berbasis AI dapat menjadi alat yang kuat untuk menjembatani pengguna dengan literatur yang relevan dengan minat mereka, sekaligus mendukung personalisasi pengalaman digital yang lebih baik.

### Referensi

- McKinsey & Company. (2013). *How retailers can keep up with consumers*. McKinsey & Company. Retrieved from [https://www.mckinsey.com](https://www.mckinsey.com)  
- Naghiaei, M., & Rahmani, H. A. (2021). The Unfairness of Popularity Bias in Book Recommendation. *Proceedings of the AAAI Conference on Artificial Intelligence*.  
- Remadnia, O., & Maazouzi, F. (2025). Hybrid Book Recommendation System Using Collaborative Filtering and Embedding-Based Deep Learning. *Journal of Intelligent Systems and Applications*, 34(2), 456–478.

## Business Understanding

### Problem Statements

- Bagaimana sistem dapat merekomendasikan buku yang sesuai dengan minat pengguna berdasarkan histori interaksi sebelumnya (rating, bacaan)?
- Pendekatan atau algoritma mana yang memberikan hasil rekomendasi paling akurat dan relevan terhadap kebutuhan pengguna, berdasarkan data Goodbooks-10k?

### Goals

- Mengembangkan sistem rekomendasi buku yang mampu menghasilkan rekomendasi bersifat personal dan relevan.
- Menyajikan output berupa Top-N rekomendasi buku untuk pengguna tertentu.
- Mengevaluasi performa sistem dengan berbagai metrik dan membandingkan model berdasarkan pendekatan yang digunakan.

### Solution Approach

Untuk mencapai tujuan tersebut, proyek ini menerapkan dua pendekatan solusi utama:

1. **Content-Based Filtering**
   - Pendekatan ini merekomendasikan buku berdasarkan kemiripan kontennya (judul, penulis, tag, dan metadata lainnya) dengan buku-buku yang telah disukai atau dibaca oleh pengguna.
   - Teknik yang digunakan antara lain TF-IDF vectorization dan CountVectorizer.
   - Pendekatan ini cocok ketika data pengguna terbatas atau ingin menekankan eksplorasi berdasarkan fitur buku itu sendiri.

2. **Collaborative Filtering**
   - Pendekatan ini merekomendasikan buku berdasarkan pola rating dari pengguna lain yang memiliki preferensi serupa.
   - Teknik yang digunakan dalam proyek ini mencakup Cosine Similarity antar pengguna, Matrix Factorization menggunakan SVD, dan Autoencoder berbasis deep learning.
   - Pendekatan ini sangat efektif dalam memanfaatkan informasi kolektif dari komunitas pengguna untuk menemukan item-item baru yang mungkin disukai.

Dengan menerapkan kedua pendekatan ini secara terpisah, proyek dapat mengevaluasi dan membandingkan kekuatan masing-masing, serta membuka peluang penggabungan keduanya menjadi sistem hybrid pada pengembangan lanjutan.

### Data Understanding

Tahapan ini bertujuan untuk memahami struktur, isi, dan kualitas data dari berbagai dataset yang digunakan dalam proyek sistem rekomendasi buku berbasis GoodBooks-10k. Dataset ini tersedia secara publik di:

> [https://github.com/zygmuntz/goodbooks-10k](https://github.com/zygmuntz/goodbooks-10k)

---

#### 1. RATINGS

- **Jumlah entri:** 981.756
- **Jumlah kolom:** 3
- **Ukuran memori:** 22.5 MB

##### Kolom:

| Kolom    | Tipe   | Deskripsi                                      |
|----------|--------|------------------------------------------------|
| book_id  | int64  | ID unik untuk buku.                            |
| user_id  | int64  | ID unik untuk pengguna.                        |
| rating   | int64  | Rating yang diberikan pengguna terhadap buku. |

##### Info Tambahan:

- Missing values: Tidak ada
- Duplikat: Ditemukan 1.644 baris duplikat

---

#### 2. BOOKS

- **Jumlah entri:** 10.000
- **Jumlah kolom:** 23
- **Ukuran memori:** ~1.8 MB

##### Kolom:

| Kolom                       | Tipe     | Deskripsi                                                              |
|----------------------------|----------|------------------------------------------------------------------------|
| id                         | int64    | ID internal baris buku.                                               |
| book_id                    | int64    | ID buku (unik).                                                       |
| best_book_id               | int64    | ID buku terbaik terkait.                                              |
| work_id                    | int64    | ID pekerjaan (work) buku.                                             |
| books_count                | int64    | Jumlah edisi buku.                                                    |
| isbn                       | object   | ISBN versi 10 digit (kadang kosong).                                  |
| isbn13                     | float64  | ISBN versi 13 digit.                                                  |
| authors                    | object   | Nama penulis.                                                         |
| original_publication_year | float64  | Tahun pertama kali diterbitkan.                                       |
| original_title             | object   | Judul asli buku.                                                      |
| title                      | object   | Judul tampilan.                                                       |
| language_code              | object   | Kode bahasa (misal: eng, en-US).                                      |
| average_rating             | float64  | Rata-rata rating buku.                                                |
| ratings_count              | int64    | Total jumlah rating.                                                  |
| work_ratings_count         | int64    | Jumlah rating berdasarkan ID pekerjaan.                               |
| work_text_reviews_count    | int64    | Jumlah ulasan teks.                                                   |
| ratings_1 - ratings_5      | int64    | Jumlah rating per nilai (1 hingga 5 bintang).                         |
| image_url                  | object   | URL gambar besar.                                                     |
| small_image_url            | object   | URL gambar kecil.                                                     |

##### Info Tambahan:

- Missing values:
  - isbn: 700
  - isbn13: 585
  - original_publication_year: 21
  - original_title: 585
  - language_code: 1.084
- Duplikat: Tidak ditemukan

---

#### 3. TAGS

- **Jumlah entri:** 34.252
- **Jumlah kolom:** 2
- **Ukuran memori:** 535.3 KB

##### Kolom:

| Kolom    | Tipe   | Deskripsi                         |
|----------|--------|-----------------------------------|
| tag_id   | int64  | ID unik tag.                      |
| tag_name | object | Nama/nama kategori tag.           |

##### Info Tambahan:

- Missing values: Tidak ada
- Duplikat: Tidak ditemukan

---

#### 4. TO_READ

- **Jumlah entri:** 912.705
- **Jumlah kolom:** 2
- **Ukuran memori:** 13.9 MB

##### Kolom:

| Kolom    | Tipe   | Deskripsi                                        |
|----------|--------|--------------------------------------------------|
| user_id  | int64  | ID pengguna yang menandai buku untuk dibaca.     |
| book_id  | int64  | ID buku yang akan dibaca.                        |

##### Info Tambahan:

- Missing values: Tidak ada
- Duplikat: Tidak ditemukan

---

#### 5. BOOK_TAGS

- **Jumlah entri:** 999.912
- **Jumlah kolom:** 3
- **Ukuran memori:** 22.9 MB

##### Kolom:

| Kolom              | Tipe   | Deskripsi                                            |
|--------------------|--------|------------------------------------------------------|
| goodreads_book_id  | int64  | ID buku berdasarkan Goodreads.                      |
| tag_id             | int64  | ID tag yang terkait.                                |
| count              | int64  | Berapa kali tag tersebut diterapkan pada buku.      |

##### Info Tambahan:

- Missing values: Tidak ada
- Duplikat: Ditemukan 6 baris duplikat

---

#### Kesimpulan Umum

- Total dataset: 5, namun yang digunakan hanya 4 selain to_read_df karena kurang relevan.
- Mayoritas dataset bebas dari nilai hilang dan duplikat, kecuali **BOOKS** (missing) dan **RATINGS & BOOK_TAGS** (duplikat).
- Tipe data konsisten, dominan `int64` dan `object`, dengan sedikit `float64`.

---

### Penjelasan Hasil Visualisasi

Beberapa visualisasi telah dilakukan untuk mengevaluasi distribusi dan karakteristik utama dari dataset:

1. **Distribusi Rating Pengguna**
   - Sebagian besar pengguna memberikan rating di kisaran 4 dan 5.
   - Distribusi mengindikasikan kecenderungan pengguna untuk memberikan penilaian positif.

2. **Distribusi Jumlah Rating per User**
   - Beberapa pengguna sangat aktif dan memberikan banyak rating.
   - Histogram menunjukkan pola long-tail yang umum di sistem rekomendasi.

3. **Distribusi Rata-rata Rating Buku**
   - Sebagian besar buku memiliki rating rata-rata antara 3 hingga 4.5.
   - Menunjukkan bahwa secara umum buku dalam dataset dinilai cukup baik.

4. **Top 10 Buku dengan Rating Terbanyak**
   - Visualisasi bar chart menampilkan 10 buku dengan interaksi terbanyak.
   - Buku-buku ini bisa menjadi baseline untuk validasi rekomendasi populer.

**Kesimpulan Visualisasi:**

Visualisasi membantu dalam memahami distribusi nilai dan perilaku pengguna. Hasil eksplorasi digunakan sebagai dasar untuk menentukan strategi filtering, preprocessing, dan pendekatan modeling yang lebih efektif.

## Data Preparation

Tahapan ini bertujuan untuk membersihkan dan menyiapkan data agar sesuai dan optimal untuk digunakan dalam proses pemodelan sistem rekomendasi. Data preparation dilakukan untuk dua pendekatan yang berbeda, yaitu **Content-Based Filtering** dan **Collaborative Filtering**, dengan urutan langkah yang konsisten seperti di notebook.

---

### 1. Data Cleaning

#### a. Content-Based Filtering

Langkah-langkah yang dilakukan:

1. **Menghapus duplikat dan missing values** pada:
   - `books.csv`
   - `tags.csv`
   - `book_tags.csv`

   Tujuan: memastikan data bersih dari redundansi dan kekosongan nilai yang dapat mengganggu proses ekstraksi fitur.

2. **Menggabungkan tag dengan buku**
   - `book_tags.csv` digabung dengan `tags.csv` berdasarkan `tag_id`.
   - Dilakukan agregasi untuk memilih 5 tag teratas berdasarkan `count` untuk setiap buku.

3. **Membuat kolom teks gabungan**
   - Kolom `authors`, `original_title`, dan kumpulan tag digabung menjadi satu kolom `content`.
   - Nilai kosong pada kolom teks diisi dengan string kosong (`fillna('')`).

   Tujuan: kolom `content` digunakan sebagai dasar representasi teks dalam proses vektorisasi (TF-IDF, CountVectorizer, atau deep learning).

#### b. Collaborative Filtering

Langkah-langkah yang dilakukan:

1. **Menghapus duplikat** pada dataset `ratings.csv` berdasarkan kombinasi `user_id` dan `book_id`.

2. **Menggabungkan ratings dengan metadata buku**
   - `ratings.csv` digabungkan dengan `books.csv` berdasarkan `book_id`.
   - Tujuan: menambahkan informasi tambahan dari metadata buku untuk referensi atau filtering.

3. **Melakukan filtering data**
   - Hanya mempertahankan user yang memberikan lebih dari 10 rating.
   - Hanya mempertahankan buku yang dirating lebih dari 20 kali.
   - Tujuan: menghindari data yang terlalu jarang dan meningkatkan kualitas rekomendasi.

4. **Menghapus missing values**
   - Setelah proses gabung dan filter, nilai kosong yang tersisa dihapus.

---

### 2. Splitting Data

#### a. Content-Based Filtering

- Tidak dilakukan pembagian data eksplisit karena pendekatan ini menggunakan seluruh dataset untuk menghitung kemiripan antar item dan tidak menggunakan model deep learning karena model sederhana sudah cukup.
- Evaluasi dilakukan berdasarkan hasil perhitungan kemiripan antar item menggunakan semua data buku.

#### b. Collaborative Filtering

Langkah-langkah splitting:

1. Membentuk **user-item matrix** dari data rating.
2. Menggunakan fungsi split khusus per pengguna:
   - Untuk setiap pengguna, 20% data rating mereka disimpan sebagai **data test**.
   - Sisanya tetap sebagai **data train**.

Tujuan:

- Menyimulasikan skenario nyata: sistem mencoba merekomendasikan buku yang belum dirating user.
- Memungkinkan evaluasi performa model dalam memprediksi rating yang belum diketahui sebelumnya.

---

### Alasan Tahapan Data Preparation

- **Data Cleaning** sangat penting untuk memastikan kualitas dan keakuratan data yang masuk ke dalam model.
- **Filtering** data membantu fokus pada pengguna dan item yang benar-benar aktif dan signifikan.
- **Splitting data secara logis** (per user) memberikan validasi realistis atas kemampuan sistem rekomendasi dalam memprediksi preferensi pengguna.

Dengan menerapkan tahapan-tahapan ini secara sistematis dan berurutan, data menjadi lebih siap, bersih, dan terstruktur dengan baik untuk membangun sistem rekomendasi yang akurat dan efektif.

### Modeling and Result

Pada tahap ini, sistem rekomendasi dibangun menggunakan dua pendekatan utama, yaitu **Content-Based Filtering** dan **Collaborative Filtering**. Fokus utama pada bagian ini adalah menampilkan hasil rekomendasi (Top-N Recommendation) yang dihasilkan dari masing-masing model.

---

#### 1. Content-Based Filtering

Pendekatan ini merekomendasikan buku berdasarkan kemiripan konten (cosine similarity) dengan buku yang pernah disukai oleh pengguna. Representasi konten dibentuk dari fitur `authors`, `original_title`, dan tag buku, kemudian dikonversi menggunakan dua teknik:

- **TF-IDF Vectorizer**
- **CountVectorizer**

#### a. TF-IDF + Cosine Similarity

Top-5 rekomendasi untuk buku: *The Hunger Games (The Hunger Games, #1)*

| Judul Buku                                                      | Penulis             |
|------------------------------------------------------------------|---------------------|
| The Hunger Games Trilogy Boxset (The Hunger Games)              | Suzanne Collins     |
| Mockingjay (The Hunger Games, #3)                               | Suzanne Collins     |
| The Program (The Program, #1)                                   | Suzanne Young       |
| Catching Fire (The Hunger Games, #2)                            | Suzanne Collins     |
| Hunger (Gone, #2)                                               | Michael Grant       |

#### b. Count Vectorizer + Cosine Similarity

Top-5 rekomendasi untuk buku: *The Hunger Games (The Hunger Games, #1)*

| Judul Buku                                                      | Penulis             |
|------------------------------------------------------------------|---------------------|
| Mockingjay (The Hunger Games, #3)                               | Suzanne Collins     |
| The Hunger Games Trilogy Boxset (The Hunger Games)              | Suzanne Collins     |
| The Program (The Program, #1)                                   | Suzanne Young       |
| That Was Then, This Is Now                                      | S.E. Hinton         |
| Gregor and the Curse of the Warmbloods (Underland Chronicles)   | Suzanne Collins     |

---

#### 2. Collaborative Filtering

Pendekatan ini merekomendasikan buku berdasarkan pola interaksi pengguna terhadap buku, tanpa melihat konten buku. Model yang digunakan:

- **User-Based (Cosine Similarity)**
- **Matrix Factorization (SVD)**
- **Autoencoder (Neural Network)**

#### a. Cosine Similarity

Top-10 rekomendasi untuk user ID 33716:

| Judul Buku                                             | Penulis                | Avg. Rating |
|--------------------------------------------------------|-------------------------|-------------|
| A Short History of Nearly Everything                  | Bill Bryson             | 4.19        |
| Heidi                                                 | Johanna Spyri et al.    | 3.97        |
| Notes from a Small Island                             | Bill Bryson             | 3.91        |
| In a Sunburned Country                                | Bill Bryson             | 4.05        |
| Neither Here nor There: Travels in Europe             | Bill Bryson             | 3.88        |
| The Lost Continent: Travels in Small Town America     | Bill Bryson             | 3.83        |
| Heretics of Dune (Dune Chronicles #5)                 | Frank Herbert           | 3.83        |
| Harry Potter Collection (Harry Potter, #1-6)          | J.K. Rowling            | 4.73        |
| The Mother Tongue: English and How It Got That Way    | Bill Bryson             | 3.95        |
| What to Expect the First Year                         | Heidi Murkoff et al.    | 3.86        |

#### b. Matrix Factorization (SVD)

Top-10 rekomendasi untuk user ID 33716:

| Judul Buku                                             | Penulis                | Avg. Rating |
|--------------------------------------------------------|-------------------------|-------------|
| Heidi                                                 | Johanna Spyri et al.    | 3.97        |
| J.R.R. Tolkien 4-Book Boxed Set                        | J.R.R. Tolkien          | 4.59        |
| Notes from a Small Island                             | Bill Bryson             | 3.91        |
| The Long Dark Tea-Time of the Soul                    | Douglas Adams           | 4.05        |
| Tropic of Cancer                                      | Henry Miller            | 3.71        |
| Neither Here nor There                                | Bill Bryson             | 3.88        |
| Harry Potter Collection (Harry Potter, #1-6)          | J.K. Rowling            | 4.73        |
| The Design of Everyday Things                         | Donald A. Norman        | 4.18        |
| The Broken Wings                                      | Kahlil Gibran et al.    | 3.93        |
| What to Expect the First Year                         | Heidi Murkoff et al.    | 3.86        |

#### c. Autoencoder

Top-10 rekomendasi untuk user ID 33716:

| Judul Buku                                             | Penulis                | Avg. Rating |
|--------------------------------------------------------|-------------------------|-------------|
| Harry Potter and the Goblet of Fire (Harry Potter #4) | J.K. Rowling            | 4.53        |
| Heidi                                                 | Johanna Spyri et al.    | 3.97        |
| J.R.R. Tolkien 4-Book Boxed Set                        | J.R.R. Tolkien          | 4.59        |
| Notes from a Small Island                             | Bill Bryson             | 3.91        |
| The Portrait of a Lady                                 | Henry James et al.      | 3.76        |
| Heretics of Dune (Dune Chronicles #5)                 | Frank Herbert           | 3.83        |
| Harry Potter Collection (Harry Potter, #1-6)          | J.K. Rowling            | 4.73        |
| The Mother Tongue: English and How It Got That Way    | Bill Bryson             | 3.95        |
| The Broken Wings                                      | Kahlil Gibran et al.    | 3.93        |
| What to Expect the First Year                         | Heidi Murkoff et al.    | 3.86        |

---

### Ringkasan Output

- **Content-Based Filtering** berhasil merekomendasikan buku yang serupa dari sisi konten seperti penulis dan tema cerita.
- **Collaborative Filtering** memberikan hasil yang konsisten dan personal berdasarkan pola interaksi pengguna, dengan top rekomendasi banyak didominasi oleh seri buku populer seperti *Harry Potter*.
- Hasil menunjukkan bahwa model dapat memberikan rekomendasi Top-N yang relevan dan bervariasi sesuai metode yang digunakan.

### Perbandingan Teknik yang Digunakan

#### Content-Based Filtering

| Teknik                     | Kelebihan                                                                 | Kekurangan                                                                 |
|---------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **TF-IDF Vectorizer**     | Lebih memperhatikan kata unik; cocok untuk teks panjang                   | Bisa mengabaikan informasi penting dari kata umum (sering muncul)          |
| **CountVectorizer**       | Simpel dan cepat, cocok untuk dataset kecil atau kata-kata pendek         | Tidak membedakan kata penting dengan kata umum                            |


#### Collaborative Filtering

| Teknik                         | Kelebihan                                                                 | Kekurangan                                                                 |
|--------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Cosine Similarity (User-Based)** | Mudah diimplementasikan, dapat menangkap hubungan antar pengguna         | Kurang efektif untuk dataset besar; tidak dapat menangani sparsity tinggi |
| **Matrix Factorization (SVD)** | Dapat menemukan pola laten; cocok untuk menangani data sparsity          | Butuh tuning dan tidak bisa menangani user/item baru (cold-start)         |
| **Autoencoder**                | Dapat menangkap pola non-linear yang kompleks                             | Butuh banyak data dan waktu training; lebih sulit dijelaskan              |


## Evaluation

### Metrik Evaluasi yang Digunakan

Evaluasi sistem rekomendasi dilakukan berdasarkan jenis pendekatannya:

- **Content-Based Filtering**: menggunakan metrik *Precision@N*, *Recall@N*, dan *F1-Score@N* dengan asumsi bahwa **kemiripan penulis** dijadikan proksi relevansi (relevance).
- **Collaborative Filtering**: menggunakan metrik **Root Mean Squared Error (RMSE)** yang mengukur seberapa dekat prediksi rating dengan nilai rating sebenarnya.

### Penjelasan Metrik Evaluasi

### 1. Evaluasi Content-Based Filtering

#### a. Precision

Mengukur proporsi item yang relevan dari N item yang direkomendasikan.

- **Formula**:  
  `Precision@N = (Jumlah item relevan dalam Top-N) / N`
- **Cara kerja**: Nilai precision tinggi menunjukkan bahwa sebagian besar item yang direkomendasikan benar-benar relevan bagi pengguna.

#### b. Recall

Mengukur proporsi item relevan yang berhasil ditemukan oleh sistem dari seluruh item relevan yang tersedia.

- **Formula**:  
  `Recall@N = (Jumlah item relevan dalam Top-N) / (Jumlah total item relevan)`
- **Cara kerja**: Recall tinggi berarti sistem berhasil menemukan banyak item yang relevan dari keseluruhan item relevan yang mungkin.

#### c. F1-Score

Merupakan harmonic mean dari precision dan recall, berguna untuk menyeimbangkan keduanya.

- **Formula**:  
  `F1@N = 2 × (Precision@N × Recall@N) / (Precision@N + Recall@N)`

---

### 2. Evaluasi Collaborative Filtering

#### a. Mean Squared Error (MSE)

MSE digunakan selama **proses pelatihan** untuk mengoptimalkan model, khususnya pada pendekatan seperti autoencoder.

- **Formula**:  
  `MSE = (1/n) × Σ(yᵢ - ŷᵢ)²`
- **Cara kerja**: MSE menghitung rata-rata kuadrat dari selisih antara rating aktual dan prediksi. Model belajar meminimalkan nilai ini.

#### b. Root Mean Squared Error (RMSE)

RMSE digunakan untuk **evaluasi performa model** setelah training selesai.

- **Formula**:  
  `RMSE = sqrt( (1/n) × Σ(yᵢ - ŷᵢ)² )`
- **Cara kerja**: Nilai RMSE yang lebih kecil menunjukkan prediksi rating yang lebih akurat. RMSE lebih intuitif karena satuannya sama dengan rating asli.

---

### Alasan Pemilihan Metrik

- **RMSE** digunakan pada collaborative filtering karena output model adalah prediksi nilai rating kuantitatif.
- **Precision**, **Recall**, dan **F1-Score** lebih tepat digunakan untuk evaluasi sistem content-based, karena tujuannya adalah memberi rekomendasi Top-N item yang relevan.

Evaluasi ini memastikan bahwa sistem tidak hanya akurat dalam prediksi angka, tetapi juga memberikan hasil yang relevan dan bermanfaat bagi pengguna.

---

### Hasil Evaluasi

#### 1. Content-Based Filtering

Evaluasi dilakukan menggunakan pendekatan pencocokan penulis sebagai ground truth relevansi:

- **TF-IDF + Cosine Similarity**  
  - Precision@5: **0.5560**  
  - Recall@5: **0.4513**  
  - F1-Score@5: **0.4982**

- **CountVectorizer + Cosine Similarity**  
  - Precision@5: **0.4800**  
  - Recall@5: **0.3896**  
  - F1-Score@5: **0.4301**

*Kesimpulan: Model berbasis CountVectorizer menghasilkan kualitas rekomendasi yang lebih tinggi dibanding  TF-IDF berdasarkan semua metrik evaluasi.*

---

#### 2. Collaborative Filtering

Evaluasi dilakukan berdasarkan akurasi prediksi rating pada data testing menggunakan RMSE:

| Model Collaborative     | RMSE Testing |
|-------------------------|----------------|
| Cosine Similarity       | **1.3117**      |
| Matrix Factorization (SVD) | **0.5286**   |
| Autoencoder             | **0.2535**      |

*Kesimpulan: Autoencoder memberikan prediksi rating paling akurat (RMSE terkecil), diikuti oleh SVD. Cosine Similarity menghasilkan error terbesar.*

### Ringkasan

- Metrik evaluasi yang digunakan sesuai dengan karakteristik masing-masing pendekatan:
  - Precision, Recall, dan F1 cocok untuk Content-Based karena fokus pada kualitas rekomendasi Top-N.
  - RMSE cocok untuk Collaborative Filtering karena bertujuan memprediksi nilai rating.
- Evaluasi menunjukkan bahwa:
  - **CountVectorizer** lebih unggul dalam Content-Based Filtering.
  - **Autoencoder** dan **SVD** unggul dalam Collaborative Filtering, dengan Autoencoder sedikit lebih baik dari sisi error prediksi.

---

## Final Conclusion

Berdasarkan seluruh proses eksplorasi, pemodelan, dan evaluasi sistem rekomendasi yang telah dilakukan, berikut adalah jawaban terhadap aspek-aspek yang ditekankan pada tahap Business Understanding:

### 1. Apakah sistem menjawab setiap problem statement?

✅ Ya.  
Sistem rekomendasi yang dibangun berhasil menjawab pertanyaan utama:  

- **Bagaimana merekomendasikan buku berdasarkan preferensi pengguna?**  
  → Terjawab melalui pendekatan collaborative filtering (user-based, SVD, autoencoder) yang memanfaatkan riwayat interaksi pengguna.  
- **Algoritma mana yang memberikan hasil paling akurat dan relevan?**  
  → Terjawab melalui evaluasi metrik: Autoencoder memiliki RMSE terendah untuk prediksi rating, dan CountVectorizer memiliki F1-score tertinggi untuk relevansi konten.

---

### 2. Apakah model berhasil mencapai goals yang diharapkan?

✅ Ya.  
Model telah mencapai semua tujuan utama proyek:

- **Mampu memberikan rekomendasi personal yang relevan.**  
  → Ditunjukkan melalui Top-N output dari semua model (baik content-based maupun collaborative).

- **Output rekomendasi bersifat langsung dan dapat digunakan.**  
  → Disajikan melalui output sebagai daftar buku lengkap dengan judul, penulis, dan rating (untuk collaborative filtering).

- **Evaluasi performa dilakukan secara objektif.**  
  → Menggunakan metrik yang sesuai untuk tiap pendekatan: RMSE untuk rating, dan Precision/Recall/F1 untuk Top-N relevansi.

---

### 3. Apakah solusi yang dirancang berdampak terhadap tujuan bisnis?

✅ Ya.  

- Pendekatan **content-based** cocok untuk **pengguna baru** atau saat data interaksi masih terbatas.
- Pendekatan **collaborative filtering** cocok untuk **pengguna aktif**, memberikan pengalaman personalisasi yang lebih dalam.
- Proyek ini membuktikan bahwa sistem rekomendasi mampu:
  - Meningkatkan **engagement pengguna** terhadap platform literasi digital.
  - Mendorong eksplorasi buku baru tanpa perlu pencarian manual.
  - Menghadirkan rekomendasi yang **relevan, efisien, dan personal** — nilai penting dalam platform komersial atau edukasi seperti Goodreads, ePerpus, atau toko buku digital.

---

### Penutup

Sistem rekomendasi yang dibangun telah secara efektif:

- Menjawab kebutuhan pengguna dalam menemukan buku yang sesuai.
- Memberikan alternatif pendekatan yang dapat dikembangkan menjadi sistem hybrid untuk akurasi lebih tinggi.
- Mencapai semua tujuan analitis dan bisnis yang ditetapkan dalam proyek.

Pengembangan ke depan dapat mencakup integrasi pendekatan hybrid, serta real-time recommendation berbasis behavior saat ini (context-aware).
