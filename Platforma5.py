import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import schedule
import time
import threading

msg_succes = False

def aleg_folder_sursa():
    folder_sursa = filedialog.askdirectory()
    if folder_sursa:
        c_folder_sursa.delete(0, tk.END)
        c_folder_sursa.insert(tk.END, folder_sursa)

def aleg_folder_destinatie():
    folder_destinatie = filedialog.askdirectory()
    if folder_destinatie:
        c_folder_destinatie.delete(0, tk.END)
        c_folder_destinatie.insert(tk.END, folder_destinatie)

def fac_backup():
    global msg_succes
    folder_sursa = c_folder_sursa.get()
    folder_destinatie = c_folder_destinatie.get()

    if not folder_sursa or not folder_destinatie:
        messagebox.showerror("Atenție!", "Selectați folderele sursă și destinație!")
        return

    fisiere = os.listdir(folder_sursa)

    dim_totala_fis = sum(os.path.getsize(os.path.join(folder_sursa, file)) for file in fisiere)

    capacitate_stick = 1024 * 1024 * 1024  # 1 GB

    if dim_totala_fis <= capacitate_stick:
        # copiere toate fișierele în folderul destinație
        for file in fisiere:
            sursa = os.path.join(folder_sursa, file)
            destinatie = os.path.join(folder_destinatie, file)
            shutil.copy(sursa, destinatie)
            if not msg_succes:
                messagebox.showinfo("Succes!", "Operația de backup a fost realizată cu succes!")
                msg_succes = True
    else:
        messagebox.showwarning("Atenție!", "Dimensiunea totală a fișierelor este mai mare decât capacitatea stick-ului de memorie. "
                                              "Se vor copia doar fișierele ce au dimensiunea cea mai apropiată de capacitatea stick-ului.")

        # sortare fisiere după dimensiune
        sort_fis_dim = sorted(fisiere, key=lambda file: os.path.getsize(os.path.join(folder_sursa, file)), reverse=True)
        dim_curenta = 0
        for file in sort_fis_dim:
            sursa = os.path.join(folder_sursa, file)
            destinatie = os.path.join(folder_destinatie, file)
            if dim_curenta + os.path.getsize(sursa) <= capacitate_stick:
                shutil.copy(sursa, destinatie)
                dim_curenta += os.path.getsize(sursa)
            else:
                messagebox.showwarning("Avertisment", f"Fișierul {file} nu a putut fi copiat pe stick-ul de memorie, deoarece nu mai este suficient spațiu disponibil.")

def programez_backup():
    ora_backup = camp_bkp.get()
    if not ora_backup:
        messagebox.showerror("Eroare", "Introduceți ora la care să se realizeze backup-ul!")
        return

    schedule.every().day.at(ora_backup).do(fac_backup)
    messagebox.showinfo("Programare Backup", f"Backup-ul va fi realizat zilnic la ora {ora_backup}.")

def start_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# interfața grafică
root = tk.Tk()
root.title("Backup Automat")
root.geometry("450x300")

# selectare folder sursă
label_folder_sursa = tk.Label(root, text="Folder sursă:")
label_folder_sursa.grid(row=0, column=0, padx=5, pady=5)
c_folder_sursa = tk.Entry(root, width=30)
c_folder_sursa.grid(row=0, column=1, padx=5, pady=5)
buton_folder_sursa = tk.Button(root, text="Alege Folder", command=aleg_folder_sursa)
buton_folder_sursa.grid(row=0, column=2, padx=5, pady=5)

# selectare folder destinație
label_folder_destinatie = tk.Label(root, text="Folder destinație:")
label_folder_destinatie.grid(row=1, column=0, padx=5, pady=5)
c_folder_destinatie = tk.Entry(root, width=30)
c_folder_destinatie.grid(row=1, column=1, padx=5, pady=5)
buton_folder_destinatie = tk.Button(root, text="Alege Folder", command=aleg_folder_destinatie)
buton_folder_destinatie.grid(row=1, column=2, padx=5, pady=5)

label_bkp = tk.Label(root, text="Ora backup-ului (HH:MM):")
label_bkp.grid(row=2, column=0, padx=5, pady=5)
camp_bkp = tk.Entry(root, width=15)
camp_bkp.grid(row=2, column=1, padx=5, pady=5)

btn_bkp = tk.Button(root, text="Programează Backup", command=programez_backup)
btn_bkp.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

threading.Thread(target=start_scheduler, daemon=True).start()

root.mainloop()