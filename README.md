# Indonesia Economic Intelligence

**Indonesia Economic Risk & Household Cost Monitor**  
*Kerangka pemantauan historis: 2016–2026 · Horizon skenario: 2027–2030*

Proyek dashboard publik dan independen untuk mengeksplorasi bagaimana risiko geopolitik dan ekonomi eksternal dapat merambat ke perekonomian Indonesia, harga kebutuhan dasar, biaya hidup, serta daya beli rumah tangga.

> **Penting:** Proyek ini merupakan alat analisis dan edukasi independen, bukan publikasi resmi Pemerintah Indonesia, Bank Indonesia, BPS, PLN, World Bank, atau lembaga penyedia data lainnya. Data historis, peristiwa kebijakan, interpretasi analitis, dan asumsi skenario dipisahkan secara eksplisit. Nilai skenario bukan forecast resmi.

## Website publik

Setelah GitHub Pages aktif, ganti placeholder berikut dengan URL yang ditampilkan pada **Repository → Settings → Pages**:

- **Website:** `https://<USERNAME>.github.io/<REPOSITORY>/`

Navigasi utama:

| Halaman | File | Isi |
|---|---|---|
| Ringkasan proyek | [`index.html`](index.html) | Konteks, kerangka analisis, sumber data, asumsi, dan navigasi dashboard |
| Indonesia Economic Risk Dashboard | [`dashboard.html`](dashboard.html) | Kerangka indikator risiko makro dan stress test 2027–2030 |
| Household Cost & Basic Needs Dashboard | [`dashboard-mikro.html`](dashboard-mikro.html) | Harga BBM, tarif PLN per golongan rumah tangga, database harga pangan, Susenas, dan simulator biaya |

## Tujuan dan ruang lingkup

Proyek ini menghubungkan risiko eksternal dengan konsekuensi ekonomi domestik melalui jalur transmisi berikut:

**Guncangan geopolitik dan pasokan → pasar komoditas, energi, dan freight global → kondisi eksternal dan fiskal Indonesia → harga domestik → pengeluaran dan daya beli rumah tangga.**

Diskusi geopolitik digunakan sebagai konteks analisis risiko. Proyek ini tidak menyatakan bahwa suatu hasil geopolitik, motif politik, atau peristiwa masa depan tertentu pasti terjadi.

### 1. Kerangka risiko makroekonomi

Dashboard makro mengelompokkan pemantauan ke dalam enam area:

1. **Geopolitik dan pertahanan** — risiko keamanan, belanja pertahanan, dan kemungkinan trade-off fiskal.
2. **Energi** — harga minyak mentah, impor minyak dan LPG, subsidi dan kompensasi energi, serta risiko pasokan.
3. **Perdagangan** — neraca perdagangan barang dan migas, biaya impor, ketergantungan komoditas, dan ketahanan eksternal.
4. **Fiskal** — defisit APBN, utang pemerintah, subsidi, kompensasi, dan ruang fiskal.
5. **Kondisi eksternal dan keuangan** — nilai tukar rupiah, cadangan devisa, arus modal, dan kondisi pendanaan.
6. **Ekonomi riil** — pertumbuhan PDB, inflasi, konsumsi, dan kesejahteraan rumah tangga.

Dashboard makro memuat lintasan **worst-case stress test 2027–2030** berikut. Angka-angka ini adalah paket asumsi kondisional untuk menguji ketahanan terhadap tekanan energi, perdagangan, fiskal, dan eksternal. Angka tersebut bukan prediksi dasar dan bukan probabilitas kejadian.

| Indikator | Satuan | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Belanja pertahanan | % PDB | 1,15 | 1,30 | 1,50 | 1,70 |
| ICP | US$/barel | 105 | 120 | 125 | 110 |
| Neraca perdagangan migas | US$ miliar | -25 | -27 | -30 | -27 |
| Neraca perdagangan barang | US$ miliar | +8 | -5 | -18 | -10 |
| Utang pemerintah (lintasan skenario) | % PDB | 43,5 | 46,2 | 49,0 | 51,5 |
| Defisit APBN | % PDB | 2,9 | 3,0 | 3,0 | 2,8 |
| Nilai tukar USD/IDR | Rp per US$ | 19.000 | 21.500 | 24.000 | 26.000 |
| Cadangan devisa | US$ miliar | 135 | 120 | 105 | 95 |
| Pertumbuhan PDB riil | % | 3,8 | 2,0 | -1,5 | 0,5 |
| Inflasi CPI | % | 5,0 | 7,5 | 9,0 | 6,5 |

