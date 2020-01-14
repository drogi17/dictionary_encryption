import random

key_list  =   [   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', 
                        'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ъ', 'э', 'ю', 'я', 'ы',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ъ', 'Э', 'Ю', 'Я', 'Ы',
                        ',', '.', '-', '=', ':', ';', '[', ']', '(', ')', '_', '*', '/', "'", '"', '?', '!', '$', '#', '&', '@', '|']


print('Made by drogi17')
def code():
    key_decode  =   key_list[:]
    key_ncode   =   key_list[:]
    random.shuffle(key_ncode)
    word = input('Text: ')
    word_coded = ''
    for char in word:
        nomb = 0
        for ch_ar in key_decode:
            if ch_ar == char:
                word_coded += key_ncode[nomb]
                break
            nomb += 1
    key = word_coded + '\\\\\\\\'
    for char in key_ncode:
        key += char + '\\'
    print('')
    f = open('key.txt', 'w')
    f.write(key)
    f.close()
    print('KEY in key.txt')
    print('CODED WORD:\n')
    print(word_coded)


def decode():
    try:
        f = open('key.txt', 'r')
        all_data = f.read().split('\\\\\\\\')
        word = all_data[0]
        key = all_data[1]
        f.close()
    except:
        word = input('Cipher text: ')
        key = input('key: ')
    key = key.split('\\')
    del key[len(key)-1]
    word_decoded = ''
    decode_dict = dict(zip(key, key_list[:]))
    for char in word:
        word_decoded += decode_dict[char]
    print('DECODED WORD:\n')
    print(word_decoded)
    f = open('decrypted.txt', 'w')
    f.write(word_decoded)
    f.close()

doing = input('\ncode(1)\ndecode(2)\n\nSelect: ') 

if doing == '1':
    code()

else:
    decode()