import pandas as pd

# Pandas Veri Tipleri
#1- Series
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
series = pd.Series(data=array)

print(series)
#Output -> 0    0
#          1    1
#          2    2
#          3    3
#          4    4
#          5    5
#          6    6
#          7    7
#          8    8
#          9    9
#         10   10
#dtype: int64

#2- DataFrame
dataframe1 = pd.DataFrame(data=array,index) 


seri1 = pd.Series([0, 1, 2, 3])
seri2 = pd.Series(['a', 'b', 'c', 'd'])

veri1 = dict(rakam=seri1, harf=seri2)
dataFrame1 = pd.DataFrame(veri1)

print(dataFrame1)
#Output -> 
#   rakam  harf
#0      0     a
#1      1     b
#2      2     c
#3      3     d

#DataFrame'i Kopyalama
dataFrame2 = pd.DataFrame(dataFrame1)


#Ornek olarak bir DataFrame oluşturma
dictionary = {"isim:"["Kaan", "Aslı", "Ege"],
              "yas:" [21, 20, 22]}

dataframe1 = pd.DataFrame(dictionary)


#[------------------------------------------]

#Örnek kodlar

#Giriş
uygulamalar = pd.read_csv('C:\\googleplaystore.csv', sep=',')
#csv dosyalarında veriler virgül ile ayrıldığı için sep=',' diyerek virgüllerden kurtardık 

#okuma işlemi tamamlandı şimdi ise tipini ekrana basalım.
print(type(uygulamalar))
#Output-> <class 'pandas.core.frame.DataFrame'>

#ilk kaydı ekrana basalım ve ilk verimizi bir görelim.
uygulamalar.head(1)
#Output -> 
#                                              App        Category  Rating Reviews Size  ... Content Rating        Genres     Last Updated Current Ver   Android Ver
#
#0  Photo Editor & Candy Camera & Grid & ScrapBook  ART_AND_DESIGN     4.1     159  19M  ...       Everyone  Art & Design  January 7, 2018       1.0.0  4.0.3 and up



#Kolon Başlıklarını Görmek için
print(uygulamalar.columns)
#Output -> 
#Index(['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
#       'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
#       'Android Ver'],
#      dtype='object')




#DataFrame hakkında genel bilgi öğrenmek için
print(uygulamalar.info())
#Output -> 
#<class 'pandas.core.frame.DataFrame'>    #veri tipi
#RangeIndex: 10841 entries, 0 to 10840    #kaç elemandan oluştuğu
#Data columns (total 13 columns):         #kaç kolon içerdiği
#App               10841 non-null object  #her bir kolonun kaç değer barındırdığı 
#                                         #(eksikler kayıp)
#Category          10841 non-null object
#Rating            9367 non-null float64  #en fazla kayıp görüldüğü gibi bu kolonda
#Reviews           10841 non-null object
#Size              10841 non-null object
#Installs          10841 non-null object
#Type              10840 non-null object
#Price             10841 non-null object
#Content Rating    10840 non-null object
#Genres            10841 non-null object
#Last Updated      10841 non-null object
#Current Ver       10833 non-null object
#Android Ver       10838 non-null object
#dtypes: float64(1), object(12)           #kaç adet veri tipinden oluştuğu
#memory usage: 592.9+ KB                  #hafızada ne kadar yer kapladığı
#None




#Kolonların Veri Tipleri
print(dataFrame1.dtypes)
#Output -> 
#App                object
#Category           object
#Rating            float64
#Reviews            object
#Size               object
#Installs           object
#Type               object
#Price              object
#Content Rating     object
#Genres             object
#Last Updated       object
#Current Ver        object
#Android Ver        object
#dtype: object



#Sadece Numeric Kolonları Listelemek İçin
print(uygulamalar.describe())
#Output -> 
#            Rating
#count  9367.000000 # toplamı
#mean      4.193338 # ortalaması
#std       0.537431 # standart sapması
#min       1.000000 # minimum değeri
#25%       4.000000 # sol parça ortanca değeri
#50%       4.300000 # ortanca değeri
#75%       4.500000 # sağ parça ortanca değeri
#max      19.000000 # maximum değeri



