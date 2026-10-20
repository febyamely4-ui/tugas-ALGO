#input
nilai_tugas = 90
nilai_UTS = 80
nilai_UAS = 88
Kehadiran = 90
#menghitung nilai akhir
nilai_akhir =(0.2 * 90) + (0.3 * 80) + (0.5 * 88)
print("Nilai Akhir:", nilai_akhir)
if nilai_akhir < 60 and Kehadiran < 75:
    print("BELUM LULUS")
#menentukan kelulusan dengan predikat
elif nilai_akhir >= 85 and Kehadiran >= 90 and nilai_akhir % 2 == 0:  
    print("LULUS DENGAN PREDIKAT")
else:
    print("LULUS")
