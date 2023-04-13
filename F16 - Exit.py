import os
import sys

def exit_program():
    while True:
        save_input = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if save_input.lower() == 'y':
            os.system('save')
            sys.exit()
        elif save_input.lower() == 'n':
            sys.exit()
        else:
            print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")