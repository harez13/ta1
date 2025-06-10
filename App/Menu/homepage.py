import streamlit as st
import base64


# st.set_page_config(page_title="About Me", layout="centered")
st.set_page_config(layout="wide")




# Judul utama
st.title("Dampak kesehatan dan sumber polusi udara")

# Membuat dua kolom
col1, col2 = st.columns([1, 1])

# Kolom kiri - Faktor risiko kematian
with col1:
    st.subheader("Apa faktor risiko utama kematian di seluruh dunia?")
    st.markdown("Dari 62 juta orang yang meninggal setiap tahun (sampai tahun 2021), berdasarkan faktor risiko:")

    data_risiko = [
        ("1", "Tekanan darah tinggi", "10.9M"),
        ("2", "Polusi Udara (Luar Ruangan & Dalam Ruangan)", "8.1M"),
        ("3", "Merokok", "6.2M"),
        ("4", "Gula darah tinggi", "5.3M"),
        ("5", "Polusi partikel luar ruangan", "4.7M"),
        ("6", "Kegemukan", "4.7M"),
        ("7", "Kolesterol tinggi", "3.6M"),
        ("8", "Polusi udara dalam ruangan", "3.1M"),
        ("9", "Diet tinggi natrium", "1.9M"),
        ("10", "Konsumsi alkohol", "1.8M"),
        ("11", "Diet rendah buah", "1.7M"),
        ("12", "Diet rendah biji-bijian utuh", "1.5M"),
        ("13", "Berat badan lahir rendah", "1.5M"),
        ("14", "Asap rokok", "1.3M"),
    ]

    st.markdown("###")
    for i, faktor, jumlah in data_risiko:
        highlight = faktor.lower().startswith("all") or faktor.lower() == "kenapa"
        st.markdown(f"<div style='padding:4px; background-color:{'#E6F0FA' if highlight else 'transparent'}'>"
                    f"<strong>{i}.</strong> {faktor} <span style='float:right'>{jumlah}</span></div>",
                    unsafe_allow_html=True)

    st.caption("Sumber: [IHME, Global Burden of Disease (2024)](https://www.healthdata.org/research-analysis/gbd)")

# Kolom kanan - Sumber Polusi PM2.5
with col2:
    st.subheader("Sumber Utama Polusi PM2.5")
    st.markdown("""
    Karena PM2.5, partikel debu halus dengan diameter hingga 2.5 mikrometer, dapat menembus jauh ke dalam paru-paru dan masuk ke aliran darah, 
    maka partikel ini menimbulkan risiko kesehatan yang signifikan. Sumbernya sangat bervariasi menurut lokasi, tetapi berikut ini adalah 
    sumber yang paling umum di seluruh dunia.
    """)

    sumber_pm25 = [
        ("🔥", "Pembakaran batu bara"),
        ("⛽", "Pembakaran bensin"),
        ("🚛", "Pembakaran diesel"),
        ("🪵", "Pembakaran kayu"),
        ("🏍️", "Pembakaran motor"),
        ("🏭", "Proses industri"),
        ("🔥", "Kebakaran"),
        ("🔁", "Konversi gas menjadi partikel"),
    ]

    cols = st.columns(2)
    for i, (ikon, nama) in enumerate(sumber_pm25):
        with cols[i % 2]:
            st.markdown(f"<div style='padding:12px; border:1px solid #ccc; border-radius:8px; margin-bottom:8px;'>"
                        f"<h3 style='margin:0'>{ikon}</h3><p style='margin:0'>{nama}</p></div>", unsafe_allow_html=True)

    st.caption("Sumber: [AQMD Community in Action Guidebook](https://www.aqmd.gov/docs/default-source/aq-spec/star-grant/community-in-action-guidebook-on-air-quality-sensors-%28appendices-only%29.pdf)")


st.markdown("---")
st.subheader("Bagaimana polusi udara memengaruhi anak-anak?")

# Bagian atas: dampak terhadap anak-anak
col_a1, col_a2, col_a3 = st.columns(3)

with col_a1:
    st.markdown("### Masalah pernapasan")
    st.write("Meningkatnya kasus asma dan bronkitis")

with col_a2:
    st.markdown("### Penurunan fungsi paru-paru")
    st.write("Paparan jangka panjang dapat mengganggu perkembangan paru-paru")

