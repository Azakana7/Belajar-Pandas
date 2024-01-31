import pandas as pd

data = [10, 9, 7, 8, 10]
siswa = ["Andi", "Budi", "Cindy", "Dedi", "Edi"]

nilai = pd.DataFrame({
    "Nama": siswa,
    "Nilai": data
})
print(nilai)

#Beda

data = [10, 9, 7, 8, 10, 8]

print(data[1])

data[2] = 10

print(data)

data.append(9)

print(data)

#Beda

data = [10, 9, 7, 8, 10, 8] indeks O 
    for elemen in data: 
        print("Elemen ke ", indeks, " = ", elemen) indeks = indeks + 1


#Batas

print("4" + "5")


nilai1 = 8
nilai2 = 8
jumlah = nilai1 + nilai2
print(jumlah)


data = [7, 9, 4, 10, 8, 2]
print(data[1])
data[3] = 7
print(data)
data.append(4)
print(data)


data = [7, 9, 4, 10, 8, 2]
indeks = 0
for elemen in data:
  print("Elemen ke ", indeks, "=", elemen)
  indeks = indeks + 1



data = [12, 6, "Kurniawaty", "5", 7]
for x in data:
  print(x/2)



data = [8, 14, "Alisa", 6, 4]
for x in data:
  try:
    print(x/2)
  except:
    print("Bukan bilangan")


nil = 4
if (nil > 0):
  print("Bilangan positif")
else:
  print("Bilangan negatif")


import pandas as pd

data = [10, 9, 7, 8, 10]
siswa = ["Andi", "Budi", "Cindy", "Dedi", "Edi"]

nilai = pd.DataFrame({
    "Nama": siswa,
    "Nilai": data
})
print(nilai)
