# %% [markdown]
# # **Weather Classification**
# 
# - **Nama:** Zid Irsyadin Sartono Wijaogy
# - **Email:** zidirsyadin@gmail.com | a208yaf520@devacademy.id
# - **ID Dicoding:** zid_isw

# %% [markdown]
# ## **Perkenalan Dataset**

# %% [markdown]
# ### Air Quality Index in Jakarta 2010-2023 Dataset
# 
# Dataset *Air Quality Index in Jakarta 2010-2023* yang tersedia di Kaggle, yang dipublikasikan oleh pengguna dengan nama pengguna senadu34, menyediakan data mengenai kualitas udara di Jakarta selama periode 2010 hingga 2021. Dataset ini sangat berguna untuk analisis kualitas udara dan studi terkait dampaknya terhadap kesehatan serta faktor lingkungan.
# 
# Dataset ini menyajikan data simulasi yang mencakup berbagai parameter terkait kualitas udara, seperti:
# 
# - **Indeks Polutan Udara (ISPU)**: Mengukur kualitas udara berdasarkan konsentrasi berbagai polutan seperti PM10, PM2.5, CO, NO2, dan O3.
# - **Tanggal**: Waktu pengukuran kualitas udara.
# - **Stasiun**: Titik pengukuran kualitas udara di Jakarta.
# 
# Dataset ini dapat diakses melalui tautan berikut:
# 
# [Air Quality Index in Jakarta 2010-2021 – Kaggle](https://www.kaggle.com/datasets/senadu34/air-quality-index-in-jakarta-2010-2021/data?select=ispu_dki_all.csv)
# 

# %% [markdown]
# ## **Import Library**

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import time
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from imblearn.over_sampling import SMOTE

# %% [markdown]
# ## **Data Loading**

# %%
file_path = 'ispu_dki_all.csv'

# Memuat dataset
data = pd.read_csv(file_path)

# Menampilkan beberapa baris pertama untuk melihat struktur data
data.head()

# %% [markdown]
# ### Data Loading
# 
# Dalam tahap **Data Loading**, dataset yang digunakan dalam proyek ini sebelumnya terdiri dari dua jenis file, yaitu:
# 
# 1. **ispu_dkix**: File ini merepresentasikan hasil pengukuran **AQI** dari setiap stasiun pemantauan, dengan “x” menunjukkan nomor urut stasiun. File ini mencakup hasil pengukuran AQI dari tahun 2010 hingga 2021 untuk setiap stasiun pemantauan secara terpisah.
#    
# 2. **ispu_dki_all**: File ini merupakan hasil gabungan dari pengukuran AQI dari semua stasiun pemantauan, di mana nilai AQI tertinggi pada setiap hari akan merepresentasikan kualitas udara Jakarta pada hari tersebut. File ini mencakup hasil pengukuran AQI dari tahun 2010 hingga 2023.
# 
# Dalam proyek ini, **saya memilih menggunakan file 'ispu_dki_all'** karena file ini mencakup data yang lebih banyak dan mencakup pengukuran AQI dari lebih banyak tahun, sehingga memberikan gambaran yang lebih komprehensif tentang kualitas udara di Jakarta.
# 

# %% [markdown]
# ## **Data Understanding**

# %% [markdown]
# ### **Explorartory Data Analysis (EDA)**

# %%
# Menampilkan informasi tentang dataset
data.info()

# Menampilkan statistik deskriptif untuk data numerik
data.describe()

# %%
# Mengecek missing values
missing_values = data.isnull().sum()
print(f"Missing values per column:\n{missing_values}")

# %%
# Mengecek duplikat
duplicates = data.duplicated().sum()
print(f"Jumlah duplikat: {duplicates}")

# %%
# Boxplot untuk mendeteksi outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data.select_dtypes(include=[np.number]))  # Untuk kolom numerik
plt.title('Boxplot untuk Deteksi Outliers')
plt.show()


# %%
# Menampilkan jumlah data per stasiun
station_counts = data['stasiun'].value_counts().reset_index()
station_counts.columns = ['Stasiun', 'Jumlah Data']

# Visualisasi jumlah data per stasiun dengan Plotly
fig = px.bar(station_counts, 
             x='Stasiun', 
             y='Jumlah Data', 
             title='Jumlah Data per Stasiun', 
             labels={'Stasiun': 'Nama Stasiun', 'Jumlah Data': 'Jumlah Data'},
             color='Jumlah Data',  
             template='plotly_dark')  

fig.update_xaxes() 
fig.show()

# %%
# Visualisasi distribusi AQI secara keseluruhan
fig = px.histogram(data, 
                   x='categori', 
                   nbins=30, 
                   title='Distribusi AQI Secara Keseluruhan', 
                   labels={'categori': 'AQI'},
                   marginal='rug')

fig.update_layout(
    xaxis_title='AQI', 
    yaxis_title='Frekuensi',
    template='plotly_dark'  
)

fig.show()