with col_a3:
    st.markdown("### Perkembangan kognitif")
    st.write("Dampak potensial terhadap perkembangan otak dan prestasi akademik")

st.caption("Sumber: [EEA (European Environment Agency)](https://www.eea.europa.eu/en)")

# Bagian bawah: statistik global
st.markdown("###")
col_b1, col_b2, col_b3 = st.columns(3)

with col_b1:
    st.markdown("### 99%")
    st.write("Populasi dunia tinggal di tempat-tempat yang kualitas udaranya melampaui batas pedoman tahunan WHO.")
    st.caption("Sumber: [World Health Organization](https://www.who.int)")

with col_b2:
    st.markdown("### 8,1 Juta")
    st.write("Kematian di seluruh dunia dapat disebabkan oleh polusi udara.")
    st.markdown("""
    - **4,7 juta**  
      Karena polusi udara partikulatif luar ruangan  
    - **3,1 juta**  
      Karena polusi udara dalam ruangan  
    - **0,5 juta**  
      Karena polusi ozon luar ruangan  
    """)
    st.caption("Sumber: [Health Effects Institute 2021 - Numbers for 2021](https://www.healtheffects.org/annual-report-2021)")

with col_b3:
    st.markdown("### 100/100,000")
    st.write("Orang-orang di seluruh dunia meninggal karena polusi udara.")
    st.markdown("""
    - **58/100,000**  
      Dari partikel luar ruangan  
    - **39/100,000**  
      Dari polusi udara dalam ruangan  
    - **6/100,000**  
      Dari polusi ozon luar ruangan  
    """)
    st.caption("Sumber: [IHME (Institute for Health Metrics and Evaluation) 2024](https://www.healthdata.org/)")

st.markdown("---")
st.markdown("#### Apa yang menyebabkan kualitas udara buruk?")
st.markdown(""" 
Polusi udara berasal dari sumber alami maupun buatan manusia.
Sumber alami mencakup debu, tanah, pasir yang terbawa angin, asap gunung berapi, dan material yang terbakar.
Sumber buatan manusia—seperti kendaraan bermotor, pembangkit listrik, pabrik, pembakaran bahan bakar, dan kegiatan pertanian—merupakan penyebab utama polusi udara di kota-kota dan lebih mudah dikendalikan melalui peraturan.

Kontribusi tiap sumber polusi berbeda-beda tergantung lokasi dan kebijakan setempat. Setiap wilayah memiliki campuran penyebab dan jenis polutannya sendiri, yang umumnya dikelompokkan sebagai berikut:
""")

st.markdown("###### Industri")
st.markdown(""" 
Industri mencakup polusi dari fasilitas seperti pabrik manufaktur, pertambangan, dan kilang minyak serta pembangkit listrik tenaga batu bara dan boiler untuk pembangkitan panas dan listrik.

Aktivitas industri merupakan sumber global utama nitrogen oksida (NOx), hidrogen sulfida, senyawa organik yang mudah menguap (VOC), dan materi partikulat, yang semuanya berkontribusi terhadap ozon dan kabut asap.
""")

st.markdown("###### Pertanian")
st.markdown(""" 
Penggunaan pupuk yang berlebihan di lahan pertanian merupakan salah satu penyumbang polusi udara partikulat halus yang signifikan. 
Sebuah studi dalam Geophysical Research Letters menemukan bahwa polusi yang dihasilkan dari pertanian lebih besar daripada semua sumber PM buatan manusia lainnya di sebagian besar wilayah Amerika Serikat, Eropa, Rusia, dan Cina.

Secara global, penggunaan lahan pertanian meningkat karena meningkatnya permintaan produk hewani dan makanan per kapita.
""")

st.markdown("###### Mengangkut")
st.markdown(""" 
Polusi udara dari transportasi terutama mengacu pada pembakaran bahan bakar pada kendaraan bermotor, seperti mobil, truk, kereta api, pesawat terbang, dan kapal. 
Emisi transportasi merupakan penyumbang utama meningkatnya kadar partikel halus (PM2.5), ozon, dan nitrogen dioksida (NO2).

Mayoritas emisi dari transportasi terjadi di pasar kendaraan teratas dunia, karena cenderung ada korelasi kuat antara emisi transportasi per kapita dan pendapatan.
Seiring meningkatnya standar hidup dan aktivitas ekonomi, demikian pula permintaan akan transportasi.
""")

