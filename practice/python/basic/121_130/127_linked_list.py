from icecream import ic

class Node:
    def __init__(self, data:str):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = None
 
    def show(self):
        tmp = self.head.next
        while tmp:
            ic(tmp.data)
            tmp = tmp.next
    
    # 末尾に追加する
    def append(self, node:Node):
        # 何も入っていないとき
        if self.head.next is None:
            self.head.next = node
            self.tail = node
            node.prev = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    # target_nodeの前に挿入する
    def insert_before(self, target_node:Node, insert_node:Node):
        target_node.prev.next = insert_node
        insert_node.next = target_node
        target_node.prev = insert_node

    # target_nodeの後に挿入する
    def insert_after(self, target_node:Node, insert_node:Node):
        if target_node.next is None:
            target_node.next = insert_node
            insert_node.prev = target_node
            self.tail = insert_node
        else:
            target_node.next.prev = insert_node
            insert_node.next = target_node.next
            target_node.next = insert_node

    # nodeを削除する
    def delete(self, node:Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node


linked_list = LinkedList()
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')

linked_list.append(node_a)
linked_list.append(node_b)
linked_list.insert_before(target_node=node_b, insert_node=node_c)
linked_list.insert_after(target_node=node_b, insert_node=node_d)
linked_list.insert_after(target_node=node_b, insert_node=node_e)
linked_list.append(node_f)
linked_list.show()

print('-'*20)
linked_list.delete(node_b)
linked_list.show()