# %%
# Buat subplots untuk setiap polutan
fig, axes = plt.subplots(2, 3, figsize=(15, 8))  # 2 baris, 3 kolom
pollution_columns = ["pm10", "co", "o3", "no2", "so2"]
axes = axes.flatten()

for i, col in enumerate(pollution_columns):
    sns.histplot(data[col], bins=30, kde=False, ax=axes[i], color="blue")
    axes[i].set_title(f"Distribusi {col}")
    axes[i].set_xlabel("Konsentrasi")
    axes[i].set_ylabel("Frekuensi")

plt.tight_layout()
plt.show()

# %%
# Fungsi untuk menghitung AQI berdasarkan rentang USA
def calculate_aqi(concentration, breakpoints, aqi_values):
    for i in range(len(breakpoints) - 1):
        if breakpoints[i] <= concentration <= breakpoints[i + 1]:
            aqi = ((aqi_values[i + 1] - aqi_values[i]) / (breakpoints[i + 1] - breakpoints[i])) * \
                  (concentration - breakpoints[i]) + aqi_values[i]
            return round(aqi)
    return np.nan  # Jika nilai di luar jangkauan

# Rentang untuk masing-masing polutan berdasarkan standar USA
pollutant_ranges = {
    'pm10': ([0, 54, 155, 255, 355, 425, 605], [0, 50, 100, 150, 200, 300, 500]),
    'so2': ([0, 35, 75, 185, 305, 605, 805], [0, 50, 100, 150, 200, 300, 500]),
    'no2': ([0, 53, 100, 360, 649, 1249, 2049], [0, 50, 100, 150, 200, 300, 500]),
    'co': ([0, 4.4, 9.4, 12.4, 15.4, 30.4, 40.4], [0, 50, 100, 150, 200, 300, 500]),
    'o3': ([0, 54, 70, 85, 105, 200, 404], [0, 50, 100, 150, 200, 300, 500])
}

# Menghitung AQI per polutan
data_aqi = data[['pm10', 'so2', 'no2', 'co', 'o3']].copy()  # Menggunakan fitur yang tersedia
for pollutant, (breakpoints, aqi_values) in pollutant_ranges.items():
    data_aqi[pollutant + '_AQI'] = data_aqi[pollutant].apply(lambda x: calculate_aqi(x, breakpoints, aqi_values))

# Mengambil nilai AQI maksimum sebagai AQI utama
data['AQI_True'] = data_aqi[[col for col in data_aqi.columns if '_AQI' in col]].max(axis=1)

# Menambahkan kolom 'tahun' dengan mengekstrak tahun dari kolom 'tanggal'
data['tahun'] = pd.to_datetime(data['tanggal']).dt.year

# 2. Agregasi rata-rata AQI per tahun dan per stasiun
aqi_trend = data.groupby(['tahun', 'stasiun'])['AQI_True'].mean().reset_index()
aqi_trend.columns = ['tahun', 'stasiun', 'AQI_True']

# 3. Visualisasi tren AQI berdasarkan perhitungan USA dengan Plotly
fig = px.line(aqi_trend, x='tahun', y='AQI_True', color='stasiun', markers=True,
              title='Tren Kualitas Udara (AQI USA) di Berbagai Lokasi Pemantauan',
              labels={'tahun': 'Tahun', 'AQI_True': 'Indeks Kualitas Udara (AQI)', 'stasiun': 'Stasiun'})
fig.update_layout(template='plotly_dark', legend_title='Stasiun')
fig.show()


