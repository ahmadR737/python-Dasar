from my_package import geometri, operasi

print(operasi.kurang(10, 4))
print(geometri.luas_persegi(5))

from my_package.operasi import kurang
from my_package.geometri import luas_persegi

print(kurang(20, 7))          # Output: 13
print(luas_persegi(8))        # Output: 64
