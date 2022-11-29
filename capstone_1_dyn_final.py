# DYN
# Data Awal Skor Akademik

list_akademik = [
      {'NIS':'101','Nama':'Lemmy','Program':'Data Science','Nilai1':'80','Nilai2':'70','Nilai3':'60','Kelas':'C'},
      {'NIS':'102','Nama':'Luki','Program':'Data Science','Nilai1':'70','Nilai2':'60','Nilai3':'80','Kelas':'C'},
      {'NIS':'103','Nama':'Echa','Program':'Data Science','Nilai1':'90','Nilai2':'80','Nilai3':'70','Kelas':'C'}
]

# print(list_akademik)
# ===============================================================================================
# Menu 1
# Memberikan pilihan menampilkan semua siswa atau siswa terpilih

def read():
    while True:    
        inputRead = (int(input('''
            Menu Menampilkan Data Nilai Siswa:
                1. Menampilkan data seluruh siswa
                2. Menampilkan data siswa terpilih
                3. Kembali ke Menu Utama
            Masukkan angka menu yang ingin dijalankan:''')))
        if inputRead == 1:
            tampilkan_semua()
        elif inputRead == 2:
            cari_siswa()
        elif inputRead == 3:
            break
        else:
            print("Menu tidak tersedia, pilih 1-3 ")

# ===============================
# Menu 1: sub menu 1
# Menampilkan seluruh data siswa

def tampilkan_semua():

    print('\nDaftar Nilai Seluruh Siswa')
    print(f'{"NIS":<9}| {"Nama":<9}| {"Program":<14}| {"Nilai1":<9}| {"Nilai2":<9}| {"Nilai3":<9} | {"Kelas":<4}')
    for i in range(len(list_akademik )):
        nis = list_akademik[i]['NIS']
        nama = list_akademik[i]['Nama']
        program = list_akademik[i]['Program']
        nilai1 = list_akademik[i] ['Nilai1']
        nilai2 = list_akademik[i] ['Nilai2']
        nilai3 = list_akademik[i] ['Nilai3']
        kelas = list_akademik[i] ['Kelas']
        print(f'{nis:<9}| {nama:<9}| {program:<14}| {nilai1:<9}| {nilai2:<9}| {nilai3:<9} | {kelas:<4}')
        print()

# ================================
# Menu 1: sub menu 2
# Menampilkan data siswa terpilih

def cari_siswa():
    masukan_nis = input('Masukkan NIS yang dicari!: ') 
    for siswa in list_akademik:
        if siswa['NIS'] == masukan_nis:
           print(f'{"NIS":<9}| {"Nama":<9}| {"Program":<14}| {"Nilai1":<9}| {"Nilai2":<9}| {"Nilai3":<9} | {"Kelas":<4}')
           print(f'{siswa["NIS"]:<9}|{siswa["Nama"]:<9}| {siswa["Program"]:<14}| {siswa["Nilai1"]:<9}| {siswa["Nilai2"]:<9}| {siswa["Nilai3"]:<9}| {siswa["Kelas"]:<4}')
           break
        elif siswa['NIS'] != masukan_nis:
            print('NIS tidak ditemukan, mohon masukkan NIS yang benar!')
        else:
            home_page()
            

# ==========================================
# Tambah Data Siswa Baru

def Add():
    inputAdd = (int(input('''
        Pilih Tambah Data Nilai Siswa:
            1. Menambah Daftar Nilai Siswa
            2. Kembali ke menu utama
        Silahkan masukkan angka yg diinginkan:''')))
    if inputAdd == 1:
        AddDataNilaiSiswa = (input("\n\tMasukkan NIS Baru:"))
        
        for i in list_akademik:
            if(i['NIS']) == AddDataNilaiSiswa :
                print("\n\tData sudah tersimpan!")
            else:
                NISBaru = int(input("\tSilahkan masukkan NIS:"))
                NamaBaru = input("\tSilahkan masukkan Nama Siswa:")
                ProgramBaru = input("\tSilahkan masukkan Program:")
                Nilai1Baru = int(input("\tSilahkan masukkan Nilai1:"))
                Nilai2Baru = int(input("\tSilahkan masukkan Nilai2:"))
                Nilai3Baru = int(input("\tSilahkan masukkan Nilai3:"))
                KelasBaru = input("\tSilahkan masukkan Kelas:")
                DaftarNilaiSiswaBaru={'NIS': NISBaru,'Nama': NamaBaru,'Program': ProgramBaru,'Nilai1': Nilai1Baru,'Nilai2': Nilai2Baru,'Nilai3': Nilai3Baru,'Kelas': KelasBaru}
                Konfirmasi = input(" Yakin mau disimpan? Ya / Tdk? ")
                if Konfirmasi == 'Ya':
                    list_akademik.append(DaftarNilaiSiswaBaru)
                    tampilkan_semua()
                    break
                else:
                    print("Kita kembali ke Menu Utama")
                    home_page()
    elif inputAdd == 2:
        home_page()
