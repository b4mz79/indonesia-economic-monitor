# Data Maintenance Playbook — Indonesia Economic Monitor

> **Dokumen handover operasional untuk pemeliharaan dataset.** Baca dokumen ini sebelum memperbarui angka, mengganti CSV, mengubah asumsi, atau mengedit dashboard. Tujuannya menjaga kesinambungan kerja lintas sesi dan mencegah data yang tidak sebanding tercampur.

- Repository: https://github.com/b4mz79/indonesia-economic-monitor
- Branch acuan: `main`
- Website: https://b4mz79.github.io/indonesia-economic-monitor/
- Zona waktu pencatatan: WIB (Asia/Jakarta)
- Baseline dokumen ini: **3 November 2026**

## 1. Aturan kerja yang tidak boleh dilanggar

1. **Periksa repo `main` terlebih dahulu.** Isi GitHub terbaru adalah source of truth; jangan mengandalkan cuplikan kode atau file dari percakapan lama.
2. **Jangan mengarang, menginterpolasi, atau mengisi data yang tidak ditemukan.** Nilai kosong lebih benar daripada angka perkiraan tanpa dasar.
3. **Simpan provenance per observasi.** Dataset harga harus mempertahankan tanggal/periode, lokasi, unit, tahap rantai harga, nama sumber, URL sumber, dan catatan metodologi.
4. **Pisahkan observasi, estimasi model, kebijakan resmi, survei pengeluaran, dan asumsi skenario.** Jangan menyatukannya menjadi satu seri tanpa label dan metodologi yang jelas.
5. **Jangan menyamakan cakupan lokal dengan nasional.** Harga di satu kota/kabupaten tidak otomatis mewakili provinsi; satu provinsi tidak mewakili Indonesia.
6. **Jangan menghapus sejarah secara diam-diam.** Jika revisi sumber mengubah data lama, simpan tanggal/versi sumber dan catat perubahan.
7. **Jangan mengganti definisi indikator hanya demi menyambungkan seri.** Perubahan perimeter, populasi, frekuensi, satuan, metode survei, atau harga harus ditandai.
8. **Pertahankan batas lisensi.** MIT hanya untuk kode asli proyek; data World Bank/BPS/media/pemerintah dan materi pihak ketiga mengikuti ketentuan masing-masing. Jangan menganggap semua CSV bebas dilisensikan ulang.
9. **Update README dan catatan perubahan** jika sumber, cakupan, definisi, periode, atau keterbatasan data berubah secara material.
10. **Validasi sebelum menyatakan selesai.** Baca ulang file dari GitHub, periksa skema dan konsistensi, uji JavaScript, lalu periksa GitHub Pages Actions.

## 2. Peta file data dan cara pembaruannya

| File | Dipakai untuk | Bentuk / skema | Strategi pembaruan |
|---|---|---|---|
| `fpdb.csv` | Harga pangan tingkat pasar (Food Price Database) | CSV besar; 88 variabel sumber versi baseline, termasuk kolom `c_*` close-price estimates | Periksa katalog World Bank RTFP dan rilis Indonesia terbaru; unduh arsip, simpan backup, ekstrak, pangkas mulai 2016, QA, baru ganti file aktif |
| `bbm_household_prices.csv.gz.b64` | Snapshot harga BBM rumah tangga | gzip yang dikodekan Base64 agar dapat disimpan sebagai teks di GitHub | Tambah snapshot ketika ada perubahan harga yang terverifikasi; jangan membuat panel bulanan palsu |
| `pln_household_tariffs.csv.gz.b64` | Tarif listrik rumah tangga | gzip + Base64; seri tarif menurut golongan dan periode efektif | Periksa keputusan tarif/siaran resmi PLN atau ESDM setiap periode penyesuaian; catat golongan, daya, subsidi, tanggal efektif dan jenis tarif |
| `lpg_household_prices.csv` | HET LPG 3 kg di pangkalan dan harga agen Bright Gas | CSV; `observation_date,product,capacity_kg,price_rp_per_cylinder,region,administrative_level,price_stage,record_status,date_precision,source_name,source_url,source_note` | Update saat ada regulasi HET daerah atau perubahan harga agen yang dapat diverifikasi; jangan gabungkan tingkat agen, pangkalan dan pengecer |
| `lpg_3kg_retail_prices.csv` | Harga aktual/pantauan konsumen LPG 3 kg di pengecer/pasar | CSV; `period_start,period_end,province,location,price_min_rp_per_cylinder,price_max_rp_per_cylinder,observation_type,source_name,source_url,source_note` | Tambahkan observasi lokal yang memiliki sumber dan periode jelas; pertahankan rentang dan jenis bukti; jangan mengisi provinsi kosong dengan HET |
| `household_welfare_indicators.csv` | Kesejahteraan dan pasar tenaga kerja | CSV; `observation_date,indicator,indicator_label,value,unit,reference_population,frequency,source_name,source_url,source_note` | Update saat rilis BPS yang relevan terbit; frekuensi asli setiap indikator wajib dipertahankan |
| `README_metodologi.txt` | Catatan asumsi dan perbandingan indikator makro | Teks | Update jika baseline historis, periode observasi, perimeter fiskal, atau asumsi stress test berubah |
| `dashboard.html` | Dashboard makro | Sebagian besar angka dan asumsi ditanam langsung dalam JavaScript/HTML | Saat memperbarui data makro, audit array/label/sumber pada file ini dan README; belum ada satu CSV historis makro terpisah yang menjadi sumber tunggal |
| `dashboard-mikro.html` | Dashboard mikro | Memuat file CSV lokal melalui `fetch()`; beberapa seri dikompresi dan didekode di browser | Pastikan nama file, path relatif, parser, dropdown, default filter, label sumber dan unit sesuai dataset terbaru |

