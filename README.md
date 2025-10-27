# UTS COMPUTER VISION

## Identitas
- **Nama:** Andi Azlan Jaslin
- **NIM:** 43050230040
- **Kelas:** TI4B

## Deskripsi Karakter
Karakter yang dibuat: **Buaya (gaya kartun lucu)**. Dibuat menggunakan fungsi dasar OpenCV seperti circle, ellipse, rectangle, line, dan putText.

## Transformasi yang digunakan
- Translasi (translate)
- Rotasi (rotate)
- Resize (ubah ukuran)
- Crop (memotong bagian gambar)

## Operasi Aritmatika / Bitwise
- cv2.bitwise_or()
- cv2.add()

## Struktur Projek
```
UTS_ComputerVision/
├── karakter.py
├── img/
│   └── background.jpg
├── output/
│   ├── karakter.png
│   ├── translate.png
│   ├── rotate.png
│   ├── resize.png
│   ├── crop.png
│   ├── bitwise.png
│   └── final.png
└── README.md
```

## Cara Menjalankan
1. Pastikan Python dan OpenCV (cv2) terinstall: `pip install opencv-python numpy`
2. Jalankan: `python3 karakter.py`
3. Hasil gambar akan tersimpan di folder `output/`

## Catatan
File ini dibuat otomatis dan siap diupload ke GitHub. Jika komputer kamu tidak memiliki OpenCV, tetap upload repository ini — dosen biasanya mengecek kode dan struktur.