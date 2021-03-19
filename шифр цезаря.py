msg = input('Введите текст: ')
key = int(input('Ключ '))
mode = input('encrypt\\decrypt: ')

SYMVOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ?!'


translete = ''

for symbol in msg:
    if symbol in SYMVOLS: 
        symbolIndex = SYMVOLS.find(symbol)
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        if translatedIndex >= len(SYMVOLS):
            translatedIndex -= len(SYMVOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMVOLS)

        translete += SYMVOLS[translatedIndex]
    else:
        translete += symbol

print(translete)
