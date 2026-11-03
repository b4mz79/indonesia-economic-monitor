# IEM Project — Roadmap Pengembangan

**Status dokumen:** Roadmap awal  
**Tanggal penyusunan:** 3 November 2026  
**Repository:** https://github.com/b4mz79/indonesia-economic-monitor

## Arah pengembangan

Mengembangkan Indonesia Economic Monitor (IEM Project) dari dashboard statis berbasis kompilasi data menjadi monitor berkala yang tetap transparan mengenai sumber, periode, metodologi, dan keterbatasan data. Prioritas berikutnya adalah membangun mekanisme **Scenario vs Actual** untuk dashboard makro, tanpa menyamarkan skenario kondisional yang sudah ada sebagai forecast resmi.

## Roadmap

| Tahap | Target waktu | Fokus | Hasil yang diharapkan |
|---|---|---|---|
| 1. Fondasi pemantauan | November 2026 | Inventarisasi sumber primer per indikator; definisi, satuan, frekuensi, cakupan, jadwal rilis; desain struktur data dan QA | Source register; skema vintage skenario dan observasi aktual; baseline skenario dibekukan |
| 2. Baseline dan dry run | Desember 2026 | Menyiapkan pencatatan vintage; mengumpulkan rilis aktual terbaru yang tersedia; simulasi proses pembaruan bulanan | Baseline terdokumentasi; laporan dry run; daftar sumber yang dapat/tidak dapat diotomasi |
| 3. Scenario vs Actual | Mulai Januari 2027 | Pembaruan aktual berkala dan perbandingan dengan lintasan stress test 2027–2030 | Tampilan aktual, skenario pembanding, deviasi, status rilis, tanggal pembaruan, dan catatan interpretasi |
| 4. Otomasi selektif | Setelah sumber stabil | GitHub Actions untuk sumber dengan endpoint/unduhan stabil; validasi otomatis; perubahan diajukan sebagai commit/PR untuk review | Pipeline terjadwal yang dapat direproduksi, dengan log, QA, dan jejak perubahan |
| 5. Evaluasi dan pengembangan forecast | Tahap lanjutan | Jika diperlukan, membangun forecast terpisah dengan metode, input, horizon, dan vintage eksplisit | Forecast vs Actual yang dapat dievaluasi secara metodologis; tidak mencampur forecast dengan stress scenario |

## Cakupan pemantauan makro

1. Pertumbuhan ekonomi dan inflasi.
2. Nilai tukar rupiah dan cadangan devisa.
3. Energi, termasuk ICP dan indikator pasokan/biaya energi.
4. Perdagangan, ekspor-impor, dan neraca eksternal.
5. Fiskal: pendapatan, belanja, defisit, utang, subsidi, dan kompensasi energi.
6. Geopolitik dan ketahanan pasokan sebagai konteks risiko, bukan dipaksakan menjadi seri numerik jika tidak tersedia ukuran yang konsisten.

Frekuensi indikator tidak seragam. Siklus review dilakukan bulanan, tetapi tidak berarti setiap indikator memiliki angka baru setiap bulan. Pembaruan hanya dilakukan ketika sumber merilis observasi atau revisi yang dapat diverifikasi.

## Desain data yang dituju

### 1. Scenario vintages

Setiap versi skenario disimpan terpisah dengan sekurang-kurangnya: `scenario_id`, `vintage_date`, `indicator`, `period`, `value`, `unit`, `assumption_note`, dan `methodology_note`. Vintage lama tidak boleh ditimpa.

### 2. Actual observations

Setiap observasi aktual disimpan dengan sekurang-kurangnya: `indicator`, `observation_period`, `value`, `unit`, `release_date`, `source_name`, `source_url`, `status`, dan `coverage_note`. Revisi data harus dapat dilacak.

### 3. Comparison layer

Lapisan perbandingan menghubungkan aktual dengan vintage skenario yang sesuai. Perhitungan deviasi hanya dilakukan ketika definisi, satuan, periode, dan perimeter sebanding. Data yang belum dirilis atau tidak sebanding harus ditandai, bukan diisi atau dipaksakan.

## Siklus pembaruan akhir bulan

Review akhir bulan mencakup:
- pemeriksaan rilis baru/revisi dari sumber primer;
- pencatatan periode data dan tanggal rilis;
- pembaruan seri yang memiliki data baru saja;
- pemeriksaan kualitas dan keterbandingan;
- perhitungan deviasi Scenario vs Actual jika layak;
- ringkasan perubahan, sumber, data tertunda, dan isu metodologi;
- review sebelum dataset/dashboard dipublikasikan.

**Otomasi awal:** review bulanan berbantuan untuk mengidentifikasi rilis dan menyiapkan usulan perubahan.  
**Otomasi lanjutan:** GitHub Actions terjadwal hanya untuk sumber yang menyediakan endpoint/unduhan stabil dan dapat divalidasi secara deterministik. Perubahan yang memerlukan interpretasi manual tidak boleh dipublikasikan otomatis tanpa review.

## Prinsip yang tidak boleh dilanggar

- Skenario 2027–2030 yang sekarang adalah **conditional stress scenario**, bukan forecast resmi atau probabilitas.
- Gunakan label **Scenario vs Actual** sampai tersedia forecast terpisah yang memiliki metode dan vintage jelas.
- Pisahkan observed, estimated, revised, scenario, dan forecast.
- Jangan mengarang, menginterpolasi, atau menganggap data belum tersedia sebagai nol.
- Jangan menggabungkan seri dengan frekuensi, definisi, satuan, atau perimeter berbeda tanpa penjelasan.
- Pertahankan source URL, tanggal rilis/akses, versi, dan catatan perubahan.
- Jangan menimpa vintage skenario maupun observasi historis yang telah dipublikasikan.
- Semua perubahan publik harus melalui pemeriksaan kualitas dan dapat direproduksi.

## Dokumen terkait

- [Project Background](PROJECT_BACKGROUND.md)
- [Data Maintenance](DATA_MAINTENANCE.md)
- [README dan metodologi](README.md)
