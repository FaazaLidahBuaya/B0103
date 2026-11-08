# --- 1. Variabel profil karakter ---
nama_hero = "Arthas"            # String
level = 10                      # Integer
hp = 250.5                      # Float
is_alive = True                 # Boolean
inventory = ["Pedang Baja", "Busur Panjang", "Kapak Perang"]  # List
atribut = {"kekuatan": 80, "kelincahan": 65}                  # Dictionary

# --- 2. Tampilkan seluruh informasi karakter ---
print("=== PROFIL KARAKTER ===")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Hidup     :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

# --- 3. Tampilkan tipe data masing-masing variabel ---
print("\n=== TIPE DATA ===")
print("Tipe nama_hero :", type(nama_hero))
print("Tipe level     :", type(level))
print("Tipe hp        :", type(hp))
print("Tipe is_alive  :", type(is_alive))
print("Tipe inventory :", type(inventory))
print("Tipe atribut   :", type(atribut))

# --- 4. Aksi karakter ---
# a. Mendapatkan item baru
inventory.append("Ramuan HP")

# b. Naik level: konversi ke float lalu tambah 0.5
level = float(level)
level = level + 0.5

# --- 5. Cetak informasi terbaru ---
print("\n=== PROFIL KARAKTER (TERBARU) ===")
print("Nama Hero :", nama_hero)
print("Level     :", level, "->", type(level))
print("HP        :", hp)
print("Hidup     :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)