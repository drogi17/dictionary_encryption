import random
import sys

key_list  =   [   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', 
                        'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ъ', 'э', 'ю', 'я', 'ы',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
                        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ъ', 'Э', 'Ю', 'Я', 'Ы',
                        ',', '.', '-', '=', ':', ';', '[', ']', '(', ')', '_', '*', '/', "'", '"', '?', '!', '$', '#', '&', '@', '|', '’', '^']


print('Made by drogi17')
def code(): 
    key_ncode   =   key_list[:]
    random.shuffle(key_ncode)
    try:
        word = input('Text: ')
    except UnicodeDecodeError:
        print('Error "UnicodeDecodeError".')
        sys.exit()
    if len(word) >= 2000:
        print("Unable to encode more than 2000 characters.")
        word = word[:2000]
    word_coded = ''
    ncode_dict = dict(zip(key_list[:], key_ncode))
    
    try:
        for char in word:
            word_coded += ncode_dict[char]
    except KeyError as Key_Error:
        print("Invalid character: " + str(Key_Error))
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()
    key = ''
    for char in key_ncode:
        key += char + '\\'
    print('')
    with open('key.txt', 'w') as f:
        f.write(key)
    with open('message.txt', 'w') as f:
        f.write(word_coded)
    print('KEY in key.txt')
    print('CODED WORD:\n')
    print(word_coded)



def decode():
    try:
        with open('key.txt', 'r') as f:
            key = f.read()
        with open('message.txt', 'r') as f:
            message = f.read()
    except:
        message = input('Cipher text: ')
        key = input('key: ')
    key = key.split('\\')
    del key[len(key)-1]
    word_decoded = ''
    decode_dict = dict(zip(key, key_list[:]))
    try:
        for char in message:
            word_decoded += decode_dict[char]
    except KeyError as Key_Error:
        print("Invalid character: " + str(Key_Error))
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()
    print('DECODED WORD:\n')
    print(word_decoded)
    f = open('decrypted.txt', 'w')
    f.write(word_decoded)
    f.close()

def new_mess(): 
    try:
        with open('key.txt', 'r') as f:
            key = f.read()
    except:
        key = input('key: ')
    key_ncode   =   key.split('\\')
    try:
        word = input('Text: ')
    except UnicodeDecodeError:
        print('Error "UnicodeDecodeError".')
        sys.exit()
    if len(word) >= 2000:
        print("Unable to encode more than 2000 characters.")
        word = word[:2000]
    word_coded = ''
    ncode_dict = dict(zip(key_list[:], key_ncode))
    
    try:
        for char in word:
            word_coded += ncode_dict[char]
    except KeyError as Key_Error:
        print("Invalid character: " + str(Key_Error))
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()
    key = ''
    for char in key_ncode:
        key += char + '\\'
    print('')
    with open('message.txt', 'w') as f:
        f.write(word_coded)
    print('CODED WORD:\n')
    print(word_coded)

def new_key(): 
    key_ncode = key_list[:]
    random.shuffle(key_ncode)
    key = ''
    for char in key_ncode:
        key += char + '\\'
    with open('key.txt', 'w') as f:
        f.write(key)
    print('KEY in key.txt')


try:
    doing = input('\nEncrypt message with new key(1)\nDecrypt message(2)\nNew message with key in key.txt file(3)\nNew encryption key(4)\n\nSelect: ') 

    if doing == '1':
        code()

    elif doing == '2':
        decode()

    elif doing == '3':
        new_mess()
    
    elif doing == '4':
        new_key()
except KeyboardInterrupt:
    pass
