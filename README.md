# Deskripsi
Skrip notif-nadine melaporkan kondisi presensi Nadine Anda, melalui pushbullet.com. 

# Prasyarat
Membuat akun [pushbullet.com](https://www.pushbullet.com/) dan menginstall aplikasi PushBullet di perangkat Anda (Android ataupun iOS). Buat token pushbullet melalui menu [Settings](https://www.pushbullet.com/#settings).

# Instalasi
1. Penuhi requirement import khususnya selenium dan Chrome webdriver.
2. Isikan username dan password Nadine pada variabel `username` dan `password`.
3. Isikan token pushbullet.com pada variabel `pushbullet_token`

# Cara Menjalankan
Jalankan dengan perintah:
`python3 notif-nadine.py`

Jika semua berjalan lancar, akan muncul Push Notification di perangkat Anda yang berisi informasi presensi Anda hari ini di aplikasi Nadine.

![Notif](https://raw.githubusercontent.com/BetaUliansyah/notif-nadine/main/img/notif-nadine.jpg)

# Cronjob
Perintah ini dapat dijalankan secara terjadwal melalui cronjob seperti berikut ini:
```
30 7 * * 1-5 python3 /home/beta/monabsensi/notif-nadine.py
30 17 * * 1-5 python3 /home/beta/monabsensi/notif-nadine.py
```

Cronjob di atas berarti menjalankan skrip setiap hari kerja (1-5 berarti Senin sampai Jumat) tiap jam 7.30 pagi dan tiap jam 17.30 sore.
