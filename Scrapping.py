import requests
import pandas as pd
from bs4 import BeautifulSoup

url_ss = 'https://studentsite.gunadarma.ac.id/'
laman_ss = requests.get(url_ss)
halaman = requests.get(url_ss)
hasil = BeautifulSoup (halaman.content, 'html.parser')


from bs4 import BeautifulSoup  
soup = BeautifulSoup(laman_ss.content, 'html.parser')



kontainer_berita = soup.find_all('div', class_='content-box')


judul_list = []
ringkasan_list = []

for berita in kontainer_berita:
    for judul in berita.find_all('h3'):
        judul_string = judul.get_text()
   
        judul_rapi = ' '.join(str(judul_string).strip().split()) 
        print(judul_rapi)
        # append judul ke list
        judul_list.append(judul_rapi)

    for rangkuman in berita.find_all('div', class_='content-box-wrapper'):
        rangkuman_rapi = ' '.join(str(rangkuman.get_text()).strip().split())
        print(rangkuman_rapi)

        ringkasan_list.append(rangkuman_rapi)

with open('berita.txt', mode='w') as berita_file:
    for judul, rangkuman in zip(judul_list, ringkasan_list):
        berita_file.write(judul)
        berita_file.write('\n')
        berita_file.write(rangkuman)
        berita_file.write('\n\n')

data = {'Judul': judul_list, 'Ringkasan': ringkasan_list}

# Membuat data frame
df = pd.DataFrame(data)

# Menampilkan data frame
print(df)