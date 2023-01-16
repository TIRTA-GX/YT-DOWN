# module
import os,sys,time
os.system("clear")
print("")
print("\33[0;31m")
os.system("figlet YT DOWN")
print("-------------------")
print("Author Tirta-GX   -\33[0;37m")
print("-------------------\33[0;37m")
import pytube

tanyakan = input("masukan url video anda ==>")

x = pytube.YouTube(tanyakan)

path = "/sdcard"

y = x.streams.get_highest_resolution().download(path)

print(y)
