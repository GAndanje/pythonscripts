class Node:
    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode
        print('inside Node class')
        print(self.data,":",self.nextNode)
class linkedList:
    def __init__(self,head=None):
        self.head=head
        print('inside linkedlist class')
        print(self.head)
    def insertMethod(self,nodeobject):
        if self.head ==None:
            self.head= Node(nodeobject)
            return self.head
        currentNode =self.head
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
        currentNode.nextNode =Node(nodeobject)
        return f'assigned node {currentNode.nextNode.data}'
    def displaylinkedList(self):
        nodesList = []
        currentNode =self.head
        while currentNode.nextNode != None:
            nodesList.append(f'{currentNode.data}:{currentNode.nextNode.data}')
            currentNode = currentNode.nextNode
        nodesList.append(None)
        print(nodesList,len(nodesList))
        

linkedList1 =linkedList()
linkedList1.insertMethod(1)
print('-------')
linkedList1.insertMethod(2)
linkedList1.insertMethod(3)
linkedList1.insertMethod(4)
print('--------')
# print(linkedList1.head.data)#1
# print(linkedList1.head.nextNode.data)#2
# print(linkedList1.head.nextNode.nextNode.data)#3
# print(linkedList1.head.nextNode.nextNode.nextNode.data)#4
# print(linkedList1.head.nextNode.nextNode.nextNode.nextNode)#none
print(linkedList1.displaylinkedList())


