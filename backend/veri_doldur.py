from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Kilerimizin (Veritabanının) şifresi ve adresi
DATABASE_URL = "postgresql://admin:sifre123@localhost:5432/rota_app"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Adım 1: Kilerdeki rafımızın (Tablomuzun) şeklini çiziyoruz
class Mekan(Base):
    __tablename__ = "mekanlar"
    
    id = Column(Integer, primary_key=True, index=True)
    isim = Column(String, index=True)
    kategori = Column(String)
    enlem = Column(Float)   # Haritadaki Latitude (Kuzey-Güney)
    boylam = Column(Float)  # Haritadaki Longitude (Doğu-Batı)
    puan = Column(Float)

def sahte_verileri_ekle():
    print("Veritabanı tablosu hazırlanıyor...")
    # Tabloyu PostgreSQL içinde fiziksel olarak oluşturur
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Kilerde daha önce malzeme var mı diye kontrol edelim
    mevcut_mekan_sayisi = db.query(Mekan).count()
    if mevcut_mekan_sayisi > 0:
        print("Kilerde zaten mekanlar var! Tekrar eklemeye gerek yok. ✅")
        db.close()
        return

    # Adım 2: 3 Tane Gerçek Koordinatlı İstanbul Mekanı Hazırlayalım
    mekan1 = Mekan(isim="Moda Sahil Çay Bahçesi", kategori="Kafe", enlem=40.9796, boylam=29.0238, puan=4.8)
    mekan2 = Mekan(isim="Karaköy Güllüoğlu", kategori="Tatlıcı", enlem=41.0239, boylam=28.9774, puan=4.9)
    mekan3 = Mekan(isim="Beşiktaş Kahvaltıcılar Sokağı", kategori="Restoran", enlem=41.0425, boylam=29.0006, puan=4.5)

    # Adım 3: Mekanları kilere yerleştirip kapıyı kilitliyoruz (commit)
    db.add_all([mekan1, mekan2, mekan3])
    db.commit()
    db.close()
    
    print("🎉 3 yeni İstanbul mekanı başarıyla kilere (veritabanına) eklendi!")

if __name__ == "__main__":
    sahte_verileri_ekle()