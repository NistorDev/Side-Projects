import os
import shutil
from pathlib import Path

def get(source_folder):
    return [f for f in source_folder.iterdir() if f.is_file()]

def calculate(files):
    return sum(f.stat().st_size for f in files)

def copy(files, destination_folder):
    for file in files:
        shutil.copy(file, destination_folder)

def main():
    source_folder = Path(input("Introduceti calea fisierului sursa: "))
    destination_folder = Path(input("Introduceti calea fisierului destinatie (USB stick): "))

    destination_folder.mkdir(parents=True, exist_ok=True)

    files = get(source_folder)
    
    if not files:
        print("Nu exista fisiere in sursa!")
        return

    total_size = calculate(files)
    print(f"Dimensiune totala: {total_size / (1024 * 1024):.2f} MB")

    copy(files, destination_folder)
    print("Fisierele au fost copiate.")

if __name__ == "__main__":
    main()
