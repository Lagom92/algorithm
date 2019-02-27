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

while front != rear:   # 큐가 비어있지 않으면, 앞에서 하나씩 출력
    front += 1
    print(q[front])

print()

queue = []
queue.append(1)   #enqueue
queue.append(2)
queue.append(3)

while len(queue) > 0:   # dequeue: queue.pop(0)
    print(queue.pop(0))
