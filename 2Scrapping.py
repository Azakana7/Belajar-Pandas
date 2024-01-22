import requests
import pandas as pd 
from bs4 import BeautifulSoup

th = "http://www.jobs.id/lowongan-kerja?kata-kunci=part time"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
lowkers = hasil.find_all(class_="single-jobs-ads")

posisi = []
instansi = []
gaji = []
for p in lowkers:
    t1 = p.select("h3")
    posisi.append(t1[0].get_text())

    t1 = p.select("a")
    try:
        instansi.append(t1[0].get_text())
    except IndexError:
        instansi.append("-")

    t2 = p.select("span")
    try: 
        gaji.append(t2[1].get_text())
    except IndexError:
        gaji.append(t2[0].get_text())

# Cetak
print(posisi)
print(instansi)
print(gaji)
