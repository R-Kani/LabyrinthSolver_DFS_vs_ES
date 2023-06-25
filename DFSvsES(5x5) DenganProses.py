from exSearch import ES
from DFS import DFS
from pyamaze import maze,agent,COLOR,textLabel, textLabelJudul1, textLabelJudul2, textLabelJudul3
from timeit import timeit

panjang = 5
lebar = 5
m=maze(panjang,lebar)

#Membuat labirin
m.CreateMaze(1,1,loopPercent=75) #(1,1) = goal dan loopPercent = tingkat kesulitan 

pencarianES,jalurES,jalur2_ES=ES(m)
pencarianDFS,jalurDFS,jalur2_DFS=DFS(m)

#Menampilkan jalur keluar yang didapatkan algoritma

#Exhaustive Search
pES=agent(m,footprints=True,color=COLOR.yellow,shape='square',filled=True)
a=agent(m,footprints=True,color=COLOR.red, filled=True)
m.tracePath({pES:pencarianES},delay=50)
m.tracePath({a:jalur2_ES},delay=300)

#DFS
pDFS=agent(m,footprints=True,shape='square',color=COLOR.cyan)
b=agent(m,footprints=True,filled=True,color=COLOR.blue)
m.tracePath({pDFS:pencarianDFS},showMarked=True,delay=450)
m.tracePath({b:jalur2_DFS},delay=300)

textLabelJudul3(m,f'LABIRIN UKURAN  {panjang} X {lebar} \t') ##Label header judul ukuran labirin

#Variabel perhitungan waktu eksekusi
t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
t2=timeit(stmt='ES(m)',number=1000,globals=globals())

#Menampilkan hasil eksuksi algoritma Exhaustive Search
textLabelJudul1(m, '\n  Exhaustive Search\t\n') #Label header judul Exhaustive Search
textLabel(m,'Waktu Eksekusi Exhaustive Search \t',t2) #Label untuk header perhitungan waktu Exhaustive Search
textLabel(m,'Jumlah Sel Yang Dikunjungi Exhaustive Search \t',len(pencarianES)+1) #Label untuk header perhitungan jumlah sel yang dikunjungi dalam pencarian solusi Exhaustive Search
textLabel(m,'Panjang Jalur Keluar Exhaustive Search \t\t',len(jalur2_ES)+1) #Label untuk header perhitungan panjang jalur untuk keluar labirin Exhaustive Search

#Menampilkan hasil eksuksi algoritma DFS
textLabelJudul2(m, '\n             DFS   \t\n') #Label header judul DFS
textLabel(m,'Waktu Eksekusi DFS \t\t',t1) #Label untuk header perhitungan waktu DFS
textLabel(m,'Jumlah Sel Yang Dikunjungi DFS \t\t',len(pencarianDFS)+1) #Label untuk header perhitungan jumlah sel yang dikunjungi dalam pencarian solusi DFS
textLabel(m,'Panjang Jalur Keluar DFS \t\t\t',len(jalur2_DFS)+1) #Label untuk header perhitungan panjang jalur untuk keluar labirin DFS

#Menjalankan program
m.run()