Lintasan ini harus diuji ulang menggunakan data resmi yang relevan dan asumsi yang diperbarui sebelum dipakai sebagai dasar keputusan.

### 2. Biaya kebutuhan dasar dan paparan rumah tangga

Dashboard mikro berfokus pada saluran biaya yang paling dekat dengan anggaran rumah tangga:

- **Pangan:** beras, telur, cabai, minyak goreng, gula, serta komoditas lain yang tersedia dalam seri harga.
- **Listrik:** tarif menurut golongan pelanggan, kelas daya, status subsidi/nonsubsidi, dan tanggal berlaku.
- **BBM:** harga menurut jenis produk dan wilayah. Harga satu produk atau satu wilayah tidak otomatis mewakili harga nasional.
- **LPG:** LPG 3 kg bersubsidi, HET daerah, harga agen, harga eceran, serta LPG nonsubsidi harus dibedakan.
- **Pengeluaran nonpangan:** perumahan, kesehatan, pendidikan, dan kelompok pengeluaran lain.
- **Paparan rumah tangga:** porsi pengeluaran dan kuantitas konsumsi, dengan memanfaatkan data Susenas jika seri yang sebanding tersedia.

Simulator rumah tangga di dashboard mikro merupakan **alat sensitivitas ilustratif**. Nilai pengeluaran awal, porsi anggaran, dan laju kenaikan biaya dapat diubah pengguna. Nilai default bukan rata-rata rumah tangga, kelompok desil, atau proyeksi resmi BPS.

Salah satu lintasan stress biaya yang dibahas menggunakan asumsi inflasi tahunan 5,0% (2027), 7,5% (2028), 9,0% (2029), dan 6,5% (2030). Secara majemuk, lintasan ini setara dengan kenaikan tingkat harga sekitar 31% dari akhir 2026 hingga 2030. Ini adalah ilustrasi skenario, bukan forecast resmi dan bukan pengganti penghitungan berdasarkan keranjang konsumsi aktual.

## Household Energy Dataset — BBM dan tarif PLN

Dashboard mikro memuat dua dataset energi rumah tangga yang disimpan sebagai arsip gzip berformat Base64 text agar dapat ditangani GitHub Contents API sebagai file teks:

- [Arsip harga BBM rumah tangga](bbm_household_prices.csv.gz.b64): 49 snapshot harga — Premium (5), Pertalite (17), dan Pertamax (27).
- [Arsip tarif PLN rumah tangga](pln_household_tariffs.csv.gz.b64): 71 catatan tarif untuk tujuh kelompok rumah tangga, dari 450 VA hingga 6.600 VA ke atas.

Halaman dashboard mendekompresi kedua arsip di browser modern melalui `DecompressionStream('gzip')`. Tombol unduh pada masing-masing bagian menghasilkan file CSV biasa. File sumber menyimpan tanggal/presisi tanggal, jenis produk atau golongan, harga/tarif, wilayah acuan, nama sumber, URL, dan catatan metodologi.

### Metodologi BBM

Harga adalah snapshot yang dilaporkan oleh sumber, bukan observasi harian atau bulanan lengkap. Harga Pertamax dapat berbeda antarwilayah. Sebagian nilai historis berasal dari tabel retrospektif media dengan presisi bulan dan/atau wilayah yang tidak dirinci. Karena itu dashboard menampilkan titik data tanpa menghubungkannya menjadi tren kontinu. Premium penugasan luar Jamali dibedakan dari harga di wilayah Jamali.

Sumber per baris mencakup ESDM, Sekretariat Kabinet, detikOto, Katadata, ANTARA, Kementerian PANRB, detikFinance, dan Tirto. Tautan dan cakupan wilayah tersedia pada kolom `source_name`, `source_url`, `reference_area`, dan `source_note`.

### Metodologi tarif PLN

Dataset mencakup tujuh kelompok rumah tangga: 450 VA subsidi, 900 VA subsidi, 900 VA RTM, 1.300 VA, 2.200 VA, 3.500–5.500 VA, dan ≥6.600 VA. Jenis catatan dibedakan menjadi snapshot bulanan, interval tarif efektif, skedul tarif yang dipublikasikan, dan snapshot tarif resmi terbaru.

