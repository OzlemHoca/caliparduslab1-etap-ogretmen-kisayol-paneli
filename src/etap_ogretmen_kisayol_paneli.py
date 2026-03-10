#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAP Öğretmen Kısayol Paneli - İlk Prototip
ÇalıPardusLab1 / Pardus Hata Yakalama ve Öneri Yarışması 2026

Bu sürüm, öğretmenin ders sırasında kullanabileceği temel işlemler için
örnek bir kısayol paneli mantığını göstermek amacıyla hazırlanmıştır.
Gerçek sistem ayarlarını değiştirmez; simülasyon çıktıları verir.
"""


def baslik_yaz() -> None:
    print("=" * 55)
    print("ETAP ÖĞRETMEN KISAYOL PANELİ")
    print("=" * 55)
    print("Öğretmen için hızlı erişim yardımcı aracı\n")


def menu_goster() -> None:
    print("Lütfen bir işlem seçin:")
    print("1 - Beyaz tahta aracını aç")
    print("2 - Ekran görüntüsü al")
    print("3 - Ses seviyesini göster")
    print("4 - Ders klasörünü aç")
    print("5 - Sistem durumunu göster")
    print("6 - Çıkış")
    print()


def beyaz_tahta_ac() -> None:
    print("\n[Beyaz Tahta]")
    print("Beyaz tahta aracı açılıyor... (simülasyon)")
    print("Hazır.\n")


def ekran_goruntusu_al() -> None:
    print("\n[Ekran Görüntüsü]")
    print("Ekran görüntüsü alma işlemi başlatıldı... (simülasyon)")
    print("Görüntü kaydedildi.\n")


def ses_durumu_goster() -> None:
    print("\n[Ses Durumu]")
    print("Mevcut ses seviyesi: %70")
    print("Mikrofon durumu: Pasif")
    print()


def ders_klasoru_ac() -> None:
    print("\n[Ders Klasörü]")
    print("Ders materyalleri klasörü açılıyor... (simülasyon)")
    print("Klasör hazır.\n")


def sistem_durumu_goster() -> None:
    print("\n[Sistem Durumu]")
    print("Bağlantı durumu: Çevrim içi")
    print("Projeksiyon/ekran modu: Hazır")
    print("Kısayol paneli: Etkin")
    print()


def ana_program() -> None:
    baslik_yaz()

    while True:
        menu_goster()
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            beyaz_tahta_ac()
        elif secim == "2":
            ekran_goruntusu_al()
        elif secim == "3":
            ses_durumu_goster()
        elif secim == "4":
            ders_klasoru_ac()
        elif secim == "5":
            sistem_durumu_goster()
        elif secim == "6":
            print("\nProgram sonlandırıldı.")
            break
        else:
            print("\nGeçersiz seçim yaptınız. Lütfen tekrar deneyin.\n")


if __name__ == "__main__":
    ana_program()
