anak = ['wanti', 'risa', 'riska', 'wiwin']

for a in anak: #cara mudah tidak bisa mengirim index di perulangan
    print(f'hai {a}')

for a in range(0, len(anak)): #cara ribet bisa keuntungannya bisa akses nilai indexnya
    print(f'{a+1} hai {anak[a]}')