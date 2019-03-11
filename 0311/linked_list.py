# Linked List

class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.link = n

def addFirst(data):
    global Head
    Head = Node(data, Head)


Head = None
addFirst(10)
addFirst(20)
addFirst(30)
# Head -> 30/link -> 20/link -> 10/None

print(Head.item)  # Head 의 item 이 아니라 Head 가 가리키는 item
# 30
print(Head.link.item)
# 20
print(Head.link.link.item)
# 10


