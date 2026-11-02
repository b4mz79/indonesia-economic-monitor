# Indonesia Economic Intelligence

**Indonesia Economic Risk & Household Cost Monitor**  
*Kerangka pemantauan historis: 2016–2026 · Horizon skenario: 2027–2030*

Proyek dashboard publik dan independen untuk mengeksplorasi bagaimana risiko geopolitik dan ekonomi eksternal dapat merambat ke perekonomian Indonesia, harga kebutuhan dasar, biaya hidup, serta daya beli rumah tangga.

> **Disclaimer:** Proyek ini merupakan alat analisis, edukasi, dan pemantauan independen. Ini bukan publikasi resmi, nasihat investasi/keuangan, nasihat hukum, rekomendasi kebijakan, atau pengganti data dan pengumuman resmi. Nilai skenario merupakan asumsi kondisional, bukan prediksi. Data dapat tidak lengkap, berbeda cakupan/periode, terlambat, atau direvisi. Penggunaan ulang kode dan data tunduk pada ketentuan yang berbeda: **MIT hanya berlaku untuk kode asli proyek; dataset dan materi pihak ketiga tidak otomatis dilisensikan dengan MIT.** Baca bagian [Disclaimer](#disclaimer) dan [Lisensi dan penggunaan ulang](#lisensi-dan-penggunaan-ulang) sebelum mengutip atau menggunakan kembali materi.

## Website publik

Portal publik GitHub Pages:

- **Website:** https://b4mz79.github.io/indonesia-economic-monitor/

Navigasi utama:

| Halaman | File | Isi |
|---|---|---|
| Ringkasan proyek | [`index.html`](index.html) | Konteks, kerangka analisis, sumber data, asumsi, dan navigasi dashboard |
| Indonesia Economic Risk Dashboard | [`dashboard.html`](dashboard.html) | Kerangka indikator risiko makro dan stress test 2027–2030 |
| Household Cost & Basic Needs Dashboard | [`dashboard-mikro.html`](dashboard-mikro.html) | Harga BBM, tarif PLN, LPG subsidi/nonsubsidi, pengangguran, upah, kemiskinan, daya beli, ketimpangan, pangan, dan simulator biaya |

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

## LPG Household Price Dataset

File publik: [`lpg_household_prices.csv`](lpg_household_prices.csv) (referensi HET pangkalan dan harga agen) serta [`lpg_3kg_retail_prices.csv`](lpg_3kg_retail_prices.csv) (pantauan harga konsumen/pengecer LPG subsidi 3 kg).

Dataset referensi `lpg_household_prices.csv` memisahkan:
- **HET LPG 3 kg di tingkat pangkalan:** ketetapan daerah per kabupaten/kota. Kota Bandung, Kabupaten Bandung, dan Kota Cimahi memiliki dasar serta tanggal pelaksanaan berbeda.
- **Bright Gas 5,5 kg dan 12 kg:** snapshot harga nonsubsidi tingkat agen menurut zona dan tanggal sumber, termasuk tabel regional 15 Juli 2026 serta pembaruan Pulau Jawa pada 15 Agustus 2026. Harga agen bukan selalu harga akhir yang dibayar konsumen.

Dataset terpisah `lpg_3kg_retail_prices.csv` berisi 19 catatan harga pasar/pengecer yang dapat ditelusuri, mencakup 14 dari 38 provinsi: Aceh, Sumatera Utara, Riau, Kepulauan Bangka Belitung, DKI Jakarta, Jawa Barat, DI Yogyakarta, Jawa Timur, Kalimantan Barat, Kalimantan Tengah, Nusa Tenggara Barat, Sulawesi Tengah, Sulawesi Selatan, dan Sulawesi Tenggara. Satu catatan lintas Jakarta Selatan–Tangerang Selatan tidak dipisahkan menurut provinsi dan karena itu tidak dihitung sebagai provinsi tambahan. Rentang dan angka mengikuti sumber; jenis observasi dibedakan antara pemantauan resmi, inspeksi lapangan, laporan media, dan keluhan masyarakat. Ini bukan survei harga provinsi yang seragam atau rata-rata provinsi.

File retail memuat periode laporan/pengamatan, provinsi dan lokasi rinci, rentang harga per tabung, jenis observasi, sumber, URL, serta catatan metodologi. Nilai yang belum ditemukan dibiarkan kosong; tidak diisi dengan HET pangkalan.

**Penting:** HET LPG 3 kg bukan angka nasional tunggal. Jangan menggunakan HET Kota Bandung untuk seluruh Jawa Barat/Indonesia. Snapshot harga nonsubsidi tidak membentuk panel bulanan nasional dan tidak diinterpolasi.

## Household Welfare and Labour Market Dataset

File publik: [`household_welfare_indicators.csv`](household_welfare_indicators.csv). Dataset saat ini berisi sebelas kelompok indikator:
1. **Pengeluaran riil per kapita per tahun yang disesuaikan** — proxy standar hidup layak berdasarkan konsumsi Susenas yang disesuaikan dengan IHK dan PPP (komponen IPM). Nilai bukan pendapatan disposabel atau upah.
2. **Upah rata-rata buruh** — nilai nominal bulanan pekerja buruh/karyawan/pegawai. Belum dideflasi dan tidak mencakup semua pekerja mandiri/informal.
3. **TPT** — penganggur sebagai persentase angkatan kerja.
4. **TPAK** — partisipasi penduduk usia kerja dalam angkatan kerja.
5. **Proporsi pekerja informal** — menggunakan klasifikasi status pekerjaan BPS.
6. **Kemiskinan** — persentase penduduk di bawah garis kemiskinan, hasil Susenas.
7. **Gini Ratio** — ketimpangan distribusi pengeluaran, bukan pendapatan.
8. **Porsi pengeluaran 40% terbawah** — ukuran distribusi pengeluaran menurut kriteria Bank Dunia.
9. **Setengah pengangguran** — tingkat dan jumlah pekerja yang masih menginginkan/tersedia untuk tambahan jam/pekerjaan; indikator labor underutilization yang tidak tertangkap hanya oleh TPT.
10. **Jumlah angkatan kerja, penduduk bekerja, dan penganggur** — ukuran stok tenaga kerja nasional pada November 2025, Februari dan Mei 2026.
11. **Garis kemiskinan per kapita/bulan** — batas minimum pengeluaran nasional untuk makanan dan nonmakanan.

Frekuensi dan periode sumber dipertahankan:
- Sakernas menggunakan titik periode survei yang disebutkan dalam rilis (antara lain Agustus, November 2025, Februari dan Mei 2026); jangan menganggapnya sebagai seri bulanan kontinu.
- Kemiskinan, Gini, dan distribusi pengeluaran memakai periode Susenas Maret/September yang tersedia.
- Pengeluaran riil per kapita yang disesuaikan merupakan indikator IPM tahunan; nilai 2020–2025 menggunakan seri nasional BPS.
- Semua nilai upah pada file adalah **nominal**. Penghitungan upah riil memerlukan deflator IHK yang periodenya cocok; dashboard tidak membuat klaim upah riil dari selisih inflasi sederhana.

Satu indikator tidak cukup untuk mewakili daya beli. Kombinasi pengeluaran riil per kapita, upah, kemiskinan, distribusi pengeluaran, TPT, setengah pengangguran, TPAK, informalitas, jumlah penduduk bekerja, dan garis kemiskinan memberikan konteks yang lebih luas. Kualitas pekerjaan, jam kerja, dan pendapatan rumah tangga tetap perlu diperluas saat seri data yang sebanding tersedia. Seri setengah pengangguran nasional kini mencakup 2023 (6,68%), 2024 (7,99%), 2025 (7,91%), dan Februari 2026 (7,27%). BPS mencatat jumlah setengah penganggur 9,34 juta pada 2023 dan 11,56 juta pada 2024.

- BPS — [Keadaan Angkatan Kerja Indonesia Februari 2026](https://www.bps.go.id/id/publication/2026/06/26/96b31cf730df9e84f17bfe03/keadaan-angkatan-kerja-di-) dan rilis Sakernas Mei 2026 — ketenagakerjaan, TPT, TPAK, upah dan jumlah penduduk bekerja.
- BPS — [Sakernas Mei 2026](https://www.bps.go.id/id/pressrelease/2026/08/05/2606/tingkat-pengangguran-terbuka-tpt-sebesar-4-65-persen-rata-rata-upah-buruh-sebesar-3-39-juta-rupiah.html) — TPT, TPAK, upah, angkatan kerja, penduduk bekerja.
- BPS — [Sakernas Februari 2026](https://www.bps.go.id/id/news/2026/05/06/910/ekonomi-indonesia-resilien-dan-tumbuh-solid--pada-triwulan-i-2026.html) — jumlah penganggur, TPT dan setengah pengangguran.
- BPS — [Indikator Pekerjaan Layak di Indonesia 2024](https://web-api.bps.go.id/download.php?f=V3QKN8oEbZwBYEUHwdWdZHJGOUx6eTJqUXQ4M2o0dldpTmMrUEVwNHB1ZTMvZEFyVDVmcVhPNFU4NVRtcFNta2R1TGI1N0txQ29oWnVFRnM0Tm5HMUVxMk9nbHlGd1dKcVYzaDk2QXpCQ04rVHJKNVB5WkJscUg3RGFxUFN4WjRsR3R3aWJ1dDl0bzE2VzRCbmxSSDdHcmg2eEJWKzFVOWdmMDZnbHhEUms5NWxFb3dFcFh1akxXM0RQRjNxTVluOHorYWVFZHU2dHg5bVV3b1RMZStSZTNZVDVublNudTlRRnFyWU5mWjlPcVRta1JhelNxaTZHclVTaWpHak1mdHZmN2JzZzgxRXB2ZzFuTkgvNFh0ODlGK1paTHdnPT0%3D) — setengah pengangguran dan indikator pekerjaan layak.

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
├── lpg_household_prices.csv
├── lpg_3kg_retail_prices.csv
├── household_welfare_indicators.csv
├── trim_fpdb.py
├── README.md
├── LICENSE
└── .gitignore
```

Jangan publikasikan backup besar, arsip ZIP sementara, atau file lokal yang tidak diperlukan. File publik `fpdb.csv` memang dimaksudkan sebagai dataset hasil pemangkasan dari 2016 ke atas.

- BPS — Indikator Pekerjaan Layak di Indonesia 2024 (Sakernas), untuk indikator setengah pengangguran.

## Sumber dan atribusi

Kerangka dashboard menggunakan informasi dan/atau dataset publik dari sejumlah institusi berikut. Periksa metadata, tanggal publikasi, versi, metodologi, serta ketentuan penggunaan pada masing-masing sumber sebelum mengutip atau menggunakan ulang data:

- [World Bank — Real Time Food Prices Indonesia](https://microdata.worldbank.org/catalog/6166)
- [World Bank — RTFP Data API](https://microdata.worldbank.org/catalog/6166/data-api)
- [World Bank — RTFP Data Dictionary](https://microdata.worldbank.org/catalog/6166/data-dictionary)
- [Badan Pusat Statistik (BPS)](https://www.bps.go.id/) — CPI, Susenas, dan publikasi pengeluaran penduduk.
- [Bank Indonesia](https://www.bi.go.id/) — PIHPS dan publikasi terkait pemantauan harga pangan.
- [Badan Pangan Nasional](https://badanpangan.go.id/) — informasi dan pemantauan harga pangan.
- [Kementerian ESDM](https://www.esdm.go.id/) — kebijakan energi, BBM, dan regulasi/komunikasi terkait listrik.
- [JDIH Kota Bandung](https://jdih.bandung.go.id/home/produk-hukum/peraturan-perundang-undangan-daerah/24800) dan [Database Peraturan BPK](https://peraturan.bpk.go.id/Details/327304/perbup-kab-bandung-no-91-tahun-2025) — referensi HET LPG 3 kg di tingkat pangkalan.
- [e-Pasar Kota Cimahi](https://e-pasar.cimahikota.go.id/komoditas/lpg-3kg1763348252), [ANTARA Aceh](https://aceh.antaranews.com/berita/413403/harga-lpg-3-kg-di-aceh-barat-tembus-rp45-ribu-tabung-begini-respons-pemkab), [MISTAR Pematangsiantar](https://mistar.id/news/siantar-simalungun/harga-lpg-3-kg-di-pangkalan-rp17-ribu-di-pengecer-tembus-rp22-ribu), [PPID Riau](https://ppid.riau.go.id/berita/19091/kejati-riau-awasi-distribusi-lpg-bersubsidi-ke-masyarakat), [Ombudsman Babel](https://ombudsman.go.id/news/download/pwkmedia--kelangkaan-lpg-3-kg-potret-rapuhnya-tata-kelola-kapitalistik), [Ombudsman DIY](https://ombudsman.go.id/perwakilan/news/r/pwkmedia--hasil-pengawasan-ombudsman-diy-elpiji-langka-harga-naik), [Pemkot Bima](https://portal.bimakota.go.id/web/detail-berita/3447/wali-kota-bima-larang-penjualan-lpg-3-kg-di-pengecer-pengawasan-distribusi-diperketat), [InfoPublik Palangka Raya](https://infopublik.id/kategori/nusantara/964950/pemkot-palangka-raya-gelar-pengawasan-distribusi-lpg-3-kg), [RRI Palangka Raya](https://rri.co.id/palangkaraya/info-pemda/2518085/dpkukmp-palangka-raya-sidak-lpg-3-kilogram-temukan-harga-pangkalan-di-atas-het), [Pemkot Madiun](https://pendekarmedia.madiunkota.go.id/berita/16817), [detikSulsel Bone](https://www.detik.com/sulsel/watampone/d-8319713/lpg-3-kg-di-bone-langka-harga-tembus-rp-35-ribu-per-tabung), [Pemkab Morowali](https://morowalikab.go.id/news/pemprov-sulteng-dan-pemkab-morowali-sidak-lpg-3-kg-dan-bbm-jelang-hari-besar-keagamaan), dan sumber lain yang dicantumkan per baris di `lpg_3kg_retail_prices.csv` — pantauan dan laporan harga konsumen/pengecer LPG 3 kg regional.
- [Bisnis.com](https://ekonomi.bisnis.com/read/20260715/44/1988225/daftar-harga-lpg-bright-gas-pertamina-terbaru-15-juli-2026) dan [detikFinance](https://finance.detik.com/energi/d-8619653/harga-bright-gas-pertamina-turun) — harga agen LPG nonsubsidi regional.
- [PLN](https://web.pln.co.id/) — statistik kelistrikan dan informasi tarif.

### Atribusi khusus World Bank RTFP

Katalog World Bank menyatakan bahwa estimasi pada dataset Indonesia tersebut bersumber dari data yang tersedia untuk publik dan dataset harga diterbitkan sebagai open data. Tetap ikuti [World Bank Microdata Library Terms of Use](https://microdata.worldbank.org/terms-of-use), termasuk kewajiban atribusi, larangan menyiratkan endorsement, larangan menggunakan logo/merek tanpa izin, serta pembatasan khusus yang mungkin melekat pada materi tertentu. Status open data RTFP tidak mengubah lisensi sumber lain di repository ini.

Sitasi dataset yang digunakan pada versi katalog **2026-10-05**:

> Andrée, B. P. J. (2021). *Monthly food price estimates by product and market* (Version 2026-10-05). IDN_2021_RTFP_v02_M. Washington, DC: World Bank Microdata Library. [https://doi.org/10.48529/2ZH0-JF55](https://doi.org/10.48529/2ZH0-JF55).

Sebelum mengambil atau mendistribusikan ulang versi RTFP yang lebih baru, periksa kembali metadata, status akses, sitasi, dan syarat penggunaan yang menyertai versi tersebut. Proyek ini tidak didukung, disponsori, atau disahkan oleh World Bank maupun institusi lain yang tercantum sebagai sumber.

## Disclaimer

### Tujuan dan bukan nasihat profesional

Dashboard ini disediakan hanya untuk tujuan informasi, edukasi, eksplorasi data, dan analisis independen. Kontennya bukan nasihat investasi, keuangan, perpajakan, hukum, pengadaan energi, ataupun rekomendasi kebijakan. Dashboard tidak dirancang sebagai satu-satunya dasar untuk keputusan bisnis, investasi, pembelian, kebijakan publik, atau keputusan rumah tangga. Pengguna harus melakukan verifikasi mandiri dan berkonsultasi dengan tenaga profesional atau otoritas yang berwenang bila diperlukan.

### Batas akurasi, kelengkapan, dan waktu

Data dihimpun dari sumber yang berbeda dan dapat memiliki periode, frekuensi, satuan, definisi, kualitas, metode pengumpulan, dan cakupan geografis yang tidak seragam. Sebagian angka merupakan observasi langsung atau laporan lapangan; sebagian lainnya merupakan estimasi, data hasil olahan, atau kutipan dari publikasi. Sumber dapat memperbarui atau merevisi data setelah dashboard diterbitkan. Tidak ada jaminan bahwa seluruh nilai selalu terbaru, akurat, lengkap, bebas kesalahan, atau tersedia tanpa gangguan. Tanggal dan URL sumber per data harus menjadi rujukan utama ketika memverifikasi suatu angka.

### Skenario, proyeksi, dan simulator

Lintasan stress test makro 2027–2030 dan simulator biaya rumah tangga menggunakan asumsi yang dipilih untuk menguji sensitivitas terhadap kondisi tertentu. Angka tersebut bukan ramalan, forecast resmi, probabilitas kejadian, atau jaminan bahwa kondisi masa depan akan mengikuti lintasan yang ditampilkan. Perubahan asumsi dapat menghasilkan keluaran yang berbeda. Pengguna bertanggung jawab menilai kewajaran asumsi sebelum memakai hasil simulasi.

### Harga pasar, HET, dan harga konsumen

Harga BBM, LPG, pangan, listrik, dan kebutuhan dasar dapat berbeda antarwilayah, waktu, kualitas produk, saluran distribusi, jenis penjual, biaya transportasi, serta ketentuan lokal. Khusus LPG subsidi 3 kg, HET yang ditetapkan pemerintah daerah berlaku pada tahap distribusi yang ditentukan dalam regulasi (umumnya tingkat pangkalan/subpenyalur), sedangkan harga pengecer atau pantauan pasar menggambarkan laporan harga yang ditemui atau dibayar konsumen pada lokasi dan waktu tertentu. **Harga pengecer bukan HET resmi.** Rentang harga dalam dataset pengecer bukan survei statistik yang seragam, bukan rata-rata provinsi, dan tidak membuktikan dengan sendirinya adanya pelanggaran oleh penjual atau distributor. Cakupan 14 dari 38 provinsi pada versi dataset saat ini hanya menunjukkan wilayah dengan catatan yang dapat ditelusuri, bukan keseluruhan kondisi pasar nasional.

### Pengolahan dan interpretasi data

Agregasi, konversi satuan, pemilihan observasi, dan visualisasi dapat mempengaruhi cara angka dibaca. Rata-rata sederhana dari titik pasar bukan indeks harga nasional berbobot. Estimasi harga World Bank RTFP menggabungkan pengukuran langsung dan pemodelan untuk mengisi atau memperkirakan nilai yang hilang; angka tersebut tidak identik dengan CPI resmi BPS atau harga transaksi seluruh pasar. Data nominal tidak boleh ditafsirkan sebagai data riil tanpa deflator yang sesuai. Data yang tidak tersedia tidak boleh ditafsirkan sebagai nol, tidak adanya transaksi, atau tidak adanya masalah.

### Sumber pihak ketiga, merek, dan tanggung jawab pengguna

Data, statistik, peraturan, kutipan faktual, publikasi, foto, logo, merek, library eksternal, serta materi pihak ketiga tetap menjadi milik atau berada di bawah ketentuan pemilik/penerbit masing-masing. Pencantuman URL atau atribusi tidak dengan sendirinya memberikan hak untuk menyalin, mengemas ulang, atau mendistribusikan ulang seluruh materi tersebut. Pengguna wajib memeriksa ketentuan sumber sebelum menggunakan kembali data atau konten, menyertakan atribusi yang diwajibkan, dan tidak menyiratkan dukungan atau afiliasi institusional.

Dashboard dan dataset hasil kompilasi disediakan **"sebagaimana adanya"** dan **"sebagaimana tersedia"**, tanpa jaminan tersurat maupun tersirat. Sejauh diizinkan oleh hukum yang berlaku, pengelola dan kontributor proyek tidak bertanggung jawab atas kerugian atau klaim yang timbul dari penggunaan, interpretasi, ketidakakuratan, keterlambatan, atau ketidaktersediaan dashboard dan datanya. Ketentuan ini tidak mengurangi hak atau kewajiban yang tidak dapat dikesampingkan menurut hukum.

## Prinsip metodologi

- **Pisahkan observasi dan asumsi.** Data historis, peristiwa kebijakan, interpretasi analitis, dan input skenario harus tetap dapat dibedakan.
- **Jangan mengisi data hilang dengan angka rekaan.** Data kosong harus tetap kosong atau secara eksplisit diberi label sebagai estimasi/interpolasi.
- **Pertahankan satuan dan cakupan geografis.** Rp/kg, Rp/liter, Rp/kWh, kelompok komoditas, golongan daya, pasar, dan wilayah tidak dapat dipertukarkan begitu saja.
- **Jangan melebih-lebihkan keterwakilan.** Estimasi tingkat pasar atau rata-rata sederhana pasar tidak otomatis menjadi indeks harga nasional.
- **Buat skenario yang dapat direproduksi.** Catat asumsi, periode acuan, versi sumber, dan metode perhitungan.
- **Periksa keterbandingan antarwaktu.** Desain survei, bobot CPI, definisi komoditas, tarif, HET daerah, dan batas administrasi dapat berubah.

- Setengah pengangguran mengukur kekurangan pemanfaatan tenaga kerja di antara orang yang sudah bekerja; indikator ini berbeda dari TPT dan perlu dibaca bersama TPAK, pekerja informal, serta upah.

## Keterbatasan

- Lintasan stress test makro adalah skenario kondisional, bukan forecast probabilistik.
- Profil rumah tangga dan asumsi pertumbuhan default pada simulator mikro bersifat ilustratif dan dapat diubah pengguna; bukan rata-rata rumah tangga resmi.
- Dataset BBM 2016–2026 terdiri dari 49 snapshot terpilih, bukan seri harian/bulanan lengkap; tanggal dan cakupan wilayah berbeda menurut sumber.
- Dataset PLN 2016–2026 terdiri dari 71 catatan untuk tujuh golongan rumah tangga; jenis catatan dan ketersediaan snapshot tidak seragam antarperiode, dan data kosong tidak diinterpolasi.
- Dataset harga pengecer LPG 3 kg saat ini mencakup 14/38 provinsi dan menggabungkan jenis sumber yang berbeda; angka bersifat observasi lokal/rentang laporan, bukan rata-rata provinsi atau survei nasional yang seragam. Penambahan wilayah memerlukan sumber harga konsumen yang eksplisit.
- Dataset HET pangkalan LPG 3 kg dan harga agen Bright Gas tetap terpisah dari harga pengecer; ketiganya tidak boleh dibandingkan tanpa memperhatikan tahap distribusi.
- Indikator daya beli dan ketenagakerjaan memiliki frekuensi yang berbeda (IPM tahunan, Sakernas Februari/Agustus, Susenas Maret/September); angka nominal upah tidak boleh disebut sebagai upah riil.
- HET LPG dan harga eceran membutuhkan catatan spesifik wilayah serta waktu; satu nilai nasional tidak boleh diasumsikan.
- Data Susenas membutuhkan harmonisasi dan interpretasi hati-hati antarputaran survei serta perubahan kuesioner/desain.
- Database RTFP mengandung estimasi berbasis model dan cakupan pasar yang bervariasi; nilainya dapat direvisi pada rilis berikutnya.
- Garis grafik yang terlihat berkesinambungan tidak berarti setiap bulan atau pasar memiliki harga yang diamati secara langsung.

## Teknologi

- HTML5, CSS, dan JavaScript.
- [Chart.js](https://www.chartjs.org/) untuk grafik interaktif, dimuat melalui CDN jsDelivr.
- Python standard library (`csv`, `pathlib`, dan modul terkait) untuk memangkas CSV FPDB.
- GitHub Pages atau layanan static hosting lain untuk publikasi.

Koneksi internet diperlukan untuk memuat Chart.js dari CDN. File FPDB, dataset LPG, indikator kesejahteraan, dan dua arsip energi dibaca dari direktori publik yang sama; arsip energi didekompresi oleh browser.

## Lisensi dan penggunaan ulang

### Kode asli proyek — MIT

Kode sumber asli yang dibuat khusus untuk repository ini dilisensikan di bawah **MIT License**. Lihat file [LICENSE](LICENSE). Lisensi ini memberi izin untuk menggunakan, menyalin, memodifikasi, menggabungkan, menerbitkan, mendistribusikan, mensublisensikan, dan/atau menjual kode yang tercakup, dengan tetap menyertakan pemberitahuan hak cipta dan teks lisensi.

### Dataset dan materi pihak ketiga — tidak tercakup oleh MIT

**MIT License tidak melisensikan ulang seluruh isi repository.** File data dan materi dari pihak ketiga — termasuk **fpdb.csv**, **bbm_household_prices.csv.gz.b64**, **pln_household_tariffs.csv.gz.b64**, **lpg_household_prices.csv**, **lpg_3kg_retail_prices.csv**, **household_welfare_indicators.csv**, serta library, logo, foto, publikasi, dan konten eksternal — dikecualikan dari pemberian lisensi MIT sejauh materi tersebut berasal dari atau memiliki hak pada pihak lain. Ketentuan penggunaan, izin akses, hak cipta, dan kewajiban atribusinya mengikuti sumber atau pemilik masing-masing.

Dataset yang dikompilasi oleh proyek tetap harus digunakan dengan memperhatikan hak dan ketentuan sumber asal. Pencantuman sebuah file di repository publik bukan pernyataan bahwa semua isi file tersebut bebas lisensi, domain publik, atau boleh didistribusikan ulang tanpa syarat. Periksa bagian [Sumber dan atribusi](#sumber-dan-atribusi) serta ketentuan penerbit data sebelum menggunakan ulang atau mendistribusikan data.

Nama institusi, nama produk, merek dagang, dan logo tetap milik pemiliknya. Tidak ada lisensi atau izin untuk menggunakan merek/logo pihak ketiga yang diberikan melalui repository ini.

---

**Status proyek:** Kerangka dashboard publik dengan tampilan makro dan tingkat rumah tangga. Cakupan data masih berkembang; periksa source register dashboard dan tanggal rilis data sebelum mengutip angka tertentu.
