import pandas as pd

data = [10, 9, 7, 8, 10]
siswa = ["Andi", "Budi", "Cindy", "Dedi", "Edi"]

nilai = pd.DataFrame({
    "Nama": siswa,
    "Nilai": data
})
print(nilai)


data = [10, 9, 7, 8, 10, 8]

print(data[1])

data[2] = 10

print(data)

data.append(9)

print(data)
