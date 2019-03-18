# 뿌요뿌요_백
#import sys
#sys.stdin = open('input.txt', 'r')

def bfs(i, j): # 탐색과 삭제
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    v = [[0]*6 for i in range(12)]
    q = [0]*12*6*2
    front = -1
    rear = -1

    rear +=1
    q[rear] = i
    rear += 1
    q[rear] = j
    v[i][j] = 1
    cnt = 0
    while(front != rear):
        front +=1
        i = q[front]
        front +=1
        j = q[front]
        cnt +=1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if(ni>=0 and ni<12 and nj>=0 and nj<6):
                if(puyo[ni][nj] == puyo[i][j] and v[ni][nj]==0):
                    rear += 1
                    q[rear] = ni
                    rear += 1
                    q[rear] = nj
                    v[ni][nj] = v[i][j] + 1
    if cnt>=4: # 터뜨리기
        for i in range(12):
            for j in range(6):
                if(v[i][j]!=0):
                    puyo[i][j] = '.'
        return 1
    return 0

def mv():

    for j in range(6):
        for i in range(10, -1, -1):
            idx = i   #  i부터
            while(idx<11 and puyo[idx][j]!='.' and puyo[idx+1][j] == '.'): #아래칸이 '.'이면 내림
                puyo[idx+1][j] = puyo[idx][j]
                puyo[idx][j] = '.'
                idx += 1


puyo = [list(input()) for i in range(12)]

turn = 0
while(1):
    r = 0

    for i in range(12):
        for j in range(6):
            if(puyo[i][j] != '.'):
                r += bfs(i, j)

    if r>0: # 지워진 횟수를 탐색
        if mv()!=0:  # 지워진 공간 채우기
            turn += 1
    else:
        break #더이상 지워지지 않으면 중단

print(turn)