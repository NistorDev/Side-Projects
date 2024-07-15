# # 8. Să se scrie un program destinat schimbării parolei. Programul va trebui
#  să solicite utilizatorului 
# # parola sa curentă, să o valideze şi apoi să solicite noua parolă dorită. 
# Programul va trebui să verifice faptul 
# # că noua parolă este aleasă corespunzător, adică aceasta îndeplineşte 
# simultan următoarele criterii: 
# # a). parola nu poate fi numele de conectare (de logare) al utilizatorului, 
# sau acest nume inversat;  
# # b). parola nu poate fi numele real al utilizatorului;  
# # c). lungimea parolei trebuie să fie de cel puţin de 6 caractere şi să 
# cuprindă cel puţin două caractere ce 
# # nu sunt alfanumerice. 
# # Precizări: 
# # a. La introducerea parolei în câmpul aferent din cadrul interfeţei 
# aplicaţiei, parola nu va apărea în clar 
# # pe ecran. 
# # b. O condiţie suplimentară pentru parolă (opţională), este aceea că 
# aceasta nu trebuie să fie un 
# # cuvânt în limba engleză (este necesară utilizarea unui verificator 
# “spelling checker”).

import mysql.connector 
from getpass import getpass
import re

while True:
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = "Drrrk!@!1",
        database = 'parole',
        # table = 'parola_user'
    )
    def verify_user(username):
        # connection = connection()
        cursor = connection.cursor()

        query = "SELECT * FROM parola_user WHERE user_name = %s "
        cursor.execute(query, (username, ))

        user = cursor.fetchone()

        cursor.close()
        # connection.close()

        if user:
            return True
        else:
            return False
        
    def verify_password(username, password):
        # connection = connect_to_database()
        cursor = connection.cursor()

        query = "SELECT parola_veche FROM parola_user WHERE user_name = %s"
        cursor.execute(query, (username,))

        result = cursor.fetchone()

        cursor.close()
        # connection.close()

        if result and result[0] == password:
            return True
        else:
            return False
        
    def reverse_string(s):
        reversed_str = ""
        for char in s:
            reversed_str = char + reversed_str
        return reversed_str
        
    def validate_new_password(new_password, old_password,user_name):
        if new_password == old_password:
            print("Parola trebuie sa fie diferita de cea anterioara!")
            return False
        if len(new_password) < 6:
            print("Parola trebuie sa fie mai lunga de 6 caractere")
            return False
        if not re.search(r'[^a-zA-Z]', new_password):
            print("Parola trebuie sa contina caractere alfanumerice")
            return False
        if len(re.findall(r'[a-zA-Z0-9]', new_password)) < 2:
            print("Parola trebuie sa contina minim doua caractere alfanumerice!")
            return False
        if new_password == user_name:
            print("Parola nu poate fi numele de utilizator!")
            return False
        
        cursor = connection.cursor()
        query = "SELECT nume_real FROM parola_user WHERE user_name = %s "
        cursor.execute(query, (user_name, ))

        nume = cursor.fetchone()
        # print (nume)
        revers = ''.join(reversed(nume))
        rev1 = ''.join(reversed(nume))
        revers = reverse_string(revers)
        # print(revers)
        
        if new_password == rev1:
            print("Parola nu poate fi numele real al utilizatorului!")
            return False
        if new_password == revers:
            print("Parola nu poate fi numele real al utilizatorului inversat!")
            return False
        cursor.close()
        return True

    def update_password(username, new_password):
        # connection = connect_to_database()
        cursor = connection.cursor()
        
        query = "UPDATE parola_user SET parola_veche = %s WHERE user_name = %s"
        cursor.execute(query, (new_password, username))

        connection.commit()
        cursor.close()
        # connection.close()

    def main():
        
        user_name = input('nume utilizator: ')
        parola = input('parola veche: ')
        # if verify_password(user_name, parola):
        #     parola_noua = getpass("Enter your new password: ")

        if verify_user(user_name):
            
            if verify_password(user_name, parola):
                parola_noua = input('Introduceti noua parola: ')
                if validate_new_password(parola_noua, parola,user_name):
                    update_password(user_name, parola_noua)
                
                else:
                    print("Parola nu este valida!")
            else:
                print("Parola este invalida!")
        else:
            print("Numele de utilizator nu exista!")
    if __name__ == "__main__":
        main()
 