# %% [markdown]
# #### Data Understanding Insight
# 
# Dalam tahap **Data Understanding**, saya memulai dengan memeriksa struktur dataset **Air Quality Index (AQI)** Jakarta yang terdiri dari 4626 entri dan 11 kolom. Berikut adalah beberapa insight yang saya peroleh:
# 
# 1. **Informasi Kolom**:
#    - **Tanggal**: Kolom ini berisi informasi tanggal pengukuran AQI, dengan tipe data **object**.
#    - **Stasiun**: Nama stasiun pemantauan yang melakukan pengukuran.
#    - **pm10, pm25, so2, co, o3, no2, max**: Kolom-kolom ini berisi nilai konsentrasi polutan udara yang diukur, dengan tipe data **float64**. Nilai-nilai ini menunjukkan kualitas udara berdasarkan polutan tertentu.
#    - **Critical**: Kolom ini berisi konsentrasi polutan apa yang paling tinggi di tanggal dan stasiun itu.
#    - **Category**: Kolom kategori yang menunjukkan status kualitas udara berdasarkan kategori AQI (Baik, Sedang, Tidak Sehat, Sangat Tidak Sehat, Berbahaya, Tidak Ada Data).
# 
# 2. **Pengecekan Missing Values**:
#    - Kolom **pm25** memiliki jumlah missing values yang sangat tinggi (3903 data hilang).
#    - Kolom **pm10** memiliki 160 missing values.
#    - Kolom **so2**, **co**, **no2**, dan **o3** masing-masing memiliki beberapa missing values, yang mengindikasikan adanya data yang hilang untuk pengukuran polutan tertentu pada beberapa stasiun.
#    - **Critical** hanya memiliki 1 missing value.
#    - Selain fitur tersebut, tidak ada yang memiliki missing values.
#    Langkah selanjutnya adalah mengisi atau menghapus missing values, tergantung pada distribusi dan pentingnya kolom tersebut.
# 
# 3. **Pengecekan Duplikat**:
#    - Tidak ada data duplikat dalam dataset, yang menunjukkan bahwa setiap entri di dataset unik dan tidak ada entri ganda.
# 
# 4. **Pengecekan Outliers**:
#    - Berdasarkan **boxplot** yang dihasilkan, terlihat bahwa terdapat beberapa **outliers** pada kolom polutan seperti **pm10**, **pm25**, **so2**, **o3**, dan **no2**. Ini menunjukkan bahwa ada beberapa pengukuran yang sangat tinggi yang perlu dipertimbangkan apakah perlu dihapus atau disesuaikan.
# 
# 5. **Distribusi Data**:
#    - **Jumlah Data per Stasiun**: Stasiun **DKI4 (Lubang Buaya)** memiliki jumlah data yang paling banyak, hampir mencapai 1600 entri, sementara stasiun **DKI1 (Bundaran HI)** memiliki jumlah data yang jauh lebih sedikit.
#    - **Distribusi AQI**: Sebagian besar data memiliki status **AQI Sedang**, dengan jumlah entri terbanyak. Status **AQI Baik** dan **Tidak Sehat** juga ditemukan, tetapi dalam jumlah yang lebih sedikit.
#    
# 6. **Analisis Fitur**:
#    - Sebagian besar kolom polutan (**pm10**, **pm25**, **so2**, **co**, **o3**, **no2**) menunjukkan distribusi yang mirip dengan distribusi **long-tailed**, yang berarti terdapat nilai konsentrasi polutan yang lebih sering berada di bawah tingkat tertentu, tetapi ada juga beberapa entri dengan konsentrasi yang sangat tinggi.
# 
# 7. **Insight Visualisasi**:
#    - **Visualisasi Jumlah Data per Stasiun**: Stasiun DKI4 (Lubang Buaya) memiliki jumlah data yang jauh lebih banyak dibandingkan dengan stasiun-stasiun lainnya, seperti DKI1 (Bundaran HI) yang memiliki jumlah data yang jauh lebih sedikit. Hal ini bisa menunjukkan bahwa beberapa stasiun lebih sering melakukan pengukuran atau lebih banyak data yang terkumpul di lokasi tersebut. Ini bisa menyebabkan ketidakseimbangan dalam distribusi data antara stasiun yang mungkin perlu diperhatikan jika digunakan dalam analisis atau model prediksi. Jika diperlukan, kita bisa mengurangi data dari stasiun tertentu agar distribusi data lebih seimbang atau menggunakan strategi lain.
#    - **Visualisasi Distribusi AQI Secara Keseluruhan**: Sebagian besar data terdistribusi dalam kategori Sedang, dengan jumlah frekuensi tertinggi. Sedangkan status AQI Baik dan Tidak Sehat terlihat jauh lebih sedikit. Ini menunjukkan bahwa kualitas udara sebagian besar berada pada kategori Sedang yang tidak terlalu buruk atau baik. Ini juga bisa berarti bahwa tidak ada kejadian yang terlalu ekstrem dalam dataset, dan sebagian besar data berada dalam rentang kualitas udara yang masih bisa diterima oleh masyarakat. Ini bisa menjadi indikator bahwa kualitas udara di Jakarta secara umum cukup stabil, meskipun ada beberapa peringatan tentang kualitas udara yang buruk, seperti Tidak Sehat.
#    - **Visualisasi Tren AQI per Tahun**: Grafik tren AQI berdasarkan standar USA menunjukkan fluktuasi yang cukup besar antara tahun 2010 hingga 2022. Terlihat bahwa pada tahun 2022, beberapa stasiun menunjukkan penurunan yang signifikan pada nilai AQI dibandingkan tahun-tahun sebelumnya. Penurunan AQI pada tahun 2022 dapat disebabkan oleh beberapa faktor seperti pembatasan sosial selama pandemi COVID-19 yang menyebabkan pengurangan aktivitas industri dan transportasi. Seiring berjalannya waktu, kualitas udara dapat membaik akibat pengurangan emisi dari kendaraan dan industri yang beroperasi lebih sedikit pada masa-masa tertentu. Meskipun pandemi berakhir pada 2022, beberapa inisiatif hijau dan peningkatan kebijakan lingkungan bisa berkontribusi pada penurunan ini.
# 
# #### Langkah Selanjutnya
# Berdasarkan insight ini, langkah selanjutnya adalah:
# - Menangani missing values, terutama pada **pm25** yang akan dihapus karena nilai missing mencapai lebih dari 90%. Selain itu kolom **tanggal** juga akan dihapus agar membuat fitur yang digunakan untuk klasifikasi menjadi lebih valid.
# - Mengabaikan Outliers karena merupakan data yang valid
# - Melakukan normalisasi atau scaling pada fitur numerik agar model machine learning dapat berfungsi dengan lebih baik.
# - Menghapus kelas yang tidak memiliki sampel atau sangat sedikit
# 
# Dengan memahami data lebih mendalam, kita dapat membuat keputusan yang lebih tepat terkait pemrosesan data sebelum membangun model prediksi.
# 