# ===============================================================================================
# Update Data Siswa

def update():
    inputUpdt = (int(input('''
        Daftar Menu Update:
            1. Mengupdate Daftar Nilai Siswa
            2. Kembali ke menu utama
        Silahkan masukkan angka yg diinginkan: ''')))
    
    if inputUpdt == 1:
        tampilkan_semua()
        print(f'''
        Silahkan pilih Data yg ingin diganti ( Masukkan NIS ) : 
        1. NIS
        2. Nama
        3. Program
        4. Nilai1
        5. Nilai2
        6. Nilai3
        7. Kelas
        
        ''')
        Input_NIS = input('Masukkan NIS yg ingin diubah: ')
        # Masukkan Function utk menampilkan sebuah Baris ( Tambahkan Menu 1 Sub 2)


        list_NIS = []
        for siswa in list_akademik:
            list_NIS.append(siswa['NIS'])
        # print(list_NIS)

        # Klo NIS ada di Data Set
        if Input_NIS in list_NIS:
            # print('Ganti')
            
            for siswa in list_akademik:
                if siswa['NIS'] == Input_NIS:
                    Input_Kolom = input('Masukkan Kolom yg ingin diubah: ').capitalize()
                    Input_Nilai = input(f'Masukkan {Input_Kolom} Baru: ')
                    siswa[Input_Kolom] = Input_Nilai
                    print('Data sudah berubah')
                    break
                else:
                    print('Nomor NIS tidak dapat dicari yang anda tidak ditemukan')

    elif inputUpdt ==2:
        home_page()
    else:
        update()


# ===============================================================================================
# Delete Data Siswa

def hapus_datasiswa():
    inputDel = int(input(f'''
        Daftar Menu Hapus:
            1. Menghapus Daftar Nilai Siswa
            2. Kembali ke menu utama
        Silahkan masukkan angka yg diinginkan: '''))
    if inputDel == 1:
        DelDataNilaiSiswa = (input("\n\tMasukkan NIS Siswa yg ingin dihapus: "))
        for i in range(len(list_akademik)):
            if list_akademik[i]['NIS'] == DelDataNilaiSiswa:
                tampilkan_semua()
                del_siswa = input('Apakah kamu yakin hapus data siswa? ( Ya / Tdk ): ')
                if del_siswa.upper() == 'YA':
                    del list_akademik[i]
                    tampilkan_semua()
                    break
                elif del_siswa.upper() == 'TDK':
                    print('Kembali ke Menu Utama')
                    home_page()
    elif inputDel == 2:
        home_page()
    else:
        hapus_datasiswa()
        # printing result
        # print ("List after deletion of dictionary : " + str(list_akademik))

    # if inputDel == 1:f m
    #         if siswa['NIS'] == DelDataNilaiSiswa:
    #             print(f'{"NIS":<9}| {"Nama":<9}| {"Program":<14}| {"Nilai1":<9}| {"Nilai2":<9}| {"Nilai3":<9} | {"Kelas":<4}')
    #             print(f'{siswa["NIS"]:<9}|{siswa["Nama"]:<9}| {siswa["Program"]:<14}| {siswa["Nilai1"]:<9}| {siswa["Nilai2"]:<9}| {siswa["Nilai3"]:<9}| {siswa["Kelas"]:<4}')
    #             del_siswa = input('Apakah kamu yakin hapus data siswa?(y/no): ')
    #             for index in list_akademik:


    #         else:
    #             print("Data Tidak Tersedia, pilih 101-103 ")
    #             break
    # else:
    #     print('tes')






# ===============================================================================================
# Home page / menu utama
# berisi daftar menu


def home_page():
    while True:
        print('''
        Menu Utama :

        1. Lihat Data Siswa

        2. Tambahkan Data Siswa 

        3. Ubah Data Siswa

        4. Hapus Data Siswa

        5. Sayonara
        

        ''')
        pilih_menu = int(input("Silahkan pilih menu yang ingin dijalankan: "))
        if pilih_menu == 1:
            read()
        elif pilih_menu == 2:
            Add()
        elif pilih_menu == 3:
            update()
        elif pilih_menu == 4:
            hapus_datasiswa()
        elif pilih_menu == 5:
            print ("Sayonara")
            exit()
        else:
            print("Hayoo, menu yang kamu cari ga ada lhoo!")
            continue
            

home_page()