### Catatan penting tentang file pemangkasan FPDB

README publik saat baseline ini menjelaskan `trim_fpdb.py`, tetapi **file tersebut tidak terlihat pada daftar file root repository yang diperiksa pada 3 November 2026**. Jangan menganggap script itu tersedia atau menjalankan instruksi lama secara membabi buta. Sebelum update FPDB, periksa kembali apakah script ada di branch/commit terbaru. Jika tidak ada, pulihkan atau tulis ulang proses pemangkasan yang terdokumentasi, uji terhadap arsip sumber, dan commit script beserta dokumentasinya sebelum mengganti `fpdb.csv`.

## 3. Panduan sumber dan frekuensi

### 3.1 Food Price Database — World Bank RTFP

- Katalog: https://microdata.worldbank.org/catalog/6166
- Data API / bulk download: https://microdata.worldbank.org/catalog/6166/data-api
- Data dictionary: https://microdata.worldbank.org/catalog/6166/data-dictionary
- Terms of use: https://microdata.worldbank.org/terms-of-use
- Citation baseline: Andrée, B. P. J. (2021). *Monthly food price estimates by product and market* (Version 2026-10-05). IDN_2021_RTFP_v02_M. Washington, DC: World Bank Microdata Library. https://doi.org/10.48529/2ZH0-JF55

Baseline sumber yang tercatat di README: versi 5 Oktober 2026, data sampai 1 Oktober 2026, 222 pasar, 53.074 observasi, 88 variabel pada katalog. File lokal `fpdb.csv` dipangkas mulai 2016 dan memakai kolom close-price estimates `c_*`. Angka jumlah baris lokal tidak sama dengan jumlah observasi katalog.

**Langkah update:**
1. Periksa versi/rilis paling baru di katalog, bukan menebak resource ID atau URL download lama.
2. Unduh arsip market-level Indonesia dan simpan salinan asli bernama versi/tanggal, di luar file aktif.
3. Ekstrak dan identifikasi CSV market-level yang benar.
4. Pastikan kolom penting masih kompatibel: tanggal, negara, provinsi, kabupaten/kota, pasar, dan kolom harga `c_*`. Baca data dictionary jika nama/definisi kolom berubah.
5. Terapkan filter Indonesia dan tanggal mulai 2016 sesuai metodologi saat ini. Jangan menghapus kolom yang diperlukan dashboard.
6. Audit jumlah baris, tanggal minimum/maksimum, komoditas, pasar, missing values, ukuran file, dan beberapa record acak.
7. Ganti `fpdb.csv` hanya setelah lolos QA; uji load, filter komoditas, filter provinsi/kabupaten/pasar, chart, YoY, reload dan download CSV.
8. Catat versi, tanggal unduh, batas tanggal data, ukuran/baris, transformasi dan perubahan metodologi.

**Guardrail:** RTFP mengandung observasi harga dan estimasi model. Jangan menyebut semua nilai sebagai harga transaksi aktual. Agregasi rata-rata sederhana lintas pasar bukan CPI BPS atau indeks nasional berbobot penduduk. Revisi historis oleh penyedia harus dicatat.

### 3.2 BBM rumah tangga

Gunakan sumber primer/otoritatif untuk harga yang berlaku: pengumuman resmi Pertamina/penyalur, ESDM, atau pemerintah. Media kredibel dapat dipakai untuk merekonstruksi snapshot historis jika tanggal dan wilayahnya jelas.

