import pandas as pd

data = [10, 9, 7, 8, 10]
siswa = ["Andi", "Budi", "Cindy", "Dedi", "Edi"]

nilai = pd.DataFrame({
    "Nama": siswa,
    "Nilai": data
})
print(nilai)