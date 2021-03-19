msg = input('Введите текст: ')
SYMVOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ?!'

for key in range(len(SYMVOLS)):
    transtaded = ''
    for symdol in msg:
        if symdol in SYMVOLS:
            simbolIndex = SYMVOLS.find(symdol)
            transtadedIndex = simbolIndex - key
            if transtadedIndex < 0:
                transtadedIndex += len(SYMVOLS)
            transtaded += SYMVOLS[transtadedIndex]
        else:
            transtaded += symdol
    print(f'Key #{key}: {transtaded}')
