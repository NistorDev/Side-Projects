import mysql.connector 
from prettytable import PrettyTable
import getpass




# Establish a connection to the MySQL server


def tabel():
    while True:
        host = 'localhost'
        user = input('introduceti nume utilizator: ')
        password = getpass.getpass('introduceti parola: ')
        database = 'control'
        table = 'salariati'

       

        # Create a cursor object to execute SQL queries
        # cursor = connection.cursor()
        if user == 'user1':

            conn= mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

            cursor = conn.cursor()


            query = 'SELECT marca, nume_salariat,salariu_net FROM {}'.format(table)

            cursor.execute(query)
            column_names = [i[0] for i in cursor.description]
            print(column_names)
            # Fetch the results
            results = cursor.fetchall()

            # Display the results
            for row in results:
                print(row)

            # Close the cursor and connection
            cursor.close()
            conn.close()

            if results:
                table = PrettyTable(column_names)
                for row in results:
                    table.add_row(row)
                print(table)
            else:
                print("No results found.")

      

        elif user == 'user2':
                
            conn= mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

            cursor = conn.cursor()

            query = 'SELECT marca, nume_salariat,salariu_de_incadrare,sporuri,retineri FROM {}'.format(table)
        
            cursor.execute(query)
            column_names = [i[0] for i in cursor.description]
            print(column_names)
            # Fetch the results
            results = cursor.fetchall()

            # Display the results
            for row in results:
                print(row)

            # Close the cursor and connection
            # cursor.close()
            # conn.close()

            if results:
                table = PrettyTable(column_names)
                for row in results:
                    table.add_row(row)
                print(table)
            else:
                print("No results found.")

            modificare = input('doriti sa modificati o inregistrare? (da/nu)' )
            if modificare.lower()  == 'da':

                def upd_table(salariu_de_incadrare, sporuri,retineri,marca):
                    upd_qrry = f'update salariati set '
                    if salariu_de_incadrare:
                        upd_qrry += f'salariu_de_incadrare = {salariu_de_incadrare} , '
                    if sporuri: 
                        upd_qrry += f'sporuri = {sporuri} , '
                    if retineri:
                        upd_qrry += f'retineri = {retineri} , '
                    upd_qrry = upd_qrry[:-2]
                    upd_qrry += f'where marca = {marca} '

                    # cursor = conn.cursor
                    cursor.execute(upd_qrry)
                    conn.commit()


                marca = int(input('Alegeti marca: '))

                salariu_de_incadrare = input('Introduceti noul salariu: ')
                sporuri = input('Scrieti valoarea sporurilor: ')
                retineri = input('Scrieti valoarea retinerilor: ')
                # res = upd_table(salariu_de_incadrare, sporuri, retineri, marca)



                mod_qrry = f'select salariu_de_incadrare,sporuri,retineri from salariati where marca = {marca} ' 
                
                cursor.execute(mod_qrry)
                rows = cursor.fetchall()
                # print(rows)
                for row in rows:
                    # print(row)
                    salariu_de_incadraredb = row[0]
                    sporuridb = row[1]
                    retineridb = row[2]
                    if retineri:
                        if int(retineri) > salariu_de_incadraredb+sporuridb:
                            print('retinerile nu pot fi mai mari decat salariul net + sporuri!')
                        else:
                            upd_table(salariu_de_incadrare,sporuri,retineri,int(marca))
                            # print('aici')
                    else:
                        upd_table(salariu_de_incadrare,sporuri,retineri,int(marca))
                        # print('aici')

                #     # print(salariu_de_incadrare)

                #     salariu_de_incadrare = input('Scrieti noul salariu: ')
                #     if len(salariu_de_incadrare) == 0:
                #         salariu_de_incadrare 
                #     sporuri = input('Scrieti valoarea sporurilor: ')
                #     retineri = input('Scrieti valoarea retinerilor: ')
                    
                #     upd_qrry = f'update salariati set salariu_de_incadrare = {salariu_de_incadrare}, sporuri = {sporuri}, retineri = {retineri} where marca = {marca}'
                #     cursor.execute(upd_qrry)

        elif user == 'user3':
                
            conn= mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

            cursor = conn.cursor()

            query = 'SELECT marca, nume_salariat,salariu_de_incadrare,sporuri,retineri,salariu_net FROM {}'.format(table)

            cursor.execute(query)
            column_names = [i[0] for i in cursor.description]
            print(column_names)
            # Fetch the results
            results = cursor.fetchall()

            # Display the results
            for row in results:
                print(row)

            # Close the cursor and connection
            # cursor.close()
            # conn.close()

            if results:
                table = PrettyTable(column_names)
                for row in results:
                    table.add_row(row)
                print(table)
            else:
                print("No results found.")

            modificare = input('doriti sa adaugati o inregistrare? (da/nu)' )
            if modificare.lower()  == 'da':
                def ins_table(nume_salariat,salariu_de_incadrare, sporuri,retineri):
                        ins_qrry = f'insert into salariati ( '
                        if nume_salariat:
                            ins_qrry += 'nume_salariat , '
                        if salariu_de_incadrare:
                            ins_qrry += f'salariu_de_incadrare , '
                        if sporuri: 
                            ins_qrry += f'sporuri , '
                        if retineri:
                            ins_qrry += f'retineri , '
                        ins_qrry = ins_qrry[:-2]
                        ins_qrry += f') values ( '

                        if nume_salariat:
                            ins_qrry += f'"{nume_salariat}" , '
                        if salariu_de_incadrare:
                            ins_qrry += f'{salariu_de_incadrare} , '
                        if sporuri:
                            ins_qrry += f'{sporuri} , '
                        if retineri:
                            ins_qrry += f'{retineri} , '
                        ins_qrry = ins_qrry[:-2]
                        ins_qrry += f')'

                        cursor.execute(ins_qrry)
                        conn.commit()

                nume_salariat = input('Introduceti numele salariatului: ')
                salariu_de_incadrare = input('Introduceti salariul: ')
                sporuri = input('Scrieti valoarea sporurilor: ')
                retineri = input('Scrieti valoarea retinerilor: ')

                if salariu_de_incadrare:
                    if len(salariu_de_incadrare) == 0:
                        print('salariul de incadrare nu poate fi 0!')
                    else:
                        # print(len(salariu_de_incadrare))
                        ins_table(nume_salariat,salariu_de_incadrare,sporuri,retineri)

        else: 
            print('utilizator necunoscut')
        # Execute the query
        user_input = input("Doresti sa continui? (da/nu): ")
        if user_input.lower() != 'da':
            break

res = tabel()