Tarif 450 VA dan 900 VA subsidi dalam dataset merupakan referensi tarif prabayar tunggal; tarif pascabayar memakai blok pemakaian sehingga angka tunggal tidak boleh dibaca sebagai rata-rata tagihan. Snapshot bulanan yang tidak ditemukan tidak diinterpolasi. Tarif nominal juga tidak sama dengan pengeluaran listrik aktual setelah subsidi, kompensasi, diskon, dan pola konsumsi.

Semua angka dapat ditelusuri melalui URL sumber pada setiap baris. Kedua seri ini merupakan himpunan observasi terdokumentasi, bukan panel bulanan lengkap untuk seluruh jenis BBM dan golongan pelanggan.

## Food Price Database (FPDB)

Dashboard mikro membaca file lokal bernama **`fpdb.csv`** dari direktori yang sama dengan `dashboard-mikro.html`.

### Sumber data

Database ini berasal dari dataset market-level **World Bank Real Time Food Prices (RTFP) untuk Indonesia**:

- [World Bank — Katalog RTFP Indonesia](https://microdata.worldbank.org/catalog/6166)
- [World Bank — Data API dan bulk downloads](https://microdata.worldbank.org/catalog/6166/data-api)
- [World Bank — Data dictionary](https://microdata.worldbank.org/catalog/6166/data-dictionary)

Versi yang digunakan saat penyusunan dashboard tercatat bertanggal **5 Oktober 2026**, dengan rentang data **Januari 2007 sampai 1 Oktober 2026**. Katalog pada versi tersebut mencatat 222 pasar, 53.074 observasi, dan 88 variabel. Jumlah baris file lokal setelah pemangkasan akan berbeda karena hanya data 2016 ke atas dan kolom terpilih yang dipertahankan.

RTFP menggabungkan informasi harga yang diukur langsung dengan estimasi berbasis model, termasuk estimasi untuk observasi yang hilang. Data historis maupun estimasi terkini dapat diperbarui atau direvisi oleh penyedia dataset. Karena itu, RTFP harus diperlakukan sebagai sumber estimasi harga tingkat pasar, bukan sensus lengkap seluruh transaksi ritel.

### Data yang dipakai dashboard

Script `trim_fpdb.py` mempertahankan:

- Data Indonesia (`ISO3 = IDN`, jika kolom tersebut tersedia).
- Observasi mulai **1 Januari 2016**.
- Kolom tanggal dan geografi yang dibutuhkan dashboard, termasuk `price_date`, `adm1_name`, `adm2_name`, dan `mkt_name`.
- Mata uang dan sejumlah indikator cakupan/kualitas data.
- Seluruh kolom `c_*`, yaitu **close price estimates** untuk komoditas yang tersedia.

Agregasi grafik bulanan pada dashboard saat ini menggunakan **rata-rata sederhana tanpa pembobotan** atas observasi pasar yang tersedia setelah filter diterapkan. Hasil tersebut bukan indeks harga pangan nasional berbobot penduduk, bukan CPI resmi, dan bukan pengganti statistik inflasi BPS. Cakupan pasar, nilai kosong, interpolasi, dan definisi komoditas perlu dipertimbangkan ketika membandingkan hasil.

### Mengunduh dan menyiapkan `fpdb.csv`

1. Unduh arsip market-level Indonesia dari bagian **Data API → Bulk data downloads** pada katalog World Bank. Gunakan arsip Indonesia terbaru yang tersedia. Arsip yang digunakan saat penyusunan versi ini bernama `IDN_RTFP_mkt_2007_2026-10-05.zip`.

Untuk arsip 5 Oktober 2026 tersebut, unduhan dapat dilakukan dari PowerShell. **Resource ID pada URL bersifat spesifik versi; periksa katalog untuk rilis yang lebih baru.**

```powershell
curl.exe -L --fail --retry 3 `
  "https://microdata.worldbank.org/api/downloads/download/IDN_2021_RTFP_v02_M/360756?filename=IDN_RTFP_mkt_2007_2026-10-05.zip" `
  -o .\fpdb_source.zip

Expand-Archive -LiteralPath .\fpdb_source.zip -DestinationPath .\fpdb_source -Force
Get-ChildItem .\fpdb_source -Recurse -Filter *.csv
```

2. Identifikasi CSV market-level di dalam direktori hasil ekstraksi. Salin file tersebut ke direktori proyek dengan nama `fpdb.csv` (atau gunakan path aktualnya sebagai input script).
3. Jalankan script pemangkasan untuk menghasilkan dataset yang lebih ringan:

```powershell
py -3 .\trim_fpdb.py .\fpdb.csv .\fpdb_2016.csv
```

4. Ganti database aktif dengan hasil pemangkasan setelah memeriksa laporan script:

```powershell
Copy-Item .\fpdb_2016.csv .\fpdb.csv -Force
```

`trim_fpdb.py` membaca dan menulis CSV secara bertahap (streaming), sehingga tidak membutuhkan pandas. Script menghasilkan file output terpisah dan tidak menimpa file input. Simpan backup unduhan asli sebelum mengganti `fpdb.csv` aktif.

### Memperbarui database

Ketika rilis RTFP baru tersedia:

1. Unduh dan ekstrak arsip market-level Indonesia terbaru.
2. Simpan unduhan asli sebagai backup dengan identitas versi/tanggal.
3. Jalankan `trim_fpdb.py` terhadap CSV sumber yang baru.
4. Periksa laporan script: jumlah baris input/output, kolom yang dipertahankan, batas tanggal, dan ukuran file.
5. Ganti `fpdb.csv` dengan output yang sudah diperiksa.
6. Uji `dashboard-mikro.html` secara lokal dan pada website publik.
7. Catat tanggal rilis sumber dan perbarui README jika versi data atau metodologi berubah.

Jangan mengganti dataset lama secara diam-diam ketika hasil analisis sebelumnya masih digunakan. Simpan tanggal/versi sumber bersama laporan atau hasil analisis agar perhitungan dapat direproduksi.

## Menjalankan secara lokal

Dashboard mikro memuat data menggunakan `fetch('./fpdb.csv')`. Browser umumnya membatasi permintaan file dari protokol lokal `file://`. Karena itu, gunakan HTTP server saat menguji di luar lingkungan preview yang sudah menyediakan localhost.

Dengan Python terpasang, buka PowerShell di direktori proyek:

```powershell
py -m http.server 8000
```

Kemudian buka:

- `http://localhost:8000/` — landing page
- `http://localhost:8000/dashboard.html` — dashboard makro
- `http://localhost:8000/dashboard-mikro.html` — dashboard mikro

Hentikan server lokal dengan `Ctrl+C`.

Jika menggunakan browser preview yang sudah menyediakan server localhost, gunakan URL dari lingkungan tersebut dan pastikan `fpdb.csv` ikut disajikan dari direktori yang sama dengan `dashboard-mikro.html`.

## Publikasi menggunakan GitHub Pages

Proyek ini merupakan static website. Tidak diperlukan backend, server database, atau proses build.

1. Push file website ke branch publikasi repository, misalnya `main`.
2. Buka **Settings → Pages** pada repository GitHub.
3. Pada bagian **Build and deployment**, pilih **Deploy from a branch**.
4. Pilih branch `main` dan direktori `/(root)` (atau branch/direktori yang benar-benar digunakan repository).
5. Simpan pengaturan dan tunggu deployment selesai.
6. Buka URL Pages yang ditampilkan GitHub dan uji ketiga halaman.

### Struktur direktori publik

Letakkan file berikut pada tingkat direktori yang sama:

```text
repository-root/
├── index.html
├── dashboard.html
├── dashboard-mikro.html
├── fpdb.csv
├── bbm_household_prices.csv.gz.b64
├── pln_household_tariffs.csv.gz.b64
├── trim_fpdb.py
├── README.md
└── .gitignore
```

Jangan publikasikan backup besar, arsip ZIP sementara, atau file lokal yang tidak diperlukan. File publik `fpdb.csv` memang dimaksudkan sebagai dataset hasil pemangkasan dari 2016 ke atas.

## Sumber dan atribusi

Kerangka dashboard menggunakan informasi dan/atau dataset publik dari sejumlah institusi berikut. Periksa metadata, tanggal publikasi, versi, metodologi, serta ketentuan penggunaan pada masing-masing sumber sebelum mengutip atau menggunakan ulang data:

- [World Bank — Real Time Food Prices Indonesia](https://microdata.worldbank.org/catalog/6166)
- [World Bank — RTFP Data API](https://microdata.worldbank.org/catalog/6166/data-api)
- [World Bank — RTFP Data Dictionary](https://microdata.worldbank.org/catalog/6166/data-dictionary)
- [Badan Pusat Statistik (BPS)](https://www.bps.go.id/) — CPI, Susenas, dan publikasi pengeluaran penduduk.
- [Bank Indonesia](https://www.bi.go.id/) — PIHPS dan publikasi terkait pemantauan harga pangan.
- [Badan Pangan Nasional](https://badanpangan.go.id/) — informasi dan pemantauan harga pangan.
- [Kementerian ESDM](https://www.esdm.go.id/) — kebijakan energi, BBM, dan regulasi/komunikasi terkait listrik.
- [PLN](https://web.pln.co.id/) — statistik kelistrikan dan informasi tarif.

Ketentuan penggunaan dataset World Bank mewajibkan atribusi yang sesuai dan tidak memperbolehkan pengguna menyiratkan bahwa World Bank mendukung produk atau analisis turunan. Periksa ketentuan katalog yang berlaku dan batasan pada materi sumber sebelum mendistribusikan ulang data. Proyek ini tidak didukung atau disahkan oleh institusi yang disebutkan di atas.

## Prinsip metodologi

- **Pisahkan observasi dan asumsi.** Data historis, peristiwa kebijakan, interpretasi analitis, dan input skenario harus tetap dapat dibedakan.
- **Jangan mengisi data hilang dengan angka rekaan.** Data kosong harus tetap kosong atau secara eksplisit diberi label sebagai estimasi/interpolasi.
- **Pertahankan satuan dan cakupan geografis.** Rp/kg, Rp/liter, Rp/kWh, kelompok komoditas, golongan daya, pasar, dan wilayah tidak dapat dipertukarkan begitu saja.
- **Jangan melebih-lebihkan keterwakilan.** Estimasi tingkat pasar atau rata-rata sederhana pasar tidak otomatis menjadi indeks harga nasional.
- **Buat skenario yang dapat direproduksi.** Catat asumsi, periode acuan, versi sumber, dan metode perhitungan.
- **Periksa keterbandingan antarwaktu.** Desain survei, bobot CPI, definisi komoditas, tarif, HET daerah, dan batas administrasi dapat berubah.

## Keterbatasan

- Lintasan stress test makro adalah skenario kondisional, bukan forecast probabilistik.
- Profil rumah tangga dan asumsi pertumbuhan default pada simulator mikro bersifat ilustratif dan dapat diubah pengguna; bukan rata-rata rumah tangga resmi.
- Dataset BBM 2016–2026 terdiri dari 49 snapshot terpilih, bukan seri harian/bulanan lengkap; tanggal dan cakupan wilayah berbeda menurut sumber.
- Dataset PLN 2016–2026 terdiri dari 71 catatan untuk tujuh golongan rumah tangga; jenis catatan dan ketersediaan snapshot tidak seragam antarperiode, dan data kosong tidak diinterpolasi.
- HET LPG dan harga eceran membutuhkan catatan spesifik wilayah serta waktu; satu nilai nasional tidak boleh diasumsikan.
- Data Susenas membutuhkan harmonisasi dan interpretasi hati-hati antarputaran survei serta perubahan kuesioner/desain.
- Database RTFP mengandung estimasi berbasis model dan cakupan pasar yang bervariasi; nilainya dapat direvisi pada rilis berikutnya.
- Garis grafik yang terlihat berkesinambungan tidak berarti setiap bulan atau pasar memiliki harga yang diamati secara langsung.

## Teknologi

- HTML5, CSS, dan JavaScript.
- [Chart.js](https://www.chartjs.org/) untuk grafik interaktif, dimuat melalui CDN jsDelivr.
- Python standard library (`csv`, `pathlib`, dan modul terkait) untuk memangkas CSV FPDB.
- GitHub Pages atau layanan static hosting lain untuk publikasi.

Koneksi internet diperlukan untuk memuat Chart.js dari CDN. File FPDB dan dua arsip energi dibaca dari direktori publik yang sama; arsip energi didekompresi oleh browser.

## Lisensi dan penggunaan ulang

Belum ada lisensi perangkat lunak terpisah yang dinyatakan untuk repository ini, kecuali jika ditambahkan kemudian. Patuhi ketentuan dan kewajiban atribusi dari setiap dataset sumber, publikasi, dan library pihak ketiga. Jangan menyiratkan dukungan atau pengesahan institusional.

---

**Status proyek:** Kerangka dashboard publik dengan tampilan makro dan tingkat rumah tangga. Cakupan data masih berkembang; periksa source register dashboard dan tanggal rilis data sebelum mengutip angka tertentu.