# %% [markdown]
# ## **Data Preparation**

# %%
df_cleaned = data.copy()
# Menghapus kolom 'pm25' karena missing values-nya lebih dari 90% dan tanggal karena tidak digunakan dalam perhitungan AQI
df_cleaned = df_cleaned.drop(columns=['tanggal', 'pm25', 'tahun'])

# Mengisi missing values pada kolom numerik (gunakan rata-rata atau mean)
imputer_numeric = SimpleImputer(strategy='mean')
df_cleaned[['pm10', 'so2', 'co', 'o3', 'no2', 'AQI_True']] = imputer_numeric.fit_transform(df_cleaned[['pm10', 'so2', 'co', 'o3', 'no2', 'AQI_True']])

# Mengisi missing values pada kolom kategorikal (misalnya 'critical' dengan modus)
imputer_categorical = SimpleImputer(strategy='most_frequent')
df_cleaned['critical'] = imputer_categorical.fit_transform(df_cleaned[['critical']]).ravel()

# Memeriksa missing values setelah imputasi
print(df_cleaned.isnull().sum())

# %%
df_cleaned = df_cleaned[df_cleaned['categori'].notna() & (df_cleaned['categori'] != 'TIDAK ADA DATA') & (df_cleaned['categori'] != 'BERBAHAYA')]

# Verifikasi hasil
print(df_cleaned['categori'].value_counts())

# %%
# Mengubah kolom 'critical' dan 'stasiun' menjadi numerik
le = LabelEncoder()

df_cleaned['critical'] = le.fit_transform(df_cleaned['critical'])
df_cleaned['stasiun'] = le.fit_transform(df_cleaned['stasiun'])

# Menampilkan beberapa baris setelah encoding
print(df_cleaned[['critical', 'stasiun']].head())


# %%
# Scaling fitur numerik
scaler = StandardScaler()
df_cleaned[['pm10', 'so2', 'co', 'o3', 'no2', 'max', 'AQI_True']] = scaler.fit_transform(df_cleaned[['pm10', 'so2', 'co', 'o3', 'no2', 'max', 'AQI_True']])

# Menampilkan beberapa baris setelah scaling
print(df_cleaned.head())


# %%
df_cleaned.info()

# %% [markdown]
# ### **Splitting Data**

# %%
X = df_cleaned.drop('categori', axis=1) 
y = df_cleaned['categori']  

# Membagi data menjadi 80% training dan 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# %% [markdown]
# ### **SMOTE**

# %%
# Menggunakan SMOTE untuk menangani ketidakseimbangan kelas
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# %% [markdown]
# #### Data Preparation Insight
# 
# Setelah melakukan tahap **Data Preparation**, berikut adalah beberapa insight yang dapat diperoleh:
# 
# 1. **Missing Values**:
#    - **Tidak ada missing values** setelah melakukan imputasi pada kolom yang memiliki nilai hilang seperti **so2**, **co**, **o3**, dan **no2**. Semua nilai **missing** telah berhasil diisi dengan menggunakan **mean** untuk kolom numerik dan **modus** untuk kolom kategorikal seperti **critical**.
# 
# 2. **Class Adjusting**:
#    - Saya memutuskan untuk menghapus kelas **Berbahaya** dan **Tidak Ada Data**, karena hanya berisi satu sampel dan akan mengganggu sistem secara signifikan nantinya.
# 
# 3. **Label Encoding untuk Kolom Kategorikal**:
#    - Kolom **critical** dan **stasiun**, yang merupakan kolom kategorikal, diubah menjadi numerik menggunakan **LabelEncoder**. 
#      - Kolom **critical** menggambarkan tingkat keparahan kualitas udara yang dapat berupa kategori seperti **BAIK**, **SEDANG**, dan **TIDAK SEHAT**.
#      - Kolom **stasiun** berisi nama stasiun pemantauan yang melakukan pengukuran kualitas udara di berbagai lokasi Jakarta.
#    - Dengan mengubah kolom ini menjadi numerik, model **machine learning** dapat memprosesnya dengan lebih mudah.
# 
# 4. **Scaling (Normalisasi)**:
#    - Semua fitur numerik, seperti **pm10**, **so2**, **co**, **o3**, **no2**, dan **max**, distandarisasi menggunakan **StandardScaler**. Proses ini menstandarisasi data sehingga fitur-fitur tersebut memiliki **mean = 0** dan **std = 1**, yang sangat penting agar model **machine learning** dapat berfungsi dengan baik tanpa terpengaruh oleh perbedaan skala antar fitur.
# 
# 5. **Splitting Data**:
# 
#    Untuk memastikan bahwa model dapat dievaluasi dengan baik dan tidak overfitting, dataset dibagi menjadi dua bagian utama: **training set** dan **testing set**. Pembagian ini dilakukan dengan menggunakan fungsi `train_test_split` dari library **scikit-learn**.
# 
#    **Proses Pembagian Data:**
# 
#    - **Training Set**:
#       - Digunakan untuk melatih model machine learning.
#       - Berisi 80% dari total data.
# 
#    - **Testing Set**:
#       - Digunakan untuk mengevaluasi performa model pada data yang belum pernah dilihat sebelumnya.
#       - Berisi 20% dari total data.
# 
#    **Hasil Pembagian Data:**
# 
#    Setelah pembagian, data training dan testing memiliki distribusi kelas yang serupa, sehingga model dapat dilatih dan diuji secara adil. Dengan pembagian ini, kita dapat mengevaluasi performa model secara lebih akurat pada data yang belum pernah dilihat sebelumnya.
# 
# 6. **SMOTE (Synthetic Minority Over-sampling Technique)**:
# 
#    Untuk mengatasi **ketidakseimbangan kelas** dalam dataset, saya menggunakan **SMOTE** untuk menghasilkan sampel sintetis dari kelas yang kurang terwakili (misalnya, kategori AQI "Tidak Sehat"). Teknik ini membantu memastikan bahwa model dilatih pada data yang lebih seimbang dan dapat meningkatkan akurasi prediksi untuk kelas minoritas.
# 
# Dengan data yang sudah siap, kita dapat melanjutkan ke tahap **modeling** untuk membangun model prediksi kualitas udara Jakarta.
# 

