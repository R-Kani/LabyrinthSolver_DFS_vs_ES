from pyamaze import maze,agent,COLOR,textLabelJudul1,textLabelJudul3
from collections import deque

def ES(m,start=None):
    if start is None: #jika startnya tidak ada maka definisikan start secara default 
        start=(m.rows,m.cols) #yaitu di sudut kanan bawah labirin
        
    selanjutnya = deque()
    selanjutnya.append(start)
    jalur = {} #dictionary untuk menyimpan jalur dari sel saat ini ke sel tetangganya
    explored = [start] #list untuk menyimpan sel-sel yang telah dikunjungi
    pencarian=[] #ist untuk menyimpan urutan sel-sel yang dikunjungi selama proses pencarian

    while len(selanjutnya)>0:#perulangan jika panjang array selanjutnya > 0 atau selama masih ada sel dalam frontier (selanjutnya) yang akan dieksplorasi
        currCell=selanjutnya.popleft() #mengambil sel pada selanjutnya dan disimpan dalam currCell
        if currCell==m._goal: #jika currCell yang ditempati == goal maka perulangan dihentikan karena tujuan telah tercapai
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True: #periksa apakah sel tersebut dapat diakses 
                if d=='E':
                    child=(currCell[0],currCell[1]+1)
                elif d=='W':
                    child=(currCell[0],currCell[1]-1)
                elif d=='S':
                    child=(currCell[0]+1,currCell[1])
                elif d=='N':
                    child=(currCell[0]-1,currCell[1])
                if child in explored: #pengecekan apakah tetangga tersebut sudah pernah dikunjungi sebelumnya
                    continue #jika sudah, maka proses dilanjutkan ke tetangga berikutnya
                selanjutnya.append(child) #jika tetangga belum pernah dikunjungi sebelumnya, maka tetangga tersebut ditambahkan ke antrian 'selanjutnya'
                explored.append(child) #masukkan ke dalam list explored
                jalur[child] = currCell #menyimpan informasi jalur dari currCell ke tetangga tersebut dalam dictionary
                pencarian.append(child) #menambahkan sel tetangga ke array pencarian untuk mencatat urutan kunjungan
    
    #proses untuk menampilkan jalan keluar
    print(f'{jalur}')
    jalur2={} #dictionary untuk mengunjungi jalur secara terbalik sehingga terbentuklah jalur terbalik dari tujuan ke posisi awal.
    cell=m._goal
    while cell!=start:
        jalur2[jalur[cell]]=cell
        cell=jalur[cell]
    return pencarian,jalur,jalur2 #perulangan selama cell tidak sama dengan start

if __name__=='__main__':
    m=maze(10,10) # Ukuran labirin (Dapat diganti sesuai kebutuhan)
   
    m.CreateMaze(loopPercent=55)
    pencarian,jalur,jalur2=ES(m)
    a=agent(m,footprints=True,color=COLOR.red,shape='square',filled=True)
    c=agent(m,1,1,footprints=True,color=COLOR.yellow,shape='square',filled=True,goal=(m.rows,m.cols))
    m.tracePath({a:pencarian},delay=100)
    m.tracePath({c:jalur},delay=100)
    textLabelJudul3(m,'IMPLEMENTASI ALGORITMA BRUTE FORCE METODE EXHAUSTIVE SEARCH  \t') ##Label header judul program
    textLabelJudul1(m, '\n             LABIRIN UKURAN 10x10   \t\n') #Label header ukuran labirin
    m.run()