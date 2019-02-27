# 연습문제 1, 큐

def enq(n):
    global rear
    rear += 1
    q[rear] = n

q = [0]*10
front = -1
rear = -1

rear += 1   # enqueue
q[rear] = 1

enq(2)
enq(3)

while front != rear:   # 큐가 비어있지 않으면
    front += 1
    print(q[front])