# %% [markdown]
# ## **Modeling**

# %%
# Inisialisasi model
rf_classifier = RandomForestClassifier(random_state=42)
svc_classifier = SVC(random_state=42, probability=True)
gb_classifier = GradientBoostingClassifier(random_state=42)

# Menggunakan Stratified K-Fold Cross-Validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Fungsi untuk mengevaluasi model dengan Cross-Validation dan waktu eksekusi
def evaluate_model_with_cv(model, X, y, model_name):
    print(f"Evaluating {model_name}...\n")

    # Catat waktu mulai eksekusi
    start_time = time.time()

    # Cross-validation metrics
    accuracy_scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
    f1_scores = cross_val_score(model, X, y, cv=cv, scoring='f1_macro')
    
    # Catat waktu selesai eksekusi
    end_time = time.time()
    execution_time = end_time - start_time

    # Tampilkan hasil cross-validation
    print(f"Cross-Val Accuracy: {accuracy_scores.mean():.4f}")
    print(f"Cross-Val F1-Score: {f1_scores.mean():.4f}\n")
    print(f"Execution Time: {execution_time:.4f} seconds\n")

    # Train model pada resampled data
    model.fit(X, y)

    # Predictions pada training data
    y_pred = model.predict(X)

    # Classification report
    print(f"Classification Report for {model_name}:\n")
    print(classification_report(y, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(cmap='viridis')
    disp.ax_.set_title(f'Confusion Matrix for {model_name}')
    plt.show()

    return accuracy_scores.mean(), f1_scores.mean(), execution_time

# %% [markdown]
# ### Penjelasan Tiga Algoritma Klasifikasi
# 
# Pada proyek ini, tiga algoritma klasifikasi digunakan untuk mengevaluasi model prediksi kualitas udara Jakarta berdasarkan data AQI. Berikut adalah penjelasan mendalam tentang tiga algoritma tersebut:
# 
# ---
# 
# #### 1. **Random Forest Classifier**
# 
# **Pengertian**:
# - **Random Forest** adalah algoritma ensemble learning yang menggabungkan beberapa **decision trees** untuk meningkatkan akurasi dan mengurangi overfitting.
# - Setiap **decision tree** dalam Random Forest dilatih menggunakan subset acak dari data dan fitur. Prediksi akhir dilakukan dengan **voting** mayoritas hasil dari pohon-pohon keputusan tersebut.
# 
# **Cara Kerja**:
# - **Bagging (Bootstrap Aggregating)** digunakan untuk membangun beberapa pohon keputusan dengan mengambil sampel acak dari data (dengan pengembalian). 
# - Setiap pohon membuat prediksi, dan prediksi akhir ditentukan dengan **voting** mayoritas untuk klasifikasi.
# 
# **Kelebihan**:
# - **Robust terhadap overfitting**: Random Forest dapat mengatasi overfitting dengan baik, terutama pada data yang lebih besar dan kompleks.
# - **Mudah digunakan**: Tidak membutuhkan banyak tuning parameter dan dapat bekerja dengan baik dengan default settings.
# - **Dapat menangani data numerik dan kategorikal**: Random Forest dapat bekerja dengan baik dengan berbagai jenis data.
# 
# **Kekurangan**:
# - **Kompleksitas tinggi**: Modelnya bisa sangat besar dan lambat untuk diinterpretasikan jika pohon keputusan sangat banyak.
# - **Waktu komputasi lebih lama**: Untuk dataset yang sangat besar, training model bisa memakan waktu lebih lama dibandingkan algoritma lain yang lebih sederhana.
# 
# ---
# 
# #### 2. **Support Vector Classifier (SVC)**
# 
# **Pengertian**:
# - **Support Vector Classifier (SVC)** adalah algoritma klasifikasi berbasis **Support Vector Machine (SVM)** yang berfokus pada mencari **hyperplane terbaik** yang memisahkan kelas-kelas dengan margin yang paling lebar.
# - SVC mencoba memaksimalkan margin antara dua kelas dengan memilih titik data yang paling dekat dengan hyperplane sebagai **support vectors**.
# 
# **Cara Kerja**:
# - SVC memetakan data ke ruang fitur yang lebih tinggi jika perlu, menggunakan kernel trick untuk menangani data non-linear.
# - Algoritma ini berusaha menemukan **hyperplane** yang memaksimalkan margin antara dua kelas.
# 
# **Kelebihan**:
# - **Kinerja tinggi pada data non-linear**: SVC sangat efektif dalam menangani data non-linear dengan menggunakan kernel trick.
# - **Peningkatan akurasi**: Dapat memberikan hasil yang sangat baik, terutama pada dataset yang kompleks.
# - **Dapat menangani data dengan dimensi tinggi**: SVC bekerja dengan baik pada dataset dengan banyak fitur.
# 
# **Kekurangan**:
# - **Pemilihan kernel yang tepat**: Memilih kernel yang tepat bisa menjadi tantangan. Kernel yang salah dapat mengurangi kinerja model.
# - **Waktu komputasi lama**: SVC cenderung lebih lambat pada dataset yang sangat besar atau dengan banyak fitur.
# - **Kurang efisien untuk dataset besar**: Memerlukan banyak waktu untuk memproses dataset yang sangat besar.
# 
# ---
# 
# #### 3. **Gradient Boosting Classifier**
# 
# **Pengertian**:
# - **Gradient Boosting** adalah algoritma ensemble learning yang menggabungkan beberapa model **weak learners** (biasanya pohon keputusan kecil) dengan tujuan meningkatkan akurasi prediksi. 
# - Algoritma ini bekerja dengan membangun pohon keputusan secara berurutan, di mana setiap pohon baru mengoreksi kesalahan yang dilakukan oleh pohon sebelumnya.
# 
# **Cara Kerja**:
# - Pada setiap iterasi, **model baru** dibangun untuk mengurangi **error residual** dari model sebelumnya. 
# - Proses ini mengoptimalkan **loss function** dengan cara menggunakan gradien untuk memperbaiki kesalahan secara bertahap.
# - **Learning rate** dan jumlah pohon (estimators) adalah parameter penting dalam mengontrol kompleksitas model.
# 
# **Kelebihan**:
# - **Akurat**: Gradient Boosting sering memberikan hasil yang sangat baik dan lebih akurat dibandingkan dengan model lain, terutama dalam kompetisi data science.
# - **Dapat menangani data kompleks**: Berfungsi dengan baik untuk data dengan hubungan non-linear dan fitur yang sangat banyak.
# - **Fleksibel**: Dapat digunakan dengan berbagai jenis model dasar (misalnya pohon keputusan, regresi, dll.).
# 
# **Kekurangan**:
# - **Overfitting**: Jika tidak dikontrol dengan baik, Gradient Boosting dapat mengalami overfitting, terutama dengan data yang berisik atau terlalu banyak pohon.
# - **Waktu komputasi**: Algoritma ini lebih lambat dibandingkan dengan algoritma lain seperti Random Forest karena model dibangun secara berurutan.
# - **Memerlukan tuning**: Performa algoritma sangat bergantung pada pemilihan hyperparameter (seperti jumlah pohon dan learning rate), yang memerlukan tuning yang hati-hati.
# 
# ---
# 
# ### Kesimpulan
# 
# Ketiga algoritma yang digunakan — **Random Forest**, **SVC**, dan **Gradient Boosting**, masing-masing memiliki keunggulan dan kelemahan yang berbeda:
# 
# - **Random Forest** lebih mudah digunakan dan robust terhadap overfitting, cocok untuk dataset besar dan kompleks.
# - **SVC** bekerja sangat baik pada dataset non-linear dengan margin yang jelas antara kelas, tetapi lebih lambat pada dataset besar.
# - **Gradient Boosting** sangat akurat dan fleksibel, tetapi memerlukan tuning parameter yang cermat dan dapat lebih lambat pada data besar.
# 
# Pemilihan algoritma terbaik bergantung pada sifat dataset dan masalah yang dihadapi, serta pada waktu komputasi yang tersedia.
# 

# %% [markdown]
# ## **Evaluation**

# %%
# Evaluasi masing-masing model
rf_accuracy_cv, rf_f1_cv, rf_execution_time = evaluate_model_with_cv(rf_classifier, X_resampled, y_resampled, "Random Forest")
svc_accuracy_cv, svc_f1_cv, svc_execution_time = evaluate_model_with_cv(svc_classifier, X_resampled, y_resampled, "SVC")
gb_accuracy_cv, gb_f1_cv, gb_execution_time = evaluate_model_with_cv(gb_classifier, X_resampled, y_resampled, "Gradient Boosting")

# Menampilkan hasil ringkasan evaluasi
summary_table = pd.DataFrame({
    "Model": ["Random Forest", "SVC", "Gradient Boosting"],
    "Cross-Val Accuracy": [rf_accuracy_cv, svc_accuracy_cv, gb_accuracy_cv],
    "Cross-Val F1-Score": [rf_f1_cv, svc_f1_cv, gb_f1_cv],
    "Execution Time (seconds)": [rf_execution_time, svc_execution_time, gb_execution_time]
})

print("\nSummary of Cross-Validation Results:\n")
print(summary_table)

# %%
# Prediksi pada data uji
start_time_rf = time.time()  # Mencatat waktu mulai untuk Random Forest
rf_pred = rf_classifier.predict(X_test)
rf_end_time = time.time()  # Mencatat waktu selesai untuk Random Forest

start_time_svc = time.time()  # Mencatat waktu mulai untuk SVC
svc_pred = svc_classifier.predict(X_test)
svc_end_time = time.time()  # Mencatat waktu selesai untuk SVC

start_time_gb = time.time()  # Mencatat waktu mulai untuk Gradient Boosting
gb_pred = gb_classifier.predict(X_test)
gb_end_time = time.time()  # Mencatat waktu selesai untuk Gradient Boosting

# Fungsionalitas untuk mengevaluasi model
def evaluate_model(y_true, y_pred, model_name):
    print(f"\n{model_name} Classification Report")
    print(classification_report(y_true, y_pred, digits=4))  # Menampilkan classification report
    cm = confusion_matrix(y_true, y_pred)  # Menghitung confusion matrix
    return cm

# Melakukan evaluasi model
rf_cm = evaluate_model(y_test, rf_pred, "Random Forest")
svc_cm = evaluate_model(y_test, svc_pred, "SVC")
gb_cm = evaluate_model(y_test, gb_pred, "Gradient Boosting")

# Fungsi untuk plotting confusion matrix
def plot_confusion_matrix(cm, title):
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=True, yticklabels=True)  # Membuat heatmap confusion matrix
    plt.title(title)
    plt.ylabel('True Labels')
    plt.xlabel('Predicted Labels')
    plt.show()

# Plot confusion matrices untuk masing-masing model
plot_confusion_matrix(rf_cm, "Random Forest Confusion Matrix")
plot_confusion_matrix(svc_cm, "SVC Confusion Matrix")
plot_confusion_matrix(gb_cm, "Gradient Boosting Confusion Matrix")

# Menampilkan waktu eksekusi masing-masing model
print(f"Random Forest execution time: {rf_end_time - start_time_rf:.4f} seconds")
print(f"SVC execution time: {svc_end_time - start_time_svc:.4f} seconds")
print(f"Gradient Boosting execution time: {gb_end_time - start_time_gb:.4f} seconds")

# %% [markdown]
# ### Insight dari Evaluasi Model Klasifikasi pada Data Training dan Testing
# 
# Pada proyek ini, tiga algoritma klasifikasi telah dievaluasi menggunakan **training** dan **testing** data. Berikut adalah insight yang diperoleh dari hasil **classification report** serta waktu eksekusi masing-masing model, baik untuk data training maupun testing.
# 
# ---
# 
# #### 1. **Random Forest Classifier**
# 
# - **Training**:
#   - **Cross-Val Accuracy**: 1.0000
#   - **Cross-Val F1-Score**: 1.0000
#   - **Classification Report**:
#     - **Precision**: 1.00 untuk semua kelas (Baik, Sangat Tidak Sehat, Sedang, Tidak Sehat).
#     - **Recall**: 1.00 untuk semua kelas, menunjukkan bahwa model berhasil mengidentifikasi seluruh contoh untuk setiap kelas.
#     - **F1-Score**: 1.00 untuk semua kelas, menunjukkan keseimbangan yang sangat baik antara precision dan recall.
#   - **Execution Time** (Training): 7.9813 seconds
# 
# - **Testing**:
#   - **Execution Time** (Testing): 0.0285 seconds
#   - **Classification Report**:
#     - **Precision**: 1.00 untuk semua kelas.
#     - **Recall**: 1.00 untuk semua kelas.
#     - **F1-Score**: 1.00 untuk semua kelas.
#   - **Insight**: **Random Forest** menunjukkan **kinerja sempurna** pada **data training** dan **data testing** dengan waktu eksekusi yang sangat cepat pada data testing (0.0246 detik).
# 
# ---
# 
# #### 2. **Support Vector Classifier (SVC)**
# 
# - **Training**:
#   - **Cross-Val Accuracy**: 0.9714
#   - **Cross-Val F1-Score**: 0.9713
#   - **Classification Report**:
#     - **Precision**: 0.95 untuk **Baik**, 0.98 untuk **Sangat Tidak Sehat**, dan 0.99 untuk **Sedang** dan  0.98 untuk **Tidak Sehat**.
#     - **Recall**: 1.00 untuk **Baik** dan **Sangat Tidak Sehat**, 0.93 untuk **Sedang**, dan 0.98 untuk **Tidak Sehat**.
#     - **F1-Score**: 0.97 untuk **Baik**, 0.99 untuk **Sangat Tidak Sehat**, 0.96 untuk **Sedang**, dan 0.98 untuk **Tidak Sehat**.
#   - **Execution Time** (Training): 29.6593 seconds
# 
# - **Testing**:
#   - **Execution Time** (Testing): 0.3463 seconds
#   - **Classification Report**:
#     - **Precision**: 0.6458 untuk **Baik**, 0.9348 untuk **Sangat Tidak Sehat**, 0.9979 untuk **Sedang**, dan 0.9744 untuk **Tidak Sehat**.
#     - **Recall**: 1.00 untuk **Baik**, 1.00 untuk **Sangat Tidak Sehat**, 0.9178 untuk **Sedang**, dan 0.9871 untuk **Tidak Sehat**.
#     - **F1-Score**: 0.7848 untuk **Baik**, 0.9663 untuk **Sangat Tidak Sehat**, 0.9562 untuk **Sedang**, dan 0.9807 untuk **Tidak Sehat**.
#   - **Insight**: **SVC** menunjukkan performa yang sangat baik, namun sedikit lebih lambat dalam waktu eksekusi pada **data testing** dibandingkan dengan **Random Forest**. Precision dan recall untuk **Sangat Tidak Sehat** dan **Tidak Sehat** sangat baik.
# 
# ---
# 
# #### 3. **Gradient Boosting Classifier**
# 
# - **Training**:
#   - **Cross-Val Accuracy**: 1.0000
#   - **Cross-Val F1-Score**: 1.0000
#   - **Classification Report**:
#     - **Precision**: 1.00 untuk semua kelas (Baik, Sangat Tidak Sehat, Sedang, Tidak Sehat).
#     - **Recall**: 1.00 untuk semua kelas.
#     - **F1-Score**: 1.00 untuk semua kelas.
#   - **Execution Time** (Training): 48.2638 seconds
# 
# - **Testing**:
#   - **Execution Time** (Testing): 0.0000~ seconds
#   - **Classification Report**:
#     - **Precision**: 1.00 untuk semua kelas.
#     - **Recall**: 1.00 untuk semua kelas.
#     - **F1-Score**: 1.00 untuk semua kelas.
#   - **Insight**: **Gradient Boosting** juga menunjukkan **akurasi sempurna** pada **data testing** dan **data training**. Meskipun waktu eksekusinya lebih lama pada **data training**, waktu testing sangat cepat.
# 
# ---
# 
# ### **Summary**:
# 
# | Model                | Training Accuracy | Training F1-Score | Testing Accuracy | Testing F1-Score | Training Time (s) | Testing Time (s) |
# |----------------------|-------------------|-------------------|------------------|------------------|-------------------|------------------|
# | **Random Forest**     | 1.0000            | 1.0000            | 1.0000           | 1.0000           | 7.9813            | 0.0285           |
# | **SVC**               | 0.9714            | 0.9713            | 0.9503           | 0.9503           | 29.6592           | 0.3463           |
# | **Gradient Boosting** | 1.0000            | 1.0000            | 1.0000           | 1.0000           | 48.2638           | 0.0000           |
# 
# ### **Kesimpulan**:
# 
# - **Random Forest** dan **Gradient Boosting** menunjukkan kinerja yang sangat baik pada **data training** dan **data testing**, dengan **akurasi sempurna** pada kedua set data. **Random Forest** memiliki waktu eksekusi yang lebih cepat pada data testing, sementara **Gradient Boosting** menunjukkan waktu eksekusi lebih cepat pada data testing meskipun lebih lambat saat pelatihan.
# - **SVC** memiliki sedikit penurunan kinerja dengan **akurasi** dan **f1-score** yang sedikit lebih rendah pada data testing, tetapi masih memberikan hasil yang sangat baik. Waktu eksekusi untuk **SVC** lebih lama pada data testing dibandingkan dengan **Random Forest** dan **Gradient Boosting**.
# 
# Dengan hasil ini, **Random Forest** dipilih sebagai model terbaik karena kinerjanya yang superior dalam hal **akurasi**, **kecepatan**, dan kemampuannya untuk mengatasi kompleksitas dataset dengan lebih baik.
# 