st.markdown("###### Sumber alami")
st.markdown(""" 
Sumber polusi udara alami mencakup fenomena yang terjadi secara alami seperti aktivitas gunung berapi, kebakaran hutan, dan badai debu atau pasir. 
Dampak sumber alami terhadap kualitas udara sangat bergantung pada lingkungan setempat. 
Misalnya, lokasi di dekat gurun besar seperti Sahara sangat terpengaruh oleh debu dan pasir yang tertiup angin, sementara lokasi hutan lebih mungkin mengalami polusi udara akibat kebakaran hutan.
""")

st.markdown("###### Rumah tangga")
st.markdown(""" 
Polusi udara rumah tangga mengacu pada aktivitas pribadi, seperti memasak dan memanaskan rumah dengan pembakaran batu bara atau kayu serta pembangunan dan konstruksi rumah dan perabotan.
""")

st.markdown("###### Kebakaran hutan dan pembakaran terbuka")
st.markdown(""" 
Pembakaran bahan tanaman mengeluarkan sejumlah besar polutan, seperti halnya pembakaran bahan bakar padat lainnya seperti batu bara. 
Pembakaran bahan organik mengeluarkan partikel (PM), nitrogen oksida (NOx), karbon monoksida (CO), sulfur dioksida SO2), timbal, merkuri, dan polutan udara berbahaya (HAP) lainnya. Kebakaran ini dapat terjadi secara organik, tidak sengaja, atau disengaja. 
Karena kebakaran ini sering kali terjadi dalam skala besar, kebakaran hutan dan pembakaran terbuka berpotensi menyebabkan polusi udara yang luas.""")

st.markdown("#### Bisakah polusi udara menyebabkan masalah kesehatan?")
st.markdown("""
Polusi udara mengacu pada zat-zat di udara yang merugikan kesehatan manusia dan/atau planet secara keseluruhan. 
Pada tingkat yang signifikan, semua jenis polusi udara menimbulkan risiko efek kesehatan yang merugikan.
Besarnya risiko komplikasi kesehatan bergantung pada kesehatan seseorang secara keseluruhan, jenis polutan, konsentrasi, dan lamanya paparan udara yang tercemar.
""")

st.markdown("##### Dampak menghirup udara yang tidak sehat - gambaran umum:")
st.markdown("""
Organisasi Kesehatan Dunia (WHO) telah menganggap polusi udara sebagai risiko kesehatan lingkungan terbesar pada tahun 2019, yang diperkirakan berkontribusi terhadap 7 juta kematian dini setiap tahunnya. 
Di antara anak-anak di bawah usia 15 tahun, polusi udara merupakan penyebab kematian utama, yang menewaskan 600.000 orang setiap tahunnya.

Polusi udara digambarkan sebagai ‘pembunuh diam-diam’ karena jarang menjadi penyebab langsung kematian. 
Sebaliknya, polusi udara merupakan penyebab kematian dini terbesar ke-4 di dunia, yang meliputi:
- 29% dari seluruh kematian dan penyakit disebabkan oleh kanker paru-paru
- 17% dari seluruh kematian dan penyakit disebabkan oleh infeksi saluran pernapasan bawah akut
- 24% dari seluruh kematian akibat stroke
- 25% dari seluruh kematian dan penyakit disebabkan oleh penyakit jantung koroner
- 43% dari seluruh kematian dan penyakit disebabkan oleh penyakit paru obstruktif kronik

Diperkirakan 99% dari populasi global menghirup udara yang tidak sehat. 
Meskipun angka ini bervariasi di tiap wilayah, tidak ada satu pun yang bebas dari risiko. 
[Laporan Kualitas Udara Dunia tahun 2024](https://www.iqair.com/id/world-air-quality-report) menemukan bahwa 91% dari 138 negara dan wilayah di seluruh dunia melampaui nilai pedoman PM2.5 tahunan WHO sebesar 5 µg/m3, dengan wilayah Asia Tengah & Selatan di antara sepuluh kota paling tercemar di dunia.
""")

