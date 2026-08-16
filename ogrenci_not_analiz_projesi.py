"""
Öğrenci Not Analiz Projesi


Plan / Program: 
1. Veri Toplama: Öğrencilerin notlarını içeren bir veri seti oluşturulacak veya mevcut bir veri seti kullanılacak.
2. Veri Temizleme: Eksik veya hatalı veriler temizlenecek ve veri seti analiz için hazır hale getirilecek.
3. Veri Analizi: Öğrencilerin notları üzerinde istatistiksel analizler
4. OOP ile Kodlama: Proje, nesne yönelimli programlama (OOP) prensiplerine uygun olarak sınıflar ve nesneler kullanılarak geliştirilecek.
5. Görselleştirme: Analiz sonuçları grafikler ve tablolar ile görselleştirilecek.
6. Hata Yönetimi: Hatalar ve istisnalar uygun şekilde ele alınacak ve kullanıcıya bilgilendirici mesajlar verilecek.


Veri Seti:
isim, yas, bolum, not

Kurulumlar: 
pip install pandas, matplotlib, numpy

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class OgrenciNotAnalizSistemi:
    """
    Öğrenci Not Analiz Sistemi okuyan, analiz eden, filtreleyen ve görselleştiren bir sınıftır.
    
    Attributes:
        dosya_yolu: Öğrenci notlarını içeren CSV dosyasının yolu.
        veri_seti (pd.DataFrame): Öğrenci notlarını içeren veri seti. 
    
    """
    
    def __init__(self, dosya_yolu):
        self.dosya_yolu = dosya_yolu
        self.veri_seti = None

    def veri_okuma(self):
        """
        CSV dosyasını okuyarak veri setini oluşturur ve df içine yükler. Eğer dosya bulunamazsa hata mesajı verir.
        """
        try:
            self.veri_seti = pd.read_csv(self.dosya_yolu)

            if self.veri_seti.empty:
                raise ValueError("csv dosyası boş")
            
            # gerekli sütunları tanımla
            gerekli_sutunlar = {"isim", "yas", "bolum", "note"}

            # dosyada gerekli sütunlar var mı kontrol edelim
            if not gerekli_sutunlar.issubset(self.veri_seti.columns):
                raise ValueError(
                    f"csv dosyasında gerekli sütunlar eksik"
                    f"Gerekli sütunlar: {gerekli_sutunlar}"
                )
            
            self.veri_seti["note"] = pd.to_numeric(self.veri_seti["note"], errors = "raise")
            print("Veri başarıyla okundu")
            print(self.veri_seti) 
            
        except FileNotFoundError:
            print(f"hata: {self.dosya_yolu} bulunamadı")
        except pd.errors.EmptyDataError:
            print("csv dosyası boş")
        except ValueError as error:
            print(f"hata: {error}")
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")
            
            
            
    def numpy_ile_hesaplama(self):
        """
        Numpy kullanarak notların ortalamasını, standart sapmasını, en düşük not, en yüksek not hesaplar.
        
        """
        try:
            if self.veri_seti is None:
                raise ValueError("Veri seti yüklenmedi. Lütfen önce veri setini yükleyin.")
            
            notlar = self.veri_seti["note"].to_numpy()  #notları numpy arrayine çevirme
            
            print(f"Numpy ile hesaplanan istatistikler:")
            print(f"Ortalama {np.mean(notlar)}")
            print(f"En yüksek not {np.max(notlar)}")
            print(f"En düşük not {np.min(notlar)}")
            print(f"Standart sapma {np.std(notlar)}")
            
        except ValueError as hata:
            print(f"hata: {hata}")
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu. {e}")
            
            
    def pandas_ile_filtreleme(self):
        """
        Pandas kullanarak veri setini filtreler ve belirtilen bölüm veya yaşa göre öğrenci notlarını döndürür.
        
        notu 80'in üzerinde olan öğrencileri filtreler.
        yaşı 22 olan öğrencileri filtreler.
        bölüm adı "Bilgisayar Mühendisliği" olan öğrencileri filtreler.
        
        Args:
            bolum (str, optional): Filtrelenecek bölüm adı. Varsayılan olarak None.
            yas (int, optional): Filtrelenecek yaş değeri. Varsayılan olarak None.
        
        Returns:
            pd.DataFrame: Filtrelenmiş öğrenci notlarını içeren veri çerçevesi.
        """
        try:
            if self.veri_seti is None:
                raise ValueError("Veri seti yüklenmedi. Lütfen önce veri setini yükleyin.")
            
            print("Pandas ile filtreleme işlemi başlatıldı.")
            
            #yaşı 22 olan öğrencileri filtreleme
            yasi_buyuk_olanlar = self.veri_seti[self.veri_seti["yas"] > 22]
            print(f"22 yaşından büyük olanlar: \n{yasi_buyuk_olanlar}")
            
            #bölüm adı "Bilgisayar Mühendisliği" olan öğrencileri filtreleme
            filtrelenmis_veri = self.veri_seti[self.veri_seti["bolum"] == "Bilgisayar Mühendisliği"]
            print("Bölümü 'Bilgisayar Mühendisliği' olan öğrenciler:")
            print(filtrelenmis_veri)
            
            #notu 80'in üzerinde olan öğrencileri filtreleme
            yuksek_notlu = self.veri_seti[self.veri_seti["note"] > 80]
            print(f"Notu 80'in üzerinde olan öğrenciler: \n{yuksek_notlu} ")
            print(yuksek_notlu)
            
        except ValueError as hata:
            print(f"hata: {hata}")
        except Exception as e:
            print(f"Beklenmeyen bir hata: {e}")
            
            

    def grafik_gorsellestirme(self):
        """
        veri notlarını sütun grafiği ile görselleştirme
        
        """
        
        try:
            if self.veri_seti is None:
                raise ValueError("Veri seti yüklenmedi. Lütfen önce veri setini yükleyin.")
            
            #grafik boyutunu ayarlama ve sütun grafiği oluşturma
            plt.figure(figsize=(10, 6))
            #isim ve not x y sütunlarını kullanarak bar grafiği oluşturma
            plt.bar(self.veri_seti["isim"], self.veri_seti["note"], color='skyblue')
            plt.xlabel("Öğrenci İsimleri")
            plt.ylabel("Notlar")
            plt.title("Öğrenci Notları Grafiği")
            plt.xticks(rotation=45)
            
            plt.tight_layout() #grafiğin düzenli görünmesini sağlama
            plt.show()
        
        except Exception as e:
            print(f"hata: {e}")
            
            
    def tum_analizleri_yap(self):
        """
        Tüm analizleri sırasıyla yapar: veri okuma, numpy ile hesaplama, pandas ile filtreleme ve grafik görselleştirme.
        """
        
        #1. veriyi okuma
        self.veri_okuma()
        
        #eğer veri yüklenmezse diğer analizleri yapma
        if self.veri_seti is None:
            print("Veri seti yüklenemediği için diğer analizler yapılmayacak.")
            return 
        
        #2. numpy ile hesaplama 
        self.numpy_ile_hesaplama()
        
        #3. pandas ile filtreleme
        self.pandas_ile_filtreleme()
        
        #4. grafik görselleştirme
        self.grafik_gorsellestirme()
        
#programın başlangıç noktası
if __name__ == "__main__":
    #CSV dosyasının yolu
    dosya_yolu = "ogrenci_notlari.csv"
    
    #OgrenciNotAnalizSistemi sınıfından bir nesne oluşturma
    analiz_sistemi = OgrenciNotAnalizSistemi(dosya_yolu)
    
    #Tüm analizleri yapma
    analiz_sistemi.tum_analizleri_yap()
    