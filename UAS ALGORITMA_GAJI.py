"""
SHERLY FAUZIYAH SYAHARANI/20083000150/2F
07-07-2021
UAS ALGORITMA PEMROGRAMAN
"""

from datetime import date

def hitung_tunjangan_istri(golongan, gaji_pokok):
    if golongan == 1:
        return 0.01 * gaji_pokok
    
    if golongan == 2:
        return 0.03 * gaji_pokok

    if golongan == 3:
        return 0.05 * gaji_pokok


def hitung_tunjangan_anak(gaji_pokok):
    return 0.02 * gaji_pokok


def hitung_gaji_bruto(gaji_pokok, tunjangan_istri=None, tunjangan_anak=None):

    if tunjangan_istri != None and tunjangan_anak != None:
        return gaji_pokok + tunjangan_istri + tunjangan_anak
    
    if tunjangan_istri != None:
        return gaji_pokok + tunjangan_istri
    
    return gaji_pokok


def hitung_biaya_jabatan(gaji_bruto):
    return 0.005 * gaji_bruto


def hitung_gaji_karyawan(gaji_pokok, golongan, jenis_kelamin, status, punya_anak):

    iuran_pensiun = 15500
    iuran_organisasi = 3500
        
    if jenis_kelamin == 'LAKI-LAKI' and status == 'KAWIN' and punya_anak == 'YA':
        tunjangan_istri = hitung_tunjangan_istri(golongan, gaji_pokok)
        tunjangan_anak = hitung_tunjangan_anak(gaji_pokok)
        gaji_bruto = hitung_gaji_bruto(gaji_pokok, tunjangan_istri=tunjangan_istri, tunjangan_anak=tunjangan_anak)
        biaya_jabatan = hitung_biaya_jabatan(gaji_bruto)
        gaji_netto = gaji_bruto - (biaya_jabatan + iuran_organisasi + iuran_pensiun)
        return (tunjangan_istri, tunjangan_anak, gaji_bruto, biaya_jabatan, gaji_netto)
    
    if jenis_kelamin == 'LAKI-LAKI' and status == 'KAWIN' and punya_anak == 'TIDAK':
        tunjangan_istri = hitung_tunjangan_istri(golongan, gaji_pokok)
        gaji_bruto = hitung_gaji_bruto(gaji_pokok, tunjangan_istri=tunjangan_istri)
        biaya_jabatan = hitung_biaya_jabatan(gaji_bruto)
        gaji_netto = gaji_bruto - (biaya_jabatan + iuran_organisasi + iuran_pensiun)
        return (tunjangan_istri, 0, gaji_bruto, biaya_jabatan, gaji_netto)

        
    if jenis_kelamin == 'PEREMPUAN' and status == 'KAWIN' and punya_anak == 'YA':
        tunjangan_anak = hitung_tunjangan_anak(gaji_pokok)
        gaji_bruto = hitung_gaji_bruto(gaji_pokok, tunjangan_anak=tunjangan_anak)
        biaya_jabatan = hitung_biaya_jabatan(gaji_bruto)
        gaji_netto = gaji_bruto - (biaya_jabatan + iuran_organisasi + iuran_pensiun)
        return (0, tunjangan_anak, gaji_bruto, biaya_jabatan, gaji_netto)
        
    if status == 'BELUM KAWIN' and punya_anak == 'TIDAK':
        gaji_bruto = hitung_gaji_bruto(gaji_pokok)
        biaya_jabatan = hitung_biaya_jabatan(gaji_bruto)
        gaji_netto = gaji_bruto - (biaya_jabatan + iuran_organisasi + iuran_pensiun)
        return (0, 0, gaji_bruto, biaya_jabatan, gaji_netto)


def cetak_slip(nama, golongan, jenis_kelamin, status, gaji_pokok, hasil_gaji):
    tanggal = date.today()

    print('\n\t\t\t SLIP GAJI \t\t\t')
    print('\t\t Tanggal {} Bulan {} Tahun {} \t\t'.format(tanggal.day, tanggal.month, tanggal.year))
    print('Nama\t\t: {}'.format(nama))
    print('Golongan\t: {}'.format(golongan))
    print('Jenis Kelamin\t: {}'.format(jenis_kelamin))
    print('Status Kawin\t: {}'.format(status))
    print('Gaji Pokok\t: {}'.format(gaji_pokok))
    print('Tunjangan Istri\t: {}'.format(hasil_gaji[0]))
    print('Tunjangan Anak\t: {}'.format(hasil_gaji[1]))
    print('Gaji Bruto\t: {}'.format(hasil_gaji[2]))
    print('Biaya Jabatan\t: {}'.format(hasil_gaji[3]))
    print('Iuran Pensiun\t: 15500')
    print('Iuran Organisasi: 3500')
    print('Gaji Netto\t: {}'.format(hasil_gaji[4]))
    

def main(nama, golongan, jenis_kelamin, status, punya_anak):
    if int(golongan) == 1:
        gaji_pokok = 2500000
        golongan_satu = hitung_gaji_karyawan(gaji_pokok, int(golongan), jenis_kelamin, status, punya_anak)
        cetak_slip(nama, golongan, jenis_kelamin, status, gaji_pokok, golongan_satu)
    
    if int(golongan) == 2:
        gaji_pokok = 4500000
        golongan_dua = hitung_gaji_karyawan(gaji_pokok, int(golongan), jenis_kelamin, status, punya_anak)
        cetak_slip(nama, golongan, jenis_kelamin, status, gaji_pokok, golongan_dua)
    
    if int(golongan) == 3:
        gaji_pokok = 6500000
        golongan_tiga = hitung_gaji_karyawan(gaji_pokok, int(golongan), jenis_kelamin, status, punya_anak)
        cetak_slip(nama, golongan, jenis_kelamin, status, gaji_pokok, golongan_tiga)


if __name__ == '__main__':
    print('\t\t\tPerhitungan Gaji Karyawan CV. LOGOS')
    print('\n\t\t\t===================================\n')
    print('Silahkan masukkan data pokok seperti: Nama, Golongan, Jenis Kelamin, Status Pernikahan, dan Anak secara berurutan.')
    nama, golongan, jenis_kelamin, status, punya_anak = input('Pisahkan dengan koma:\n').split(',')
    main(nama, golongan, jenis_kelamin, status, punya_anak)

