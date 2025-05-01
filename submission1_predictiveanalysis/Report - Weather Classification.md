# Laporan Proyek Machine Learning Terapan - Zid Irsyadin Sartono Wijaogy

## **Weather Classification**

- **Nama:** Zid Irsyadin Sartono Wijaogy
- **Email:** [zidirsyadin@gmail.com](mailto:zidirsyadin@gmail.com) | [a208yaf520@devacademy.id](mailto:a208yaf520@devacademy.id)
- **ID Dicoding:** zid_isw

## **Domain Proyek**

### Latar Belakang

**Kualitas udara** adalah salah satu indikator penting yang mempengaruhi kesehatan masyarakat, lingkungan, dan kualitas hidup secara keseluruhan. Di banyak kota besar, termasuk Jakarta, polusi udara menjadi masalah yang semakin meningkat. Salah satu cara untuk mengukur kualitas udara adalah dengan menggunakan **Air Quality Index (AQI)**, yang memberikan gambaran tentang seberapa bersih atau tercemarnya udara di suatu daerah.

Jakarta, sebagai ibu kota Indonesia, mengalami masalah polusi udara yang signifikan. Kota ini memiliki tingkat polusi yang sangat tinggi, yang dapat berdampak pada kesehatan masyarakat. Menurut laporan dari **Jakarta Rendah Emisi**, kualitas udara di Jakarta telah memburuk dalam beberapa tahun terakhir, sebagian besar disebabkan oleh **kendaraan bermotor**, **industri**, dan **aktivitas pembakaran lahan** yang menyebabkan peningkatan polutan seperti **PM10**, **PM2.5**, **NO2**, **SO2**, dan **CO**. Seperti contoh hasil dari platform Jakarta Rendah Emisi:

