import json

with open('Tugas_Akhir__FINAL.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The target cell starts with '### 3.5 Analisis Mendalam Performa Model Random Forest Regressor'
target_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        if '### 3.5 Analisis Mendalam Performa Model Random Forest Regressor' in content:
            target_idx = i
            break

if target_idx != -1:
    new_source = [
        "### 3.5 Analisis Mendalam Performa Model Random Forest Regressor\n",
        "\n",
        "Berdasarkan metrik evaluasi dan grafik *scatter plot* (Actual vs Predicted) di atas, berikut adalah analisis mendalam mengenai kegagalan performa model regresi pada prediksi persentase Tip:\n",
        "\n",
        "1. **Efektivitas Random Forest pada Data Tip:**\n",
        "   * Algoritma Random Forest secara *default* sangat mudah membangun pohon keputusan (*decision trees*) yang mendalam. Pada kasus dataset regresi tip ini, model mengalami masalah **Overfitting parah** pada tahap awal. Model berhasil 'menghafal' kebiasaan acak (*noise*) pelanggan pada data pelatihannya (*Training Set*), namun prediksinya meleset tak beraturan ketika dihadapkan pada data pengujian baru (*Validation Set*).\n",
        "   * Meskipun telah dilakukan *Hyperparameter Tuning* (seperti membatasi kedalaman pohon/`max_depth`), model tetap kesulitan menyeimbangkan pembelajarannya karena relasi antara logistik pengiriman (*Delivery time*, jarak) dengan besaran tip nyaris tidak memiliki pola yang rasional secara matematis.\n",
        "\n",
        "2. **Interpretasi Metrik Evaluasi:**\n",
        "   * **R² Score:** Menggambarkan seberapa besar variansi persentase tip yang dapat dijelaskan oleh fitur yang dimasukkan. Nilai **$R^2$ yang negatif/minus** merupakan temuan kunci yang mengindikasikan bahwa performa model **lebih buruk** dibandingkan jika kita menyingkirkan *Machine Learning* dan sekadar menebak nilai rata-rata tip secara pukul rata. Ini membuktikan bahwa fitur operasional seperti Waktu Tempuh dan Biaya Total memiliki *signal* (korelasi) yang terlampau lemah untuk memprediksi angka persentase tip secara presisi.\n",
        "   * **MAE (Mean Absolute Error) & RMSE (Root Mean Squared Error):** Menunjukkan deviasi/simpangan rata-rata dari tebakan model terhadap angka tip sebenarnya. Apabila skor RMSE sangat jauh melebihi MAE, ini menggarisbawahi bahwa tebakan model sangat sering melenceng tajam dari angka aktual, karena pelanggan bisa saja memberikan tip ekstrem besar atau malah nol sama sekali tanpa logika logistik yang kuat.\n",
        "\n",
        "3. **Analisis Pola Aktual vs Prediksi (Scatter Plot):**\n",
        "   * Garis putus-putus merah merepresentasikan kondisi ideal di mana nilai Tebakan sejalan dengan nilai Aktual. Semakin acak dan menyebarnya tebaran titik biru menjauhi garis merah, artinya tingkat kesalahan *error* model semakin tinggi.\n",
        "   * Persebaran yang nyaris tanpa bentuk ini mempertegas bahwa keputusan pelanggan lebih bersifat impulsif, kebiasaan personal, atau sangat dipengaruhi persentase *default* di layar aplikasi (seperti selalu mengklik opsi 10% atau 15%), alih-alih dihitung dari jarak atau durasi pesanan.\n",
        "\n",
        "4. **Kesimpulan Akademis & Dampak Bisnis:**\n",
        "   * **Insight Riset:** Eksperimen algoritma regresi ini bukan berarti gagal secara proses kerja, melainkan sukses mengungkap realitas bahwa tebakan nominal tip pelanggan bersifat sangat independen dari metrik performa jasa pesan-antar makanan di *dataset* ini.\n",
        "   * **Rekomendasi Bisnis:** *Platform* dilarang keras untuk membangun fitur prediksi angka Tip spesifik kepada kurir/driver sebelum mengambil pesanan, karena akurasi model yang merugikan (*minus*) ini berpotensi memberikan \"harapan palsu\" (estimasi tip terlalu besar padahal aslinya kecil). Jika analisa tip tetap ingin didorong, problem ini sebaiknya direduksi secara dramatis menjadi sekadar problem klasifikasi biner (*Apakah pesanan ini berpotensi memberikan Tip di atas rata-rata: Ya / Tidak*).\n"
    ]
    nb['cells'][target_idx]['source'] = new_source
    print(f"Updated cell {target_idx}")

with open('Tugas_Akhir__FINAL.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

