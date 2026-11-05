
#input
jumlah_mahasiswa = int(input("Jumlah mahasiswa: "))

if jumlah_mahasiswa > 0 and jumlah_mahasiswa <= 10:
      total_nilai = 0

#perhitungan
      for i in range(jumlah_mahasiswa):
        nilai = int(input(f"Masukkan Nilai Mahasiswa {i + 1}:"))
        total_nilai = total_nilai + nilai
        
#Rata-rata
      rata_rata = total_nilai / jumlah_mahasiswa
      print("Rata-rata:", rata_rata)
  
else: 
  print("Jumlah Mahasiswa tidak valid, Min 1 dan Max 10")