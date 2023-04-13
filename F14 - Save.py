import os
import sys
import math
import time
import argparse
import datetime


def create_dir_if_not_exists(path):
    # Membuat direktori jika belum ada
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


def rename_file_if_exists(path):
    # Mengubah nama file jika sudah ada
    filename, ext = os.path.splitext(path)
    i = 1
    while os.path.isfile(path):
        path = f"{filename}_{i}{ext}"
        i += 1
    return path

def check_dir_or_file_exists(path):
    # Mengecek apakah path sudah ada atau belum
    return os.path.exists(path)

def save():
    # Command ini digunakan untuk menjalankan prosedur menyimpan data yang berada di program sesuai dengan struktur data eksternal.
    folder = input("Masukkan nama folder: ")
    folder_path = os.path.join("save", folder)

    # Buat direktori jika belum ada
    if not check_dir_or_file_exists(folder_path):
        print(f"\nSaving...\n\nMembuat folder {folder_path}...\n")
        create_dir_if_not_exists(folder_path)
    else:
        print(f"\nSaving...\n\nFolder {folder_path} sudah ada\n")

    # Buat path untuk file dan tambahkan suffix jika sudah ada
    now = datetime.datetime.now()
    filename = f"data_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    file_path = os.path.join(folder_path, filename)
    file_path = rename_file_if_exists(file_path)

    # Simpan data ke file
    with open(file_path, "w") as f:
        f.write("Data yang akan disimpan\n")

    print(f"Berhasil menyimpan data di {file_path}!")
