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

    koin=['gambar', 'angka']
    b=random.randint(0,1)

    tebak = input("\nTebak koinnya: ")

    if tebak == koin[b]:
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