![Image Source](https://rendahemisi.jakarta.go.id/assets/content/20211112163532_ind.jpg)

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

### Relevansi Proyek Dalam Menyelesaikan Masalah

Proyek ini bertujuan untuk membangun sistem yang dapat memprediksi dan mengklasifikasikan tingkat polusi udara di Jakarta menggunakan data **Air Quality Index (AQI)** yang mencakup berbagai polutan. Dengan menggunakan data dari berbagai stasiun pemantauan AQI di Jakarta, proyek ini bertujuan untuk memberikan informasi yang lebih cepat dan lebih akurat mengenai kondisi kualitas udara di Jakarta, yang pada gilirannya dapat membantu dalam pengambilan keputusan berbasis data untuk kebijakan lingkungan dan kesehatan masyarakat.

Di era digital ini, **teknologi** memainkan peran penting dalam mempermudah pemantauan dan pengelolaan kualitas udara. Dengan memanfaatkan teknologi dan **machine learning**, kita dapat menganalisis data kualitas udara secara real-time dan memberikan prediksi yang lebih akurat mengenai tren kualitas udara. Hal ini sangat penting karena kualitas udara yang buruk dapat memiliki dampak serius pada kesehatan manusia, seperti meningkatkan risiko penyakit pernapasan, kardiovaskular, dan bahkan kanker paru-paru. Oleh karena itu, memberikan informasi yang akurat dan mudah diakses kepada masyarakat sangat penting untuk meningkatkan kesadaran dan kewaspadaan mereka terhadap polusi udara.

Dengan sistem yang berbasis **machine learning**, kita dapat secara otomatis mengidentifikasi pola-pola dalam data yang mungkin tidak dapat dikenali dengan metode konvensional. Model-model ini dapat memprediksi perubahan kualitas udara di masa depan berdasarkan data historis, memberikan waktu bagi masyarakat dan pihak terkait untuk mengambil tindakan pencegahan. Misalnya, jika kualitas udara diprediksi akan buruk, sistem dapat memberikan peringatan kepada masyarakat untuk menghindari aktivitas luar ruangan atau menggunakan masker untuk melindungi diri mereka.

Selain itu, sistem ini dapat digunakan oleh pemerintah dan lembaga terkait untuk merumuskan kebijakan yang lebih tepat dalam mengatasi masalah polusi udara. Dengan data yang lebih akurat, pengambilan keputusan mengenai pembatasan lalu lintas, pengaturan industri, dan promosi penggunaan kendaraan ramah lingkungan dapat dilakukan dengan lebih efisien dan berdampak positif pada kualitas udara di Jakarta.

Pada akhirnya, teknologi ini tidak hanya membantu dalam **pencegahan** penyakit, tetapi juga meningkatkan **kesadaran masyarakat** akan pentingnya menjaga kualitas udara untuk kehidupan yang lebih sehat dan berkualitas. Dengan **machine learning**, kita bisa lebih proaktif dan siap menghadapi dampak buruk polusi udara di masa depan.

### Referensi

- [INDEKS STANDAR PENCEMAR UDARA (ISPU) SEBAGAI INFORMASI MUTU UDARA AMBIEN DI INDONESIA](https://ditppu.menlhk.go.id/portal/read/indeks-standar-pencemar-udara-ispu-sebagai-informasi-mutu-udara-ambien-di-indonesia)
- [Mencari Sumber Polusi di Udara melalui Source Apportionment](https://rendahemisi.jakarta.go.id/article/37/mencari-sumber-polusi-di-udara-melalui-source-apportionment)
- [Air Pollution - WHO](https://www.who.int/health-topics/air-pollution#tab=tab_1)

## **Business Understanding**

Pada bagian ini, saya akan menjelaskan proses klarifikasi masalah yang dihadapi, tujuan yang ingin dicapai, serta solusi yang dapat diimplementasikan untuk mencapai tujuan tersebut. Fokus utama proyek ini adalah memanfaatkan teknologi untuk memprediksi dan mengklasifikasikan tingkat polusi udara di Jakarta menggunakan data **Air Quality Index (AQI)** yang mencakup berbagai polutan.

### Problem Statements

Berikut adalah beberapa pernyataan masalah yang diangkat dalam konteks proyek ini:

- **Pernyataan Masalah 1**: Jakarta mengalami polusi udara yang sangat tinggi, yang berdampak pada kesehatan masyarakat. Kualitas udara yang buruk mengancam kesehatan pernapasan, kardiovaskular, serta menyebabkan kematian dini.
- **Pernyataan Masalah 2**: Masyarakat Jakarta tidak selalu memiliki informasi yang cepat dan akurat mengenai tingkat polusi udara, yang mengarah pada kurangnya kewaspadaan dan tindakan preventif terhadap polusi udara yang membahayakan.
- **Pernyataan Masalah 3**: Pemerintah dan lembaga terkait kesulitan dalam merumuskan kebijakan berbasis data terkait pengendalian polusi udara karena kurangnya sistem pemantauan dan prediksi yang efisien dan akurat.

### Goals

Tujuan dari pernyataan masalah di atas adalah sebagai berikut:

- **Jawaban untuk Pernyataan Masalah 1**: Membangun model prediksi sebagai cikal bakal sistem yang dapat memprediksi tingkat polusi udara secara real-time dan mengklasifikasikan kualitas udara berdasarkan standar AQI, sehingga dapat memberikan peringatan dini untuk mengurangi dampak negatif terhadap kesehatan masyarakat.
- **Jawaban untuk Pernyataan Masalah 2**: Memberikan informasi yang cepat, akurat, dan mudah diakses kepada masyarakat mengenai kualitas udara di Jakarta, yang dapat meningkatkan kesadaran dan kewaspadaan mereka terhadap bahaya polusi udara dan mendorong tindakan preventif.
- **Jawaban untuk Pernyataan Masalah 3**: Mengembangkan model sistem berbasis data yang menggunakan **machine learning** untuk memprediksi tren kualitas udara di masa depan, memberikan dukungan dalam pengambilan keputusan berbasis data untuk merumuskan kebijakan yang lebih efektif terkait pengendalian polusi udara.

### Solution Statements

Untuk mencapai tujuan yang disebutkan di atas, berikut adalah solusi yang diusulkan:

- **Solusi 1**: Menggunakan algoritma **machine learning** seperti **Random Forest**, **SVC**, dan **Gradient Boosting** untuk membangun dan memilih model prediksi kualitas udara yang akurat dan cepat. Dengan menggunakan data historis dari berbagai stasiun pemantauan AQI di Jakarta, model ini dapat mengklasifikasikan tingkat polusi udara dan memberikan prediksi kualitas udara dengan cepat dan tepat meski dengan data yang sedikit.

- **Solusi 2**: Menerapkan **cross-validation** dan **SMOTE** untuk menangani ketidakseimbangan kelas dalam dataset training. Dengan menggunakan teknik-teknik ini, model akan lebih robust dalam memprediksi polusi udara yang tinggi dan rendah, serta mampu memberikan akurasi yang lebih baik meskipun terdapat ketidakseimbangan dalam distribusi kelas.

### Evaluasi dan Metrik

Untuk memastikan bahwa solusi yang diusulkan dapat memenuhi tujuan, saya akan menggunakan **accuracy**, **F1-score**, dan **confusion matrix** sebagai metrik evaluasi training dan testing. Metrik-metrik ini akan membantu dalam menilai sejauh mana model dapat memprediksi kelas kualitas udara dengan akurat dan seimbang, serta mengidentifikasi area-area yang perlu ditingkatkan.

## **Data Understanding**

Dataset _Air Quality Index in Jakarta 2010-2023_ yang tersedia di Kaggle, yang dipublikasikan oleh pengguna dengan nama pengguna senadu34, menyediakan data mengenai kualitas udara di Jakarta selama periode 2010 hingga 2023 (all). Dataset ini sangat berguna untuk analisis kualitas udara dan studi terkait dampaknya terhadap kesehatan serta faktor lingkungan.

Dataset  ini memiliki 11 kolom dengan jumlah baris yang cukup bervariasi karena disebabkan oleh missing values. Berikut detail untuk informasi dataset:

| #   | Column    | Non-Null Count | Dtype   |
| --- | --------- | -------------- | ------- |
| 0   | tanggal   | 4626 non-null  | object  |
| 1   | stasiun   | 4626 non-null  | object  |
| 2   | pm10      | 4466 non-null  | float64 |
| 3   | pm25      | 723 non-null   | float64 |
| 4   | so2       | 4607 non-null  | float64 |
| 5   | co        | 4618 non-null  | float64 |
| 6   | o3        | 4621 non-null  | float64 |
| 7   | no2       | 4618 non-null  | float64 |
| 8   | max       | 4626 non-null  | float64 |
| 9   | critical  | 4625 non-null  | object  |
| 10  | categori  | 4626 non-null  | object  |

Dataset ini dapat diakses melalui tautan berikut:

[Air Quality Index in Jakarta 2010-2021 – Kaggle](https://www.kaggle.com/datasets/senadu34/air-quality-index-in-jakarta-2010-2021/data?select=ispu_dki_all.csv)

### Variabel-variabel pada Dataset Air Quality Index (AQI) Jakarta adalah sebagai berikut

- **Tanggal**: Kolom ini berisi informasi tanggal pengukuran kualitas udara pada setiap entri. Tipe data untuk kolom ini adalah **object** (string), yang mencakup format tanggal seperti "2010-01-01".

- **Stasiun**: Nama stasiun pemantauan kualitas udara di Jakarta. Setiap stasiun memiliki lokasi tertentu di Jakarta yang melakukan pengukuran kualitas udara secara berkala.

- **pm10**: Mengukur konsentrasi **particulate matter** dengan diameter kurang dari 10 mikrometer di udara. Partikel ini dapat masuk ke dalam saluran pernapasan manusia dan menyebabkan gangguan pernapasan. Tipe data: **float64**.

- **pm25**: Mengukur konsentrasi **particulate matter** dengan diameter kurang dari 2.5 mikrometer. Partikel yang lebih kecil ini dapat menembus lebih dalam ke dalam paru-paru dan memengaruhi kesehatan jantung dan pernapasan. Tipe data: **float64**.

- **so2**: Mengukur konsentrasi **sulfur dioxide** di udara. Gas ini umumnya berasal dari pembakaran bahan bakar fosil dan dapat menyebabkan iritasi pada saluran pernapasan serta berkontribusi pada pembentukan hujan asam. Tipe data: **float64**.

- **co**: Mengukur konsentrasi **carbon monoxide** di udara. Gas ini berbahaya karena menghalangi pengangkutan oksigen dalam tubuh dan dapat menyebabkan kerusakan pada sistem pernapasan serta gangguan jantung. Tipe data: **float64**.

- **o3**: Mengukur konsentrasi **ozone** di permukaan tanah. Ozone di atmosfer atas sangat penting untuk menyaring radiasi ultraviolet, tetapi ketika berada di permukaan tanah, ozone dapat menyebabkan gangguan pernapasan dan masalah kesehatan lainnya. Tipe data: **float64**.

- **no2**: Mengukur konsentrasi **nitrogen dioxide**. Gas ini dihasilkan dari pembakaran bahan bakar fosil, terutama oleh kendaraan dan industri, dan dapat menyebabkan gangguan pernapasan serta meningkatkan risiko penyakit jantung. Tipe data: **float64**.

- **max**: Kolom ini menunjukkan nilai **AQI maksimum** pada hari tertentu yang mewakili kualitas udara tertinggi yang terdeteksi pada tanggal tersebut. Kolom ini adalah nilai numerik yang mencerminkan tingkat pencemaran udara pada hari tersebut. Tipe data: **float64**.

- **Critical**: Kolom ini berisi konsentrasi polutan udara yang paling tinggi pada setiap entri. Ini menunjukkan polutan mana yang menjadi penyebab utama buruknya kualitas udara pada saat itu. Tipe data: **object**.

- **Category**: Kolom ini menunjukkan kategori kualitas udara berdasarkan AQI, dengan kategori seperti "Baik", "Sedang", "Tidak Sehat", "Sangat Tidak Sehat", "Berbahaya", dan "Tidak Ada Data". Tipe data: **object**.

### Insight dari Data Exploration (EDA)

Dalam tahap **Data Understanding**, berikut adalah beberapa insight yang diperoleh:

1. **Pengecekan Missing Values**:

   - Kolom **pm25** memiliki jumlah **missing values** yang sangat tinggi (3903 data hilang), yang menunjukkan bahwa pengukuran untuk polutan ini jarang tersedia.
   - Kolom **pm10** memiliki 160 missing values, sedangkan kolom **so2**, **co**, **no2**, dan **o3** masing-masing memiliki sedikit missing values, yang menunjukkan bahwa beberapa pengukuran polutan tidak tercatat di beberapa stasiun atau pada beberapa tanggal.
   - Kolom **Critical** hanya memiliki satu missing value, yang dapat diatasi dengan imputasi atau penghapusan baris tersebut.

2. **Pengecekan Duplikat**:

   - Dataset ini tidak memiliki duplikat, yang memastikan bahwa setiap entri dalam dataset adalah unik dan tidak ada data yang terulang.

3. **Pengecekan Outliers**:

   - Berdasarkan **boxplot** yang dihasilkan, terlihat adanya beberapa **outliers** pada kolom polutan seperti **pm10**, **pm25**, **so2**, **o3**, dan **no2**, yang menunjukkan adanya pengukuran dengan nilai sangat tinggi. Pengukuran tersebut perlu dipertimbangkan apakah perlu dibersihkan atau disesuaikan.

4. **Distribusi Data**:

   - **Jumlah Data per Stasiun**: Stasiun **DKI4 (Lubang Buaya)** memiliki jumlah data yang paling banyak, hampir mencapai 1600 entri, sementara stasiun **DKI1 (Bundaran HI)** memiliki jumlah data yang jauh lebih sedikit. Hal ini dapat menunjukkan bahwa beberapa stasiun lebih sering melakukan pengukuran, yang berpotensi menyebabkan ketidakseimbangan dalam distribusi data antara stasiun-stasiun.
   - **Distribusi AQI**: Sebagian besar data terdistribusi dalam kategori **AQI Sedang**, yang menunjukkan kualitas udara yang tidak terlalu buruk atau terlalu baik. Sedangkan kategori **AQI Baik** dan **Tidak Sehat** ditemukan dalam jumlah yang lebih sedikit.

5. **Analisis Fitur**:
   - Sebagian besar kolom polutan (**pm10**, **pm25**, **so2**, **co**, **o3**, **no2**) menunjukkan distribusi yang mirip dengan distribusi **long-tailed**, yang berarti terdapat nilai konsentrasi polutan yang lebih sering berada di bawah tingkat tertentu, tetapi ada juga beberapa entri dengan konsentrasi yang sangat tinggi.

6. **Insight Visualisasi**:
   - **Visualisasi Jumlah Data per Stasiun**: Stasiun DKI4 (Lubang Buaya) memiliki jumlah data yang jauh lebih banyak dibandingkan dengan stasiun-stasiun lainnya, seperti DKI1 (Bundaran HI) yang memiliki jumlah data yang jauh lebih sedikit. Hal ini bisa menunjukkan bahwa beberapa stasiun lebih sering melakukan pengukuran atau lebih banyak data yang terkumpul di lokasi tersebut. Ini bisa menyebabkan ketidakseimbangan dalam distribusi data antara stasiun yang mungkin perlu diperhatikan jika digunakan dalam analisis atau model prediksi. Jika diperlukan, kita bisa mengurangi data dari stasiun tertentu agar distribusi data lebih seimbang atau menggunakan strategi lain.
   - **Visualisasi Distribusi AQI Secara Keseluruhan**: Sebagian besar data terdistribusi dalam kategori Sedang, dengan jumlah frekuensi tertinggi. Sedangkan status AQI Baik dan Tidak Sehat terlihat jauh lebih sedikit. Ini menunjukkan bahwa kualitas udara sebagian besar berada pada kategori Sedang yang tidak terlalu buruk atau baik. Ini juga bisa berarti bahwa tidak ada kejadian yang terlalu ekstrem dalam dataset, dan sebagian besar data berada dalam rentang kualitas udara yang masih bisa diterima oleh masyarakat. Ini bisa menjadi indikator bahwa kualitas udara di Jakarta secara umum cukup stabil, meskipun ada beberapa peringatan tentang kualitas udara yang buruk, seperti Tidak Sehat.
   - **Visualisasi Tren AQI per Tahun**: Grafik tren AQI berdasarkan standar USA menunjukkan fluktuasi yang cukup besar antara tahun 2010 hingga 2022. Terlihat bahwa pada tahun 2022, beberapa stasiun menunjukkan penurunan yang signifikan pada nilai AQI dibandingkan tahun-tahun sebelumnya. Penurunan AQI pada tahun 2022 dapat disebabkan oleh beberapa faktor seperti pembatasan sosial selama pandemi COVID-19 yang menyebabkan pengurangan aktivitas industri dan transportasi. Seiring berjalannya waktu, kualitas udara dapat membaik akibat pengurangan emisi dari kendaraan dan industri yang beroperasi lebih sedikit pada masa-masa tertentu. Meskipun pandemi berakhir pada 2022, beberapa inisiatif hijau dan peningkatan kebijakan lingkungan bisa berkontribusi pada penurunan ini.

### Langkah Selanjutnya

Berdasarkan insight ini, langkah-langkah yang perlu dilakukan selanjutnya adalah:

- **Mengatasi Missing Values**: Mengimputasi missing values kolom lainnya yang memiliki missing values menggunakan teknik yang sesuai, kecuali kolom **"pm2.5"** karena memiliki nilai missing hingga 90%. Selain itu kolom **tanggal** juga akan dihapus agar membuat fitur yang digunakan untuk klasifikasi menjadi lebih valid.
- **Mengatasi Outliers**: Mempertimbangkan penghapusan atau penyesuaian nilai outliers pada kolom polutan, terutama yang sangat ekstrem.
- **Normalisasi atau Scaling**: Melakukan normalisasi atau scaling pada fitur numerik agar model machine learning dapat berfungsi dengan lebih baik.
- **Melakukan Label Encoder**: untuk mengubah nilai kategorikal menjadi numerikal agar memudahkan dalam proses training.
- **Menghapus Kelas yang Tidak Memiliki Sampel**: Menghapus kelas **"Tidak Ada Data"** dan **"Berbahaya"** agar model dapat berfokus pada data yang lebih representatif.

Dengan memahami data lebih mendalam, kita dapat membuat keputusan yang lebih tepat terkait pemrosesan data sebelum membangun model prediksi.

## **Data Preparation**

Pada bagian ini, saya menerapkan beberapa teknik **data preparation** untuk memastikan bahwa dataset siap digunakan dalam tahap **modeling**. Berikut adalah langkah-langkah yang dilakukan dalam **data preparation**:

1. **Menghapus Kolom yang Tidak Relevan**:

   - **Tanggal**: Kolom ini dihapus karena tidak memberikan informasi yang relevan untuk model. Meskipun tanggal dapat menunjukkan waktu pengukuran, fitur ini tidak memberikan hubungan langsung dengan prediksi kualitas udara.
   - **Tahun**: Kolom **tahun** dihapus karena merupakan hasil ekspansi dari kolom **tanggal**. Kolom ini tidak memberikan informasi tambahan yang signifikan karena tahun dapat diambil langsung dari **tanggal**.
   - **pm2.5**: Kolom **pm2.5** dihapus karena memiliki **missing value** yang sangat tinggi (90%), yang dapat memengaruhi kualitas data secara keseluruhan. Mengingat jumlah data hilang yang besar, kolom ini tidak dapat diandalkan untuk analisis lebih lanjut.

2. **Handling Missing Values**:

   Setelah menghapus kolom yang tidak relevan, saya melanjutkan dengan mengatasi **missing values** pada kolom-kolom yang memiliki nilai hilang. Kolom seperti **so2**, **co**, **o3**, dan **no2** diisi dengan **mean** untuk nilai numerik dan **modus** untuk kolom kategorikal seperti **critical**. Dengan cara ini, dataset tidak lagi memiliki missing values dan siap untuk analisis.

3. **Class Adjusting**:

   Saya memutuskan untuk menghapus kelas Berbahaya dan Tidak Ada Data, karena hanya berisi satu sampel dan akan mengganggu sistem secara signifikan nantinya.

4. **Label Encoding untuk Kolom Kategorikal**:

   - Kolom **critical** dan **stasiun**, yang merupakan kolom kategorikal, diubah menjadi numerik menggunakan **LabelEncoder**.
     - Kolom **critical** menggambarkan tingkat keparahan kualitas udara yang dapat berupa kategori seperti **BAIK**, **SEDANG**, dan **TIDAK SEHAT**.
     - Kolom **stasiun** berisi nama stasiun pemantauan yang melakukan pengukuran kualitas udara di berbagai lokasi Jakarta.
   - Dengan mengubah kolom ini menjadi numerik, model **machine learning** dapat memprosesnya dengan lebih mudah.

5. **Scaling (Normalisasi)**:

   Semua fitur numerik, seperti **pm10**, **so2**, **co**, **o3**, **no2**, dan **max**, distandarisasi menggunakan **StandardScaler**. Proses ini menstandarisasi data sehingga fitur-fitur tersebut memiliki **mean = 0** dan **std = 1**, yang sangat penting agar model **machine learning** dapat berfungsi dengan baik tanpa terpengaruh oleh perbedaan skala antar fitur.

6. **Splitting Data**:

   Untuk memastikan bahwa model dapat dievaluasi dengan baik dan tidak overfitting, dataset dibagi menjadi dua bagian utama: **training set** dan **testing set**. Pembagian ini dilakukan dengan menggunakan fungsi `train_test_split` dari library **scikit-learn**.

   **Proses Pembagian Data:**

   - **Training Set**:
      - Digunakan untuk melatih model machine learning.
      - Berisi 80% dari total data.

   - **Testing Set**:
      - Digunakan untuk mengevaluasi performa model pada data yang belum pernah dilihat sebelumnya.
      - Berisi 20% dari total data.

   **Hasil Pembagian Data:**

   Setelah pembagian, data training dan testing memiliki distribusi kelas yang serupa, sehingga model dapat dilatih dan diuji secara adil. Dengan pembagian ini, kita dapat mengevaluasi performa model secara lebih akurat pada data yang belum pernah dilihat sebelumnya.

7. **SMOTE (Synthetic Minority Over-sampling Technique)**:

   Untuk mengatasi **ketidakseimbangan kelas** dalam dataset, saya menggunakan **SMOTE** untuk menghasilkan sampel sintetis dari kelas yang kurang terwakili (misalnya, kategori AQI "Tidak Sehat"). Teknik ini membantu memastikan bahwa model dilatih pada data yang lebih seimbang dan dapat meningkatkan akurasi prediksi untuk kelas minoritas.

### Alasan Mengapa Tahapan Data Preparation Diperlukan

Tahapan **data preparation** sangat penting untuk memastikan bahwa dataset yang digunakan dalam **modeling** tidak terdistorsi oleh **missing values** atau **outliers**. Dengan menghapus kolom yang tidak relevan, seperti **tanggal**, **tahun**, dan **pm2.5**, saya mengurangi kompleksitas data yang tidak memberikan kontribusi berarti bagi model. Selain itu, dengan melakukan **scaling** pada fitur numerik, saya memastikan bahwa semua fitur berada pada skala yang sama, yang memungkinkan model **machine learning** untuk bekerja lebih efektif. Proses-proses ini memastikan bahwa dataset yang digunakan untuk membangun model prediksi kualitas udara Jakarta adalah **bersih**, **terstandarisasi**, dan **siap untuk dianalisis**. Terakhir melakukan **Splitting Data** untuk membagi dataset menjadi dataset training dan testing agar bisa mendapatkan hasil evaluasi model yang maksimal. Selain itu dilakukan juga metode **SMOTE** pada dataset training untuk menghadapi masalah imbalanced class atau ketidakseimbangan jumlah data antar kelas yang bisa membuat model dominan terhadap kelas mayoritas.

## Modeling

Pada bagian ini, saya membangun model **machine learning** untuk menyelesaikan permasalahan prediksi kualitas udara di Jakarta berdasarkan data **Air Quality Index (AQI)**.  
Beberapa algoritma klasifikasi diterapkan untuk mengevaluasi model, dan **Random Forest** dipilih sebagai model terbaik. Berikut ini penjelasan lengkap:

---

### Tahapan Modeling dan Parameter yang Digunakan

- **Data Splitting**: Dataset dibagi menggunakan **Stratified K-Fold Cross Validation** (`n_splits=5`, `shuffle=True`, `random_state=42`) untuk menjaga distribusi label di setiap fold.
- **Parameter Random State**: Seluruh model menggunakan `random_state=42` untuk memastikan reproducibility.
- **Model Training**: Menggunakan tiga algoritma utama:
  - Random Forest Classifier
  - Support Vector Classifier (SVC)
  - Gradient Boosting Classifier

---

### Algoritma yang Digunakan

#### 1. Random Forest Classifier

- **Penjelasan**:
  - Algoritma **ensemble** berbasis banyak **decision trees**.
  - Menggunakan teknik **bagging** untuk mengurangi overfitting dan meningkatkan akurasi.
  - Prediksi dilakukan berdasarkan voting mayoritas dari semua pohon.

- **Kelebihan**:
  - Robust terhadap overfitting.
  - Dapat menangani data numerik maupun kategorikal.
  - Mudah digunakan tanpa tuning parameter ekstrem.

- **Kekurangan**:
  - Model kompleks dan besar.
  - Waktu komputasi lebih lama untuk dataset besar.

- **Parameter yang Digunakan**:
  - `random_state=42`

---

#### 2. Support Vector Classifier (SVC)

- **Penjelasan**:
  - Berbasis konsep **Support Vector Machine** untuk mencari **hyperplane** terbaik.
  - Cocok untuk klasifikasi data non-linear menggunakan **kernel trick**.

- **Kelebihan**:
  - Kinerja tinggi pada data non-linear.
  - Sangat efektif untuk dataset berdimensi tinggi.

- **Kekurangan**:
  - Sensitif terhadap pilihan kernel.
  - Tidak efisien untuk dataset besar.

- **Parameter yang Digunakan**:
  - `random_state=42`
  - `probability=True` untuk menghitung probabilitas prediksi.

---

#### 3. Gradient Boosting Classifier

- **Penjelasan**:
  - Algoritma **ensemble boosting** yang membangun model secara sekuensial.
  - Tiap pohon baru berusaha memperbaiki error dari pohon sebelumnya.

- **Kelebihan**:
  - Akurasi tinggi, sangat kompetitif dalam banyak kompetisi.
  - Dapat menangani hubungan non-linear antar fitur.

- **Kekurangan**:
  - Rentan overfitting tanpa tuning yang tepat.
  - Waktu pelatihan lebih lama.

- **Parameter yang Digunakan**:
  - `random_state=42`

---

### Pemilihan Model Terbaik

Karena menggunakan lebih dari satu algoritma, pemilihan model terbaik dilakukan berdasarkan:

- Akurasi dan F1-Score pada data **testing**.
- Waktu eksekusi (efisiensi model).
- Stabilitas prediksi pada semua kelas.

**Random Forest** dipilih sebagai model terbaik karena:

- Memberikan akurasi dan F1-score sempurna (1.0000) pada data **training** dan **testing**.
- Memiliki waktu komputasi lebih efisien dibandingkan Gradient Boosting.
- Sederhana dalam tuning dan interpretasi dibandingkan SVC.

---

## Evaluation

### Metrik Evaluasi yang Digunakan

1. **Accuracy**
2. **Precision**
3. **Recall**
4. **F1-Score**

#### Penjelasan Metrik

- **Accuracy**:
  - Formula: `(Jumlah prediksi benar) / (Jumlah total prediksi)`
  - Mengukur keseluruhan akurasi prediksi model.

- **Precision**:
  - Formula: `TP / (TP + FP)`
  - Fokus pada akurasi prediksi positif model.

- **Recall**:
  - Formula: `TP / (TP + FN)`
  - Mengukur kemampuan model untuk menemukan semua data positif.

- **F1-Score**:
  - Formula: `2 * (Precision * Recall) / (Precision + Recall)`
  - Harmonic mean dari Precision dan Recall, berguna untuk data yang imbalance.

---

### Hasil Evaluasi Model

| Model                | Training Accuracy | Training F1-Score | Testing Accuracy | Testing F1-Score | Training Time (s) | Testing Time (s) |
|----------------------|-------------------|-------------------|------------------|------------------|-------------------|------------------|
| **Random Forest**     | 1.0000            | 1.0000            | 1.0000           | 1.0000           | 7.9813            | 0.0285           |
| **SVC**               | 0.9714            | 0.9713            | 0.9503           | 0.9503           | 29.6592           | 0.3463           |
| **Gradient Boosting** | 1.0000            | 1.0000            | 1.0000           | 1.0000           | 48.2638           | 0.0000           |

---

### Insight Evaluasi

- **Random Forest** dan **Gradient Boosting** menunjukkan akurasi sempurna, namun Random Forest lebih cepat dalam testing.
- **SVC** sedikit lebih rendah akurasinya pada data testing dan memerlukan waktu testing lebih lama.
- **Random Forest** lebih seimbang dalam performa akurasi dan kecepatan, sehingga lebih unggul sebagai solusi akhir.

---

### Kesimpulan

**Random Forest Classifier** dipilih sebagai model final karena:

- Akurasi dan F1-score sempurna di semua kelas.
- Waktu training dan testing relatif cepat.
- Robust terhadap overfitting dan lebih mudah diimplementasikan untuk kasus ini.

## **Kesimpulan Akhir**

Berdasarkan hasil evaluasi model, dapat disimpulkan bahwa model prediksi kualitas udara yang dibangun berhasil memberikan kontribusi signifikan terhadap Business Understanding proyek ini. Berikut adalah analisis mengenai apakah model ini berhasil menjawab problem statement, mencapai goal yang diharapkan, dan memberikan dampak positif terhadap solusi yang direncanakan:

### 1. Menjawab Problem Statement

Model machine learning yang dipilih (**Random Forest**) berhasil memprediksi tingkat polusi udara dengan akurasi yang tinggi dan kecepatan yang sangat baik. Hal ini menjawab permasalahan pertama, yakni tingginya polusi udara di Jakarta, dengan menyediakan solusi prediksi kualitas udara yang cepat dan tepat. Data yang digunakan dalam model ini berasal dari berbagai stasiun pemantauan AQI di Jakarta, memungkinkan model untuk memberikan prediksi real-time terkait kualitas udara.

Selain itu, model ini juga berhasil menjawab masalah kedua sekaligus ketiga mengenai kurangnya informasi yang cepat dan akurat tentang kualitas udara. Dengan prediksi yang akurat dan hasil yang dapat diakses dengan mudah, model ini memberikan informasi yang lebih cepat kepada masyarakat, yang dapat meningkatkan kewaspadaan terhadap bahaya polusi udara.

### 2. Mencapai Goals yang Diharapkan

Model ini berhasil mencapai tujuan yang telah ditetapkan, yaitu membuat sistem prediksi yang akurat dan cepat dalam memantau kualitas udara, yang dapat digunakan oleh masyarakat dan lembaga terkait. Dengan implementasi teknik **cross-validation** dan **SMOTE** untuk menangani ketidakseimbangan data, model menunjukkan kemampuan yang sangat baik dalam memprediksi berbagai level polusi udara, baik yang tinggi maupun rendah. Hal ini memastikan bahwa prediksi yang dihasilkan tetap akurat meskipun terdapat ketidakseimbangan kelas dalam dataset.

Tujuan jangka panjang untuk memberikan dasar yang kuat bagi pembuatan sistem pengambilan keputusan berbasis data dalam kebijakan pengendalian polusi udara juga telah tercapai, dengan model yang memberikan wawasan yang relevan untuk perencanaan kebijakan yang lebih efektif.

### 3. Dampak Terhadap Solusi Statement

Setiap solusi yang direncanakan memberikan dampak positif terhadap hasil yang diinginkan, dengan penerapan teknik-teknik tertentu seperti **machine learning**, **SMOTE**, dan **cross-validation**.

- **Penerapan Machine Learning**: Penggunaan algoritma **Random Forest** dalam membangun model prediksi kualitas udara terbukti memberikan dampak yang signifikan. Model ini mampu memproses data historis AQI dengan baik dan menghasilkan prediksi yang cepat serta akurat.

- **Penggunaan SMOTE**: Dalam menangani ketidakseimbangan kelas dalam dataset, penerapan **SMOTE** berhasil meningkatkan kualitas model dalam memprediksi polusi udara dengan lebih seimbang, meskipun ada lebih banyak data polusi udara rendah daripada polusi udara tinggi. Dengan SMOTE, model lebih robust dan dapat memprediksi dengan lebih baik kondisi polusi udara yang ekstrem (tinggi) sekalipun. Ini memastikan bahwa model tidak bias terhadap kelas tertentu, dan hasil prediksi menjadi lebih representatif.

- **Implementasi Cross-Validation**: Teknik **cross-validation** diterapkan untuk meningkatkan generalisasi model dan mengurangi kemungkinan overfitting. Hal ini berkontribusi pada kestabilan dan konsistensi hasil prediksi. Dengan teknik ini, model diuji pada berbagai subset data, yang memastikan bahwa model dapat memberikan performa yang baik tidak hanya pada data pelatihan, tetapi juga pada data yang belum pernah dilihat sebelumnya. Ini meningkatkan keandalan model saat diterapkan dalam situasi dunia nyata.

**---Ini adalah bagian akhir laporan---**
