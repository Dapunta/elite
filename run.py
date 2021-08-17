import sys, os, subprocess
import elite
import bot_follow

if sys.version[0:3] != "3.9":
  sys.exit("[!] Anda harus menggunakan versi python 3.9, versi python anda sekarang : "+sys.version[0:3])

if __name__ == "__main__":
  try:
      os.system("git pull")
      __import__("elite").folder()
  except Exception:
    os.system("clear")
    print("\n Hello! Pengguna Script Elite")
    print("\n Script Ini Dalam Masa Pengembangan Dan Dihapus Untuk Sementara Waktu")
    print("\n Harap Bersabar")
