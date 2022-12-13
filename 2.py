import random
import time


tanya = int(input("Main Berapa Kali: "))

loading = '''
Loading . . .
> > > > > > > > > ... 100%

Ngeflip koin . . .
'''

for huruf in loading:
  print(huruf,end='',flush=True)
  time.sleep(0.1)

nilai = 0

for i in range(tanya):
    flip = "Ngeflip koin lagi . . ."

    b=random.randint(0,1)

    if b == 0:
        koinnya = "gambar"
    else:
        koinnya = "angka"

    tebak = input("\nTebak koinnya: ")

    if tebak == koinnya:
        nilai += 1
        print(f"Benar, Skor kamu {nilai}\n")

        if i == tanya-1:
            print("Permainan Selesai")
            break
        else:
            for huruf in flip:
                print(huruf,end='',flush=True)
                time.sleep(0.1)
    else:
        print(f"Salah, Skor kamu {nilai}\n")

        if i == tanya-1:
            print("Permainan Selesai")
            break
        else:
            for huruf in flip:
                print(huruf,end='',flush=True)
                time.sleep(0.1)