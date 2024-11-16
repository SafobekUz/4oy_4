import psycopg2

db = psycopg2.connect(
    database='magazin',
    user='postgres',
    host='localhost',
    password='1'
)
cursor = db.cursor()

#1.1
cursor.execute("""
CREATE TABLE IF NOT EXISTS avtomobillar (
    id SERIAL PRIMARY KEY,
    nomi VARCHAR(100) NOT NULL,
    model TEXT,
    yil INTEGER,
    narx NUMERIC(12, 2),
    mavjudmi BOOL DEFAULT TRUE
);
""")

#1.2
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientlar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    familiya VARCHAR(50),
    telefon CHAR(13),
    manzil TEXT
);
""")

#1.3
cursor.execute("""
CREATE TABLE IF NOT EXISTS buyurtmalar (
    id SERIAL PRIMARY KEY,
    avtomobil_id INTEGER REFERENCES avtomobillar(id),
    client_id INTEGER REFERENCES clientlar(id),
    sana DATE NOT NULL,
    umumiy_narx NUMERIC(12, 2)
);
""")

#1.4
cursor.execute("""
CREATE TABLE IF NOT EXISTS xodimlar (
    id SERIAL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    lavozim VARCHAR(50),
    maosh NUMERIC(10, 2)
);
""")

db.commit()
print("Jadvallar yaratildi!")

#2.1
cursor.execute("""
ALTER TABLE clientlar
ADD COLUMN email VARCHAR(100);
""")

#2.2
cursor.execute("""
ALTER TABLE clientlar
RENAME COLUMN ism TO ism_klient;
""")

#2.3
cursor.execute("""
ALTER TABLE clientlar
RENAME TO mijozlar;
""")

db.commit()
print("Jadvalga o'zgartirishlar kiritildi!")

#3.1
cursor.execute("""
INSERT INTO avtomobillar (nomi, model, yil, narx)
VALUES
    ('Chevrolet', 'Malibu', 2022, 25000.00),
    ('Toyota', 'Camry', 2021, 30000.00),
    ('BMW', 'X5', 2020, 50000.00);
""")

cursor.execute("""
INSERT INTO mijozlar (ism_klient, familiya, telefon, manzil, email)
VALUES
    ('Ali', 'Valiyev', '+998901234567', 'Toshkent', 'ali@gmail.com'),
    ('Murod', 'Abduqodirov', '+998901111111', 'Samarqand', 'murod@gmail.com');
""")

cursor.execute("""
INSERT INTO xodimlar (ism, lavozim, maosh)
VALUES
    ('Jasur', 'Manager', 500.00),
    ('Aliya', 'Sotuvchi', 400.00);
""")

db.commit()
print("Ma'lumotlar kiritildi!")

#4.1
cursor.execute("""
UPDATE xodimlar
SET ism = 'Jamshid'
WHERE id = 1;
""")

cursor.execute("""
UPDATE xodimlar
SET ism = 'Aziza'
WHERE id = 2;
""")

db.commit()
print("Ma'lumotlar o'zgartirildi!")

#5.1
cursor.execute("""
DELETE FROM xodimlar
WHERE id = 1;
""")

db.commit()
print("Ma'lumotlar o'chirildi!")

#6.1
tables = ['avtomobillar', 'mijozlar', 'buyurtmalar', 'xodimlar']

for table in tables:
    cursor.execute(f"SELECT * FROM {table};")
    records = cursor.fetchall()
    print(f"\n{table} jadvali:")
    for record in records:
        print(record)

cursor.close()
db.close()
print("\nBarcha ma'lumotlar ko'rib chiqildi!")