st.markdown("##### Tingkat polusi udara yang tinggi dapat menyebabkan masalah kesehatan termasuk:")
st.markdown("""
- Efek jangka pendek: kesulitan bernapas, nyeri dada, mengi, batuk, ketidaknyamanan pernapasan umum, dan iritasi mata, hidung, dan tenggorokan.  
- Efek jangka panjang: kerusakan jaringan paru-paru, kanker, kematian dini, dan perkembangan penyakit pernapasan seperti asma, bronkitis, dan emfisema.
""")

st.markdown("##### Kelompok yang paling rentan terhadap dampak kesehatan buruk akibat polusi udara meliputi:")
st.markdown("""
- Penyakit jantung, seperti penyakit arteri koroner (CAD) atau gagal jantung kongestif  
- Penyakit paru-paru, seperti asma, emfisema, atau penyakit paru obstruktif kronik (PPOK)  
- Orang lanjut usia dan orang lanjut usia  
- Anak-anak di bawah usia 14 tahun  
- Wanita hamil  
- Pekerja luar ruangan  
- Atlet yang berolahraga di luar ruangan dengan giat
""")

st.markdown("##### Dampak kesehatan akibat polutan udara tertentu")

# Buat tabel 3 kolom seperti pada gambar
col1, col2, col3 = st.columns([1, 1.2, 1.2])

with col1:
    st.markdown("###### Ozon Tingkat Dasar")
    st.markdown("""
    - Penurunan fungsi paru-paru  
    - Asma yang memburuk  
    - Iritasi tenggorokan dan hidung  
    - Nyeri dada dan sesak napas  
    - Gejala mirip flu  
    - Kematian dini  
    - Kerentanan tinggi terhadap infeksi pernapasan  
    """)

with col2:
    st.markdown("###### Partikel Materi (PM) dan Asap Kebakaran Hutan")
    st.markdown("**Jangka pendek**")
    st.markdown("""
    - Detak jantung tidak teratur  
    - Nyeri dada  
    - Batuk  
    - Iritasi pada mata, hidung, dan tenggorokan  
    - Asma yang memburuk  
    - Penurunan fungsi paru-paru  
    """)

with col3:
    st.markdown("###### Partikel Materi (PM) dan Asap Kebakaran Hutan")
    st.markdown("**Jangka panjang**")
    st.markdown("""
    - Kerusakan jaringan paru-paru  
    - Kanker  
    - Perkembangan penyakit pernapasan seperti asma, bronkitis, dan emfisema  
    - Kematian dini  
    """)

st.markdown("##### Bagaimana saya bisa melindungi diri dari polusi udara?")

st.markdown("###### Bagaimana saya dapat meningkatkan kualitas udara di rumah saya?")
st.markdown("""
Kualitas udara dalam ruangan tidak aman dari polusi udara luar ruangan. Selain itu, ada banyak sumber emisi khusus untuk lingkungan dalam ruangan yang dapat menyebabkan peningkatan tingkat polusi udara dalam ruangan. Untuk meningkatkan kualitas udara di rumah, ventilasi dalam ruangan dan sumber dalam ruangan harus dikelola.
""")

st.markdown("###### Metode mitigasi polusi udara dalam ruangan meliputi:")
st.markdown("""
- Periksa tingkat kualitas udara terkini dan prakiraan di wilayah Anda. Ikuti anjuran kesehatan untuk kondisi terkini.  
- Tutup jendela dan pintu. Tutup rapat celah-celah pintu dan jendela untuk meminimalkan kebocoran udara.  
- Bila udara luar sangat tercemar, atur sistem pendingin udara (HVAC) dengan pemasukan udara segar ke mode resirkulasi.  
- Gunakan pembersih udara atau filter HVAC efisiensi tinggi (seperti filter HEPA atau HyperHEPA) untuk menghilangkan polutan halus dari udara.
""")

st.markdown("###### Jika tingkat polusi udara dalam ruangan sudah sangat tinggi:")
st.markdown("""
- Hindari aktivitas berat, seperti berolahraga, untuk mengurangi jumlah polusi udara yang Anda hirup.  
- Gunakan masker polusi N95, jika tersedia.  
- Hindari penggunaan produk rumah tangga selama polusi udara sangat tinggi.  
- Jalankan pembersih udara secara berkala pada pengaturan output tertinggi.  
- Ketahui peringatan kualitas udara ketika polusi udara ruangan menjadi “berbahaya” yang dapat terjadi jika terjadi kebakaran hutan di dekatnya.
""")

