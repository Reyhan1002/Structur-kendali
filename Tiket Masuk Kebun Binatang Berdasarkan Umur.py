# Menghitung Tiket Masuk Kebun Binatang

total_harga = 0.0

while True:
    input_umur = input("masukkan umur: ")
    
    # Perulangan berhenti jika input kosong (tekan Enter)
    if input_umur == "":
        break
    
    umur = int(input_umur)
    
    # Pengondisian tarif tiket berdasarkan umur
    if umur <= 2:
        harga = 0.0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14.0
        print(f"Harga ${harga:.2f}")
    elif umur >= 65:
        harga = 18.0
        print(f"Harga ${harga:.2f}")
    else:
        harga = 23.0
        print(f"Harga ${harga:.2f}")
    
    total_harga += harga
    print(f"Running total: {total_harga:.2f}")

# Pembayaran dan menghitung uang kembalian
jumlah_uang = float(input("masukkan jumlah uang: "))
kembalian = jumlah_uang - total_harga
print(f"Running kembalian: {kembalian:.2f}")
