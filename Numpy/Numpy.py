import numpy as np

# Dizi Oluşturma
array = np.array([1,2,3,4,5,6,7,8,9,10]) #tek boyutlu bir dizi ya da 
                                         #vektör oluşturma

#Output -> [ 1  2  3  4  5  6  7  8  9 10]

#[--------------------------------]

#Matris Oluşturma
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) #2x5'lik bir matris 
                                              #oluşturma

#Output -> [[ 1  2  3  4  5]
#           [ 6  7  8  9 10]]

#[--------------------------------]

#Boş Bir Matris Oluşturma
arrayZeros = np.zeros((5,5)) #5x5' lik boş bir dizi oluşturma

#Output -> [[0. 0. 0. 0. 0.]
#           [0. 0. 0. 0. 0.]
#           [0. 0. 0. 0. 0.]
#           [0. 0. 0. 0. 0.]
#           [0. 0. 0. 0. 0.]]

#[--------------------------------]

#Bir'lerden Oluşan Bir Matris Oluşturma
arrayOnes = np.ones((5,5)) #5x5' lik 1 lerden oluşan bir matris 
                          #oluşturma

#Output -> [[1. 1. 1. 1. 1.]
#           [1. 1. 1. 1. 1.]
#           [1. 1. 1. 1. 1.]
#           [1. 1. 1. 1. 1.]
#           [1. 1. 1. 1. 1.]]

#[--------------------------------]

#Rastgele Değerlerden Oluşan Bir Matris Oluşturma
rastgele = np.random.random((2,2)) #2x2'lik rastgele sayılar üretir

#Output-> array([[0.69545006, 0.26729605], [0.38600722, 0.63090146]])

#[--------------------------------]

#Belirli Aralıklarla Artan Matris Oluşturma
#Bir sayıdan diğer bir sayıya kadar belirli aralıklarla arttırma

dizi1 = np.arange(1,10,2)
#Output -> array([1, 3, 5, 7, 9])

dizi2 = np.arange(1,30,3)
#Output -> array([ 1,  4,  7, 10, 13, 16, 19, 22, 25, 28])

#[--------------------------------]

#Matrsi veya Dizinin Boyutunu Bulma
print(arrayOnes.shape) #size' ını bulup ekrana basma

#Output -> (5, 5)

#[--------------------------------]

#Yeniden Boyutlandırma
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1.reshape(5,2)) #reshape ile yeniden boyutlandırabiliriz, #fakat yeni oluşacak #matris eleman sayısı ile içine verilecek eleman #sayısı aynı olmak zorunda.

#Output ->[[ 1  2]
#          [ 3  4]
#          [ 5  6]
#          [ 7  8]
#          [ 9 10]]

#[--------------------------------]

#Genel Fonksiyonlar
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print('boyut: ', array1.ndim) #matris boyutunu ekrana basma
#Output -> boyut:  2


print("veri tipi: ",array1.dtype.name) #matris veri tipini ekrana basma
#Output -> veri tipi:  int32

print("boyut: ",array1.size) #matris boyutunu ekrana basma
#Output -> boyut:  10

print("tip: ",type(array1)) #matris tipini ekrana basma
#Output -> tip:  <class 'numpy.ndarray'> 

#[--------------------------------]

#Değer Atama
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

array1[0,0] = 11 #matrisin verilen indisine yeni değer atama
#Output -> [[11  2  3  4  5]
#           [ 6  7  8  9 10]]

#[--------------------------------]

#Matematiksel İşlemler
dizi11 = np.array([[5,3,7],[1,0,6]])
dizi22 = np.array([[1,2,9],[2,4,8]])

#1.1.) Matrislerde Toplama İşlemi 1
print(dizi11+dizi22)        
#Output-> [[ 6  5 16]
#          [ 3  4 14]]

#1.2.) Matrislerde Toplama İşlemi 2
print(np.add(dizi11,dizi22))
#Output-> [[ 6  5 16]
#          [ 3  4 14]]

#1.3.) Matrislerde Toplama İşlemi
#Eğer her elemanını belirli bir değerle toplicaksak (bu çıkarma, çarpma, bölme de olabilir) aşşağıdaki şekilde tanımlanır
print(dizi11+5)   
#Output -> [[10  8 12]
#           [ 6  5 11]]

#2.) Matrislerde Çıkarma İşlemi
print(dizi11-dizi22)
#Output -> [[ 4  1 -2]
#           [-1 -4 -2]]

#3.) Matrislerde Çarpma İşlemi
print(dizi11*dizi22)
#Output -> [[ 5  6 63]
#           [ 2  0 48]]

#4.1.) Karesini Alma 1
print(dizi22**2)  
#Output ->[[ 1  4 81]
#         [ 4 16 64]]

#4.2.) Karesini Alma 2
print(np.square(dizi22)) 
#Output -> [[ 1  4 81]
#           [ 4 16 64]]

#5.) Karekök Alma
print(np.sqrt(dizi22))
#Output -> [[1.         1.41421356 3.        ]
#          [1.41421356 2.         2.82842712]]

#6.) Trigonometrik İfadeler
#6.1) Sinüsünü Alma
print(np.sin(dizi22))
#Output -> [[ 0.84147098  0.90929743  0.41211849]
#           [ 0.90929743 -0.7568025   0.98935825]]

#6.2.) Kosinüsünü Alma
print(np.cos(dizi22))
#Output -> [[ 0.54030231 -0.41614684 -0.91113026]
#           [-0.41614684 -0.65364362 -0.14550003]]