st.markdown("###### Bagaimana masker dapat melindungi dari polusi udara?")
st.markdown("""
Masker sangat efektif dalam mengurangi paparan polusi udara. Sementara kategori masker polusi udara yang umum mencakup masker untuk menangani bahan kimia yang berasal dari pembakaran, sebagian besar tersedia di pasaran hanya bekerja untuk partikel dan polutan kecil.  

Untuk penggunaan sehari-hari, masker dengan filter partikel udara yang halus cocok untuk orang yang mengalami gas pada tingkat bahaya sedang atau tinggi. Masker berkualitas tinggi bisa membantu melindungi seseorang dari PM2.5, virus, bakteri, dan alergen.  

**Dalam mengevaluasi efektivitas masker polusi, tiga komponen harus dievaluasi:** filter polusi, segel masker, dan ventilasi.
- Filter polusi: Filter polusi biasanya diberi peringkat N90, N95, N99, atau N100. Peringkat tersebut menyatakan persentase partikel (> 0,3 µg) yang dapat diblokir oleh masker. Misalnya, masker N95 memblokir 95% partikel yang lebih besar dari 0,3 mikrogram. Ini termasuk sebagian besar PM2,5 dan PM10. Semakin tinggi peringkatnya, semakin efektif filter masker, dengan asumsi segel masker dan komponen ventilasi berfungsi dengan baik.
- Segel masker: Terlepas dari peringkat filter polusi masker, masker yang tidak menutup rapat wajah tidak efektif karena udara akan mengalir masuk tanpa disaring melalui sisi-sisi masker. Segel masker yang baik akan menyebabkan masker tersedot ke wajah saat terhirup. Untuk masker sekali pakai yang fleksibel, isapan ini harus terlihat, yang menyebabkan filter tertekuk ke dalam sehingga menciptakan permukaan cekung. Untuk masker dengan konstruksi yang lebih kokoh, tekanan yang sedikit meningkat saat menghirup udara seharusnya dapat dirasakan. Jika masker tidak tertutup rapat di wajah, udara akan mengalir masuk melalui sisi-sisi masker yang terbuka.
- Ventilasi (katup CO2): Ventilasi membuat masker lebih mudah bernapas sekaligus mengurangi kelembapan dan akumulasi CO2. Meskipun bukan fitur semua masker, banyak yang menggunakan katup CO2 seukuran koin untuk memberikan aliran keluar yang terarah. Menghirup udara yang berventilasi buruk dengan kadar CO2 yang tinggi dapat menyebabkan efek jangka pendek seperti sakit kepala, lesu, pusing, dan mual. ​​Masker dengan katup ventilasi tidak efektif untuk mengurangi penyebaran virus, karena keluaran pernapasan tidak tersaring.

Masker bedah sekali pakai terjangkau dan mudah didapat. Masker ini juga sangat efektif terhadap polusi partikel. Sebuah studi di Edinburgh yang dilakukan oleh Particle and Fiber Toxicology menguji masker bedah hingga 0,007 µg dan menemukan bahwa bahan masker bedah mampu memblokir 80% partikel.

Dalam studi lain, uji kecocokan diterapkan pada masker bedah untuk menguji efektivitasnya secara lebih akurat, dengan memperhatikan kecocokan yang umumnya longgar. Dalam pengujian ini, tingkat penyaringan turun hingga 63% akibat kebocoran di sekitar masker.

Walaupun kedua pengujian tersebut mengungkap bahwa masker bedah secara signifikan kurang efisien dibandingkan masker respirator (dengan peringkat N90-N100), masker bedah membantu mengurangi paparan polusi partikulat halus dengan biaya yang sangat rendah.
""")


# Fungsi untuk konversi gambar ke base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ganti dengan nama file gambar kamu
bg_image = get_base64_of_bin_file("Images/tom-barrett--bSucp2nUdQ-unsplash (1).jpg")

# CSS: gambar latar belakang hanya untuk konten utama (.main), tanpa mengubah elemen lain
st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("data:image/jpg;base64,{bg_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            opacity: 0.8;
        }}
    </style>
    """,
    unsafe_allow_html=True
)