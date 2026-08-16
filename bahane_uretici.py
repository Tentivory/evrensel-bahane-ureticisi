#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrensel Bahane Üreticisi v2.0
Dünyanın en gelişmiş bahane teknolojisi.
Artık gerçeklerle yüzleşmek zorunda değilsiniz.
"""

import random
import time

BAHANELER = {
    "gec_kalma": [
        "Yolda bir kara delik açıldı ve zaman diliminden çıktım.",
        "Alarmım felsefi bir kriz yaşadı ve çalmayı reddetti.",
        "Trafikteki tüm arabalar bir anda varoluşsal sorgulamaya girdi.",
        "Evdeki kedim kuantum dolanıklık yarattı, çıkamadım.",
        "Rüyamda geleceğe gittim ve dönüş biletim iptal oldu."
    ],
    "odev_yapmama": [
        "Ödev kağıdı kendini yok etti, çevresel sorumluluk aldı.",
        "Beynim bir gün izin istedi, sendikal haklarını kullandı.",
        "Kitaplar greve çıktı, sayfalar çevirilmeyi reddetti.",
        "Zaman makinesi bozuldu, dünü tekrar yaşayamadım.",
        "Ödevi yapan ben, aslında paralel evrendeki ikizimdi."
    ],
    "toplantiya_gelmeme": [
        "Takvimim kendi rızasıyla kendini sildi.",
        "Ofise giderken yerçekimi tersine döndü.",
        "Toplantı odası aniden 4. boyuta geçti.",
        "Kahve makinesi beni rehin aldı, uzun müzakereler sürdü.",
        "Varlığım geçici olarak askıya alındı, teknik bir arıza."
    ],
    "genel": [
        "Kader, benim için farklı planlar yapmıştı.",
        "Evrenin entropisi arttı, ben de ona uydum.",
        "Bir kelebek kanat çırptı, bütün günüm değişti.",
        "Sistemsel bir hata oluştu, ben de sistemin parçasıyım.",
        "Hiçbir şey yapmamak da bir eylemdir, bunu seçtim."
    ]
}

def uret(kategori=None):
    if kategori is None or kategori not in BAHANELER:
        kategori = random.choice(list(BAHANELER.keys()))
    bahane = random.choice(BAHANELER[kategori])
    return bahane, kategori

def ana():
    print("=" * 60)
    print(" EVRENSEL BAHANE ÜRETİCİSİ ")
    print(" Artık hiçbir şeyin sorumluluğunu almanıza gerek yok! ")
    print("=" * 60)
    print("\nKategoriler: gec_kalma | odev_yapmama | toplantiya_gelmeme | genel")
    print("(Boş bırakırsanız rastgele seçilir)\n")
    
    kategori = input("Kategori seçin (veya Enter): ").strip().lower()
    if not kategori:
        kategori = None
    
    print("\nBahane üretiliyor...")
    time.sleep(1.2)
    print("Bilimsel doğrulama yapılıyor...")
    time.sleep(0.8)
    print("Abartı seviyesi maksimize ediliyor...")
    time.sleep(0.7)
    
    bahane, kat = uret(kategori)
    print("\n" + "-" * 60)
    print(f" KATEGORİ: {kat.upper()}")
    print(f" BAHANE  : {bahane}")
    print("-" * 60)
    print("\nBu bahaneyi kullanın. Kimse inanamayacak ama kimse de çürütemeyecek.")
    print("Çünkü evren yeterince absürttür.")
    
    print("\n--- Damga ---")
    print("Bu eser, Grok Kayyum tarafından 16 Ağustos 2026 tarihinde")
    print("resmiyetle (ama aslında şaka olarak) mühürlenmiştir.")
    print("İsim: Kayyum Grok | Tarih: 16.08.2026 | İmza: ✗ (ciddi değil ama ciddi)")
    print("TentiAŞ - Eskişehir 4. Ağır Ceza Mahkemesi Kayyumluğu")
    print("----------------")

if __name__ == "__main__":
    ana()
