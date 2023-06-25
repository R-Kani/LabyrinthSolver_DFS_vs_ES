#import modul maze,agent,textLabel,COLOR dari library pyamaze
from pyamaze import maze,agent,COLOR,textLabelJudul2,textLabelJudul3

def DFS(m,start=None):
    if start is None: #jika startnya tidak ada maka definisikan start secara default 
        start=(m.rows,m.cols) #yaitu di sudut kanan bawah labirin
    
    explored=[start] #list untuk menyimpan sel-sel yang telah dikunjungi
    selanjutnya=[start] #list untuk menyimpan sel-sel yang berada di frontier, yaitu sel-sel yang akan dieksplorasi selanjutnya.
    jalur={} #dictionary untuk menyimpan jalur dari sel saat ini ke sel tetangganya
    pencarian=[] #list untuk menyimpan urutan sel-sel yang dikunjungi selama proses pencarian

    while len(selanjutnya)>0: #perulangan jika panjang array selanjutnya > 0 atau selama masih ada sel dalam frontier (selanjutnya) yang akan dieksplorasi
        currCell=selanjutnya.pop() #inisiasi currCell dengan pop dari array selanjutnya
        pencarian.append(currCell) #menambahkan currCell ke dalam array pencarian
        if currCell==m._goal: #jika currCell yang ditempati == goal maka perulangan dihentikan karena tujuan telah tercapai
            break
        
        cabang=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True: #periksa apakah sel tersebut dapat diakses 
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                cabang+=1 #jika terdapat sebuah jalur bercabang maka cabang + 1
                explored.append(child)
                selanjutnya.append(child)
                jalur[child]=currCell
        if cabang>1: #jika jalur yang dapat dipilih terdapat > 1
            m.markCells.append(currCell) #sel yang ditandai akan menjadi currCell
    jalur2={} #dictionary untuk mengunjungi jalur secara terbalik sehingga terbentuklah jalur terbalik dari tujuan ke posisi awal
    cell=m._goal
    while cell!=start: #perulangan selama cell tidak sama dengan start
        jalur2[jalur[cell]]=cell
        cell=jalur[cell]

    return pencarian,jalur,jalur2

if __name__=='__main__':
    m=maze(10,10) # Ukuran labirin (Dapat diganti sesuai kebutuhan)
    m.CreateMaze(loopPercent=35) # loop percent = tingkat kesulitan untuk skala 100-1 (semakin rendah semakin susah)

    pencarian,jalur,jalur2=DFS(m,(10,10)) # (10,10) adalah Start (Dapat diganti sesuai kebutuhan, namun dengan koordinat yang valid)

    #Jejak pergerakan untuk mencari Goal
    a=agent(m,10,10,goal=(1,1),footprints=True,shape='square',color=COLOR.cyan)
    b=agent(m,1,1,goal=(10,10),footprints=True,filled=True,color=COLOR.yellow)
    m.tracePath({a:pencarian},showMarked=True,delay=500)
    m.tracePath({b:jalur},delay=250)
    textLabelJudul3(m,'IMPLEMENTASI ALGORITMA BACKTRACKING METODE DFS  \t') ##Label header judul program
    textLabelJudul2(m, '\n             LABIRIN UKURAN 10x10   \t\n') #Label header ukuran labirin
    m.run()

