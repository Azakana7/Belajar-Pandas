import requests
import pandas as pd
from bs4 import BeautifulSoup

th = "https://studentsite.gunadarma.ac.id/"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
lowkers = hasil.find_all(class_="content-box")

judul_list = []
ringkasan_list = []

for berita in lowkers:
    for judul in berita.find_all('h3'):
        judul_string = judul.get_text()
   
        judul_rapi = ' '.join(str(judul_string).strip().split()) 
        #print(judul_rapi)
        # append judul ke list
        judul_list.append(judul_rapi)

    for rangkuman in berita.find_all('div', class_='content-box-wrapper'):
        rangkuman_rapi = ' '.join(str(rangkuman.get_text()).strip().split())
        #print(rangkuman_rapi)

        ringkasan_list.append(rangkuman_rapi)

data = {'Judul': judul_list, 'Ringkasan': ringkasan_list}

# Membuat data frame
df = pd.DataFrame(data)

# Menampilkan data frame
print(df)

#Credit Divo Daniel Saputra