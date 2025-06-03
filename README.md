# Sistem Klasifikasi Kondisi Udara DKI Jakarta Menggunakan Algoritma Random Forest Dengan Synthetic Minority Oversampling Technique
Project ini dibuat untuk memenuhi Tugas Akhir dari Prodi S1 Sains Data, Universitas Teknology Yogyakarta. Hasil project ini berupa aplikasi website yang bisa memprediksi kondisi udara. Aplikasi web tersebut bisa diakses di [sini](https://app-tugas-akhir-ispu-jakarta.streamlit.app/)
- Nama            = Riyan Zaenal Arifin
- NIM             = 5201811011
- Email Institusi = riyan.5201811011@student.uty.ac.id
- Email Personal  = riyanzaenal411@gmail.com
  
## Abstrak
Kualitas udara di kota-kota besar seperti DKI Jakarta sering kali menjadi perhatian khusus oleh kalangan masyarakat dan terutama oleh pemangku kepentingan. Penelitian ini bertujuan untuk membuat sistem klasifikasi kondisi udara di DKI Jakarta menggunakan algoritma Random Forest dengan teknik sampling Synthetic Minority Over-sampling Technique (SMOTE). Algoritma Random Forest dipilih karena kemampuannya dalam menangani data berdimensi tinggi dan toleransinya terhadap overfitting. Sementara itu, teknik SMOTE digunakan untuk mengatasi masalah ketidakseimbangan kelas dalam data kualitas udara. Penelitian ini menggunakan dataset Indeks Standar Pencemaran Udara DKI Jakarta tahun 2023 sebanyak 1825 data dan 12 attribute. Proses persiapan data meliputi label selection, normalisasi data, feature selection,  hapus missing, label encoding, SMOTE, dan hapus duplikasi data. Dari proses tersebut diperoleh data sebanyak 3237 data yang balance. Data testing diambil dari dataset sebanyak 50 data untuk sampel uji model jika sudah dilakukan deployment, sedangkan sisanya digunakan untuk data training model yang menggunakan 10 fold cross validation. Hasil evaluasi metrik menunjukkan nilai accuracy, precision, recall, f1 score yang sama, yakni 100% pada setaip K di cross validation, baik evaluasi data validation maupun data training. Proses deployment menggunakan model pertama dari cross validation. Hasil model tersebut memiliki performa yang lebih baik dari penelitian-penelitian sebelumnya. Hal tersebut menunjukkan potensi yang bagus penggunaan algoritma Random Forest dengan SMOTE dalam pemantauan dan prediksi kualitas udara. Peneliti menyarankan agar membuat model deployment yang lebih kompleks, seperti terhubung dengan third-party dan menggunakan server sendiri untuk menjalakan aplikasi serta mencoba kasusnya di kota lain.

## Penjelasan Folder
### [App](https://github.com/RiyZ411/Streamlit-Tugas_Akhir/tree/main/App)
Merupakan folder untuk menyimpan kode python untuk tampilan web yang menggunakan library streamlit. selain itu, disimpan juga package-package library python yang digunakan untuk pembuatan project ini yang diambil dari virtual environment.
### [Data](https://github.com/RiyZ411/Streamlit-Tugas_Akhir/tree/main/Data)
Merupakan folder untuk menyimpan data, baik data mentah, data yang sudah melalui tahap preparation, data untuk training model, dan data untuk test model.
### [Images](https://github.com/RiyZ411/Streamlit-Tugas_Akhir/tree/main/Images)
Merupakan folder untuk menyimpan gambar dari background web.
### [Models](https://github.com/RiyZ411/Streamlit-Tugas_Akhir/tree/main/Models)
Merupakan folder untuk menyimpan model, best model dari proses cross validation, serta file jupyter notebook dari pemrosesan data hingga menjadi model.
