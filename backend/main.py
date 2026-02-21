from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

# Docker'daki veritabanı adresimiz
DATABASE_URL = "postgresql://admin:sifre123@localhost:5432/rota_app"

@app.get("/")
def read_root():
    return {"mesaj": "Selam İstanbul! Backend ve API çalışıyor 🚀"}

@app.get("/db-test")
def test_db():
    try:
        # Veritabanı motorunu oluştur
        engine = create_engine(DATABASE_URL)
        
        # Bağlanmayı dene
        with engine.connect() as conn:
            # Basit bir SQL sorgusu ile versiyonu sor
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            return {"durum": "BAŞARILI ✅", "db_versiyonu": version}
            
    except Exception as e:
        return {"durum": "HATA ❌", "hata_detayi": str(e)}