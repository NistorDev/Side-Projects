crip = input('Introduceti text: ')
format1 = []
def transforma_in_hex(crip):
    for i in crip:
        f = format(ord(i),'x')
        format1.append(f)
            
    return format1

transformat = transforma_in_hex(crip)
# print('form_crip_hex')
print("Transformat in text: ",transformat)

def transforma_in_binar(f):
    res1 = []
    
    for f1 in f:
        res = "{0:08b}".format(int(f1, 16))
        
        res1.append(res)
        # print(res1)
    return res1

transf_bin = transforma_in_binar(transformat)
# print('form_crip_bin')
# print(transf_bin)

# 1 trandform list into binar and slice last 5 bits to right
concat = ''.join(str(x) for x in transf_bin)
print("Transformat in binar: ", concat)
ult5 = concat[-5:]

fara5 = concat[:-5]

# print(ult5)
# print(fara5)

schimba5 = ult5+fara5
# print('concat ultimele 5')
print("Deplasare la dreapta ultimele 5 pozitii: ",schimba5)
# 2. efectuează o inversare a biților multiplu de 3 din șirul obtinut la pasul anterior;

def schimba_bit3(binary_list):
    toggled_list = []
    for i, bit in enumerate(binary_list):
        # Check if the index is divisible by 3 (starting from 0)
        if (i + 1) % 3 == 0:
            # Toggle the bit: 0 -> 1, 1 -> 0
            toggled_list.append('0' if bit == '1' else '1')
        else:
            toggled_list.append(bit)
    return toggled_list

# 3. efectuează o deplasare ciclică la dreapta cu șapte poziții, a șirului de biți;
temp_toggle3 = schimba_bit3(schimba5)
# print('toggle_every_third bit')
# print(temp_toggle3)
toggle3 = ''.join(str(x) for x in temp_toggle3)
print("Schimba fiecare al treilea bit: ",toggle3)

ult7 = toggle3[-7:]

fara7 = toggle3[:-7]
# print(ult7)
# print(fara7)
schimba7 = ult7+fara7
# def form_crip_str(f1): 
#     for i in f1:  
#         print(i)
print("Deplaseaza la dreapta ultimii 7 biti: ",schimba7)

# 4. împarte șirul obținut în patru părți egale și permută între ele părțile 1 cu 3 și 2 cu 4;
def patru_parti(binary_string):
    # Calculate the length of each part
    part_length = len(binary_string) // 4
    
    # Use slicing to split the string into four equal parts
    parts = [binary_string[i:i+part_length] for i in range(0, len(binary_string), part_length)]
    
    return parts

string_separat = patru_parti(schimba7)

# print('split binary')
# print(string_separat)

def schimba_pozitii(parts):
    # Ensure there are at least four parts
    if len(parts) >= 4:
        parts[0], parts[2] = parts[2], parts[0]  # Swap first and third parts
        parts[1], parts[3] = parts[3], parts[1]  # Swap second and fourth parts
    return parts

schimba = schimba_pozitii(string_separat)
# print('swap_positions')
# print(schimba)
schimba = ''.join(str(x) for x in schimba)

# print('aici string schimbat')
print("Permuta partile: ",schimba)



# 5. utilizează o cheie de criptare/decriptare cu lungimea de 32 de biți care se combină cu șirul
# obținut anterior prin operația logică XOR (suma modulo 2).
def redimensioneaza_cheie(str1, str2):
    # Calculate the number of repetitions needed for str2
    repetitions = len(str1) // len(str2) + 1
    
    # Repeat str2 and concatenate to itself
    padded_str2 = (str2 * repetitions)[:len(str1)]
    
    return padded_str2

test = '01010101010'
cheie = input('introduceti cheie: ')
cheie_hex  = transforma_in_hex(cheie)
cheie_bin = transforma_in_binar(cheie_hex)
cheie_concat =  ''.join(str(x) for x in cheie_bin)

redimensionat = redimensioneaza_cheie(schimba,cheie_concat)

# y=int(s3,2) ^ int(re,2)
# y1 = '{0:b}'.format(y)

def xor_opr(binary_string, key):
    result = ''
    for i in range(len(binary_string)):
        # XOR operation between corresponding bits of binary string and key
        result += str(int(binary_string[i]) ^ int(key[i % len(key)]))
    return result
y01 = xor_opr(schimba,redimensionat)
# print('aici string cu xor')
print("Operatie de XOR",y01)
# print(re)
# print(y1)
def desparte_in_biti(string):
    return [string[i:i+8] for i in range(0, len(string), 8)]

crypt_string = desparte_in_biti(y01)
# print(crypt_string)
# print("aici incepe cript")
# f2 = form_crip_str(f1)
def biti_in_hex(binary_list):
    hex_list = []
    for binary_string in binary_list:
        decimal_value = int(binary_string, 2)
        hex_string = hex(decimal_value)[2:]  # [2:] to remove the '0x' prefix
        hex_list.append(hex_string)
    return hex_list

test1 =biti_in_hex(crypt_string)
print('Transforma binar in hex: ',test1)
# print(test1)

def hex_list_to_characters(hex_list):
    char_list = []
    for hex_string in hex_list:
        decimal_value = int(hex_string, 16)
        character = chr(decimal_value)
        char_list.append(character)
    return char_list

def schimba_in_ascii(hex_list):

    ascii_string = ''.join([chr(int(hex_value, 16)) for hex_value in hex_list])
    return ascii_string

test3 = schimba_in_ascii(test1)
print('Transforma hex in asci: ',test3)
print(test3)

#decriptare
input = input("Decriptati?")
def ascii_in_hex(string):
    hex_list = [hex(ord(char))[2:] for char in string]
    return hex_list

test_ascii = ascii_in_hex(test3)
# print('aici operatie inversa, ascii to hex')
# print(test_ascii)

ascii_in_binar=transforma_in_binar(test_ascii)
# print(ascii_in_binar)
concatdecript = ''.join(str(x) for x in ascii_in_binar)
print("Sir binar criptat: ",concatdecript)

revers_xor =xor_opr(concatdecript,redimensionat)
print("Operatie inversa de XOR",revers_xor)

separa_parti2=patru_parti(revers_xor)
# print(separa_parti2)
schimba_parti = schimba_pozitii(separa_parti2)
# print(schimba_parti)
schimba2 = ''.join(str(x) for x in schimba_parti)
print("Interschimba pozitiile: ",schimba2)

primele7 = schimba2[:7]
ultm7 = schimba2[7:]
# print(primele7)
# print(ultm7)

concat2 = ultm7+primele7
print("Muta inapoi 7 pozitii: ",concat2)

temp_revers_bit3=schimba_bit3(concat2)
revers_bit3 = ''.join(str(x) for x in temp_revers_bit3)
print("Schimba fiecare al treilea bit: ",revers_bit3)

primele5 = revers_bit3[:5]
ultm5 = revers_bit3[5:]
concat3 = ultm5+primele5
print("Deplaseaza 5 pozitii: ",concat3)

desparte =desparte_in_biti(concat3)
# print(desparte)

hexdecript =biti_in_hex(desparte)
# print(hexdecript)

decript = schimba_in_ascii(hexdecript)

print("Sir original: ",decript)
