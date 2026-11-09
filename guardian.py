import time

def guardian():
    print("Luxiverse ha despertado...")
    while True:
        time.sleep(3600) # 1 hora
        print("Toma agua y respira.")

guardian()