Untuk setiap snapshot, pertahankan:
- tanggal berlaku atau tanggal laporan (jangan samakan keduanya jika berbeda);
- produk dan varian;
- harga per liter;
- wilayah/radius pemasaran;
- jenis bukti dan presisi tanggal;
- sumber dan URL;
- catatan apakah angka merupakan harga resmi, laporan historis, atau harga di wilayah tertentu.

Jangan menganggap Pertamax satu harga nasional jika sumber menyebut perbedaan wilayah. Jangan membuat nilai bulanan untuk bulan tanpa bukti. Premium adalah seri historis yang terbatas; jangan memperlakukannya sebagai produk yang masih tersedia nasional.

### 3.3 Tarif PLN rumah tangga

Prioritaskan regulasi dan pengumuman resmi PLN/ESDM. Simpan tanggal mulai berlaku, golongan daya, status subsidi/nonsubsidi, satuan Rp/kWh, serta jenis struktur tarif.

Tarif prabayar tunggal, tarif pascabayar dengan blok pemakaian, biaya administrasi, pajak penerangan jalan, dan total tagihan adalah konsep berbeda. Jangan menyajikan tarif nominal sebagai tagihan aktual. Bila tidak ada perubahan tarif, jangan menggandakan snapshot seolah-olah observasi baru; interval berlaku dapat digunakan jika skema data mendukungnya.

### 3.4 LPG 3 kg: HET, agen, pengecer

**Tiga tahap harga wajib dipisah:**
- HET/ketetapan resmi di tingkat pangkalan sesuai regulasi kabupaten/kota.
- Harga agen atau penjualan acuan LPG nonsubsidi, dengan zona/radius yang dinyatakan sumber.
- Harga pasar/pengecer yang dilaporkan atau dipantau, yaitu angka yang mungkin benar-benar dibayar konsumen.

Untuk HET, cari keputusan kepala daerah/JDIH dan verifikasi tanggal berlaku aktual, bukan hanya tanggal keputusan. Untuk harga pengecer, sumber dapat berupa monitoring pemerintah, inspeksi, laporan media, atau keluhan warga; masukkan jenis bukti pada `observation_type`. Catat lokasi rinci dan rentang harga sebagaimana sumber.

**Dilarang:**
- menyamakan HET pangkalan dengan harga eceran;
- menyimpulkan pelanggaran hanya karena harga pengecer melebihi HET;
- menggeneralisasi satu lokasi menjadi harga seluruh provinsi;
- mengubah rentang menjadi satu nilai rata-rata tanpa dasar;
- mengisi provinsi tanpa observasi dengan HET atau estimasi;
- menghitung rata-rata provinsi dari kumpulan sumber yang heterogen tanpa metodologi sampel yang memadai.

Baseline 3 November 2026: file retail berisi **19 catatan**, mencakup **14 dari 38 provinsi**. Angka 14/38 berarti provinsi yang memiliki observasi terverifikasi/tertelusur dalam dataset saat itu, bukan survei nasional yang representatif. Satu laporan gabungan Jakarta Selatan–Tangerang Selatan tidak dapat dihitung sebagai provinsi terpisah karena tidak terdisagregasi.

### 3.5 Kesejahteraan dan pasar tenaga kerja — BPS

Sumber utama: https://www.bps.go.id/ dan publikasi/rilis BPS sesuai indikator (Susenas, Sakernas, kemiskinan, IPM).

Pertahankan frekuensi asli:
- Sakernas: titik Februari/Agustus atau periode khusus yang disebutkan rilis.
- Kemiskinan, Gini, distribusi pengeluaran: titik Susenas Maret/September yang tersedia.
- Pengeluaran riil per kapita disesuaikan: seri tahunan IPM.
- Upah: nilai nominal dan populasi buruh/karyawan/pegawai yang didefinisikan BPS.

Jangan mengubah seri semesteran/semester khusus menjadi bulanan. Jangan menyebut upah nominal sebagai upah riil tanpa deflator dan periode yang cocok. Gini dan porsi 40% terbawah pada file ini mengukur distribusi **pengeluaran**, bukan pendapatan. TPT menggunakan angkatan kerja sebagai denominator; setengah pengangguran adalah indikator berbeda.

### 3.6 Indikator makro pada dashboard

Angka historis dan asumsi stress test saat ini sebagian tertanam dalam `dashboard.html` dan dijelaskan di `README.md` / `README_metodologi.txt`. Saat memperbarui:
- cari rilis resmi untuk masing-masing indikator dan simpan periode observasi serta unit;
- jangan menyambung data dengan perimeter berbeda tanpa catatan (misalnya utang pemerintah pusat vs general government);
- bedakan annual average, year-end, satu bulan, year-to-date, kuartal, dan year-on-year;
- jangan membandingkan angka 2026 parsial dengan setahun penuh tanpa label;
- jangan mengubah lintasan stress 2027–2030 menjadi forecast atau probabilitas;
- jika asumsi skenario berubah, jelaskan alasan dan ubah README serta label dashboard bersamaan.

## 4. QA checklist sebelum commit

### Dataset
- [ ] Header/urutan kolom sesuai schema atau perubahan schema dijelaskan.
- [ ] Tanggal valid dan format konsisten; rentang periode masuk akal.
- [ ] Unit dan basis harga jelas (Rp/liter, Rp/kWh, Rp/tabung, %, indeks, orang, dan sebagainya).
- [ ] Tidak ada duplikasi yang tidak disengaja; duplikat sah dijelaskan.
- [ ] Nilai kosong tidak diisi dengan asumsi diam-diam.
- [ ] Sumber dan URL tersedia untuk setiap observasi yang memerlukannya.
- [ ] Periode, wilayah, populasi referensi, dan frekuensi tidak hilang.
- [ ] Klasifikasi observasi vs estimasi vs kebijakan resmi vs asumsi tetap benar.
- [ ] Jumlah baris, tanggal terbaru, cakupan wilayah/komoditas dan ukuran file dicatat.
- [ ] File lama/backup tersedia sebelum penggantian dataset besar.

### Dashboard
- [ ] Nama file/path `fetch()` sesuai.
- [ ] Tidak ada error JavaScript atau kegagalan parsing CSV.
- [ ] Status loading, empty state, dan error state bekerja.
- [ ] Filter/default selection sesuai (beras tetap menjadi default komoditas pangan jika masih tersedia).
- [ ] Angka KPI, chart, tabel, dan download menggunakan dataset yang sama.
- [ ] Label sumber, tanggal data, satuan, cakupan, dan disclaimer sesuai.
- [ ] Semua tautan navigasi/back-to-home, source repository, dan scroll-to-top tetap berfungsi.
- [ ] Uji lokal via HTTP server, bukan hanya membuka HTML dengan `file://`.

### GitHub
- [ ] Fetch SHA terbaru dari branch `main` sebelum update file.
- [ ] Update file secara berurutan; jangan menulis file yang sama secara paralel.
- [ ] Baca ulang file yang baru di-commit dan verifikasi isinya.
- [ ] Periksa seluruh inline script dengan parser JavaScript.
- [ ] Periksa GitHub Actions Pages run untuk commit terbaru.
- [ ] Nyatakan deployment selesai hanya jika workflow terbaru sukses; commit saja bukan bukti portal sudah terpublikasi.

## 5. Format log pembaruan dataset

Setiap sesi pembaruan data yang material dicatat di bagian bawah dokumen ini atau dalam file log bertanggal. Gunakan format berikut:

```text
Tanggal/WIB:
File:
Indikator/produk:
Sumber dan URL:
Tanggal rilis sumber:
Periode data:
Cakupan wilayah/populasi:
Jumlah baris sebelum -> sesudah:
Tanggal minimum/maksimum:
Transformasi:
QA:
Perubahan metodologi/definisi:
Keterbatasan:
Commit:
Status GitHub Pages:
```

Jangan hanya menulis “dataset diperbarui”. Catat apa yang berubah, mengapa, dan bagaimana memverifikasinya.

## 6. Riwayat pemeliharaan

### 2026-11-03 — Baseline playbook dibuat
- Menyatukan aturan pembaruan untuk dataset pangan, BBM, PLN, LPG, kesejahteraan/tenaga kerja, serta indikator makro.
- Menegaskan pemisahan HET pangkalan vs harga pengecer dan larangan mengisi cakupan yang tidak tersedia.
- Mencatat baseline LPG retail 19 catatan / 14 dari 38 provinsi.
- Mencatat sumber FPDB World Bank yang digunakan: versi 2026-10-05, data sampai 2026-10-01.
- Menandai bahwa `trim_fpdb.py` disebut dalam README, tetapi tidak ditemukan pada daftar file root yang diperiksa; perlu verifikasi/pemulihan sebelum update FPDB berikutnya.
- Memuat checklist QA dan format log untuk sesi pemeliharaan selanjutnya.

---

*Dokumen internal proyek untuk menjaga konsistensi kerja. Perbarui dokumen ini ketika struktur file, skema, sumber, proses ETL, cakupan, atau metodologi berubah.*
