import argparse
import os

def load(nama_folder):
    # validasi keberadaan folder
    if not os.path.isdir(nama_folder):
        print(f"Folder '{nama_folder}' tidak ditemukan.")
        return

    print("Loading...")
    # Menjalankan prosedur load data
    # ...
    print("Load data berhasil.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help="Nama folder yang berisi file penyimpanan.")
    args = parser.parse_args()

    if args.nama_folder:
        load(args.nama_folder)
    else:
        print("Tidak ada nama folder yang diberikan!\nUsage: python main.py <nama_folder>")