#6.3.) Tanjantını Alma
print(np.tan(dizi22))
#Output -> [[ 1.55740772 -2.18503986 -0.45231566]
#           [-2.18503986  1.15782128 -6.79971146]]

#6.4) arcsin, arccos, arctan
#Aynı şekilde arcsin, arccos, arctan işlemlerini de gerçekleştirebiliriz.

#7.) e Üzeri Alma
print(np.exp(dizi11)) 
#Output -> [[1.48413159e+02 2.00855369e+01 1.09663316e+03]
#           [2.71828183e+00 1.00000000e+00 4.03428793e+02]]

#8.) Log Alma
print(np.log(dizi11))
#Output -> [[1.60943791 1.09861229 1.94591015]
#           [0.               -inf 1.79175947]]

#9.) Matris veya Dizideki Elemanları Toplama
print(dizi11.sum())
#Output -> 22

#10.) Matris veya Dizideki Maksimum Elemanı Bulma
print(dizi11.max())
#Output -> 7

# 11.) Matris veya Dizideki Minimum Elemanı Bulma 
print(dizi11.min())
#Output -> 0

#12.) Numpy dot İşlemi
a = np.array([[1,2],[3,4]]) 
b = np.array([[10,11],[12,13]]) 
np.dot(a,b)

#yapılan işlem
#[[1*10+2*12, 1*11+2*13],[3*10+4*12, 3*11+4*13]]

#output -> array([[34, 37], [78, 85]])

#13.) Axis İşlemi 
print(dizi11.sum(axis=0)) #satırları toplar ve ekrana yazdırır
#output -> [2 2 2]

#14.) Mod Alma
print(dizi11 % 2)
#Output -> [[1 1 1]
#          [1 0 0]]

#[--------------------------------]

#Matris ve Dizilerde Koşul İşlemleri
array = np.array([0,1,2,3,4,5,6,7,8,9,10])

#her bir elemanı 5 ten küçük mü karşılaştıralım
new_array = array < 5
print(new_array)
#Output -> [ True  True  True  True  True False False False False False False]

#5 ten küçük elemanları ekrana basalım
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array[array<5])
#Output -> [0 1 2 3 4]

#[--------------------------------]

#İstatistiki Bilgiler (Ortalama(Mean), Ortanca Değer(Median), Varyans ve Standart Sapma)

array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#1.) Ortalama (Mean)
print(array.mean())
#Output -> 5.0

#2.) Ortanca Değer (Median)
print(np.median(array))
#Output -> 5.0

#3.) Varyans
print(array.var())
#Output -> 10.0

#4.) Standart Sapma
print(array.std())
#Output -> 3.1622776601683795

#[--------------------------------]

#İndis ve Listeleme İşlemleri

array12 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array12[0,0]) #array12' nin [0,0]'ıncı indisteki elemanını ekrana basar 
#Output -> 1

print(array12[0,:]) # 0'ıncı satırı ekrana basar
#Output -> [1 2 3 4 5]

print(array12[-1,:]) # son satırı ekrana basar
#Output -> [ 6  7  8  9 10]

print(array12[:,1]) # 1'inci sutunu ekrana basar
#Output -> [2 7]

print(array12[0,1:4]) #array12' nin 0'ıncı satırdaki 1'den 4'e kadar 
                      #olan rakamları ekrana basar [2, 3, 4]
#Output -> [2 3 4]

terstenArray12 = array12[::-1] #array12' yi ters çeviriyor
print(terstenArray12)
#Output -> [[ 6  7  8  9 10]
#           [ 1  2  3  4  5]]
			
#[--------------------------------]

#Matris Boyut işlemleri

array123 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

vektorHali = array123.ravel() # matrisi vektörleştirme
print(vektorHali)
#Output -> [ 1  2  3  4  5  6  7  8  9 10]

matrisHali = vektorHali.reshape(2,5) # vektörü matrisleştirme
print(matrisHali)
#Output -> [[ 1  2  3  4  5]
            [ 6  7  8  9 10]]

transpozluHali = matrisHali.T # matris Transpoz alma
print(transpozluHali)
#Output -> [[ 1  6]
#           [ 2  7]
#           [ 3  8]
#           [ 4  9]
#           [ 5 10]]

#[--------------------------------]

#Komutlar

#1.) Column Stack (Sütunları bir hale getiriyor)
a = np.array((1,2,3))
b = np.array((7,8,9))
np.column_stack((a,b))
#output -> array([[1, 7], [2, 8], [3, 9]]) 

#2.) Vstack (İki matrisi birleştirme)
a = np.array((1,2,3))
b = np.array((7,8,9))
np.vstack((a,b))
#output -> array([[1, 2, 3], [2, 3, 4]])

#3.) Hstack (Verilen iki diziyi tek bir dizi haline getirme)
a = np.array((1,2,3))
b = np.array((2,3,4))
np.hstack((a,b))
#output -> array([1, 2, 3, 2, 3, 4])

#4.) Copy (bir diziyi veya matrisi kopyalama)
kopya = a.copy()

#[--------------------------------]

#Liste ve Dizi Dönüşümleri
liste = [1,2,3,4,5]

dizi= np.array(liste) # listeyi diziye dönüştürme
print(dizi)
#Output -> [1 2 3 4 5]

liste2 = list(dizi)   # diziyi listeye dönüştürme
print(liste2)
#Output -> [1, 2, 3, 4, 5]