#[------------------------------------------]

#Listeleme İşlemleri
head = uygulamalar.head() #baştan 5 satırı bize verir
tail = uygulamalar.tail() #sondan 5 satırı bize verir

head2 = uygulamalar.head(10) # baştan 10 kaydı bize verir

#Sadece belirtilen kolonları listelemek için
print(uygulamalar["App"]) # Tüm uygulama isimlerini ekrana basar
print(uyglamalar.App)     # Tüm uygulama isimlerini ekrana basar

print(uygulamalar["App"].head(4)) #ilk 4 uygulamayı ekrana basar
#Output ->
# 0       Photo Editor & Candy Camera & Grid & ScrapBook
# 1                                  Coloring book moana
# 2    U Launcher Lite – FREE Live Cool Themes, Hide ...
# 3                                Sketch - Draw & Paint
# Name: App, dtype: object




#DataFrame loc -> Belirtilen satır ya da sütunları almak için kullanılır
print(uygulamalar.loc[:, "App"]) # App sütunundaki tüm satırları al ve ekrana bas


print(uygulamalar.loc[0:4], "App") # App sütunundaki ilk 3 kaydı al (3 dahil  
                                   #(0-1-2-3))


print(uygulamalar.loc[:4], "App") # App sütunundaki ilk 4 kaydı al (4 dahil  
                                   #(0-1-2-3-4))


print(uygulamalar.loc[:, ["App","Rating"]]) #App ve Rating'deki tüm verileri listeleme


print(uygulamalar.loc[::-1,:]) #tersten yazdırma


print(uygulamalar.loc[:, :["Rating"]]) #Rating' e kadar olan tüm satır ve sutunları 
                                       #listeleme (App, Category, Rating)


print(uygulamalar.loc[:, "Rating"]) # Rating' deki tüm satırları ekrana bas


print(uygulamalar.iloc[:,2]) # Rating' deki tüm satırları ekrana bas (index olarak)



#[------------------------------------------]


#Filtreleme
print(uygulamalar.Rating.head() > 4.1 ) #ilk 5 satırdaki rating' i 4.1 den büyük olanları 
                                        #True, küçük olanları False olarak listeledik


filtrelenmis_veri = uygulamalar[uygulamalar.Rating > 4.1]
print(filtrelenmis_veri)



#Çoklu Filtreleme
#Birden Fazla Filtreleme işlemi
filtre1 = uygulamalar.Rating > 3
filtre2 = uygulamalar.Rating < 4

print(uygulamalar[filtre1 & filtre2])


#Liste Kavamları
ortalama_rating = uygulamalar.Rating.mean()
print(ortalama_rating)
#Output -> 4.193338315362443



#[------------------------------------------]


#Yeni Kolon Ekleme
uygulamalar.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in uygulamalar.columns]


#Yeni Kolon Oluşturma
ortalama_rating = uygulamalar.Rating.mean()

uygulamalar["rating_seviyesi"] = ["dusuk" if ortalama_rating > each else "yuksek" for each in uygulamalar.Rating]


#Kolon Silme
uygulamalar.drop(["rating_seviyesi"],axis=1,inplace = True)


#Kolon Güncelleme
uygulamalar["rating_yuzluk"] = [ each*10 for each in uygulamalar.Rating]
#ya da 
def donustur(rating):
    return rating*10
    
dataFrame1["rating_yuzluk"] = uygulamalar.Rating.apply(donustur)



#[------------------------------------------]


#DataFrame’ leri Birleştirme

# > Dikey Olarak Birleştirme
veri1 = uygulamalar.head()
veri2 = uygulamalar.tail()

data1 = pd.concat([veri1,veri2], axis=0)

#> Yatay Olarak Birleştirme
veri1 = uygulamalar.App
veri2 = uygulamalar.Rating

data2 = pd.concat([veri1,veri2], axis=1)

