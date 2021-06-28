#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:08:13 2021
@author: evelynebushuru
"""

class BinaryNode:
    def __init__(self,nodevalue):
        self.nodeValue = nodevalue
        self.leftNode = None
        self.rightNode = None
class BinaryTree:
    def __init__(self,root=None):
        self.root = root
    def add2Tree(self,nodeobject):
        if self.root == None:
            self.root = BinaryNode(nodeobject)
            return self
        currentBNode= self.root
        while True:
            if currentBNode.rightNode is None and currentBNode.leftNode is None:
                if nodeobject>= currentBNode.nodeValue:
                    currentBNode.rightNode = BinaryNode(nodeobject)
                    return self
                else:
                    currentBNode.leftNode = BinaryNode(nodeobject)
                    return self
            elif currentBNode.rightNode is None:
                if nodeobject  >= currentBNode.nodeValue:
                    currentBNode.rightNode = BinaryNode(nodeobject)
                    return self
            elif currentBNode.leftNode is None:
                if nodeobject < currentBNode.nodeValue:
                    currentBNode.leftNode = BinaryNode(nodeobject)
                    return self
            else:
                if nodeobject >=currentBNode.rightNode.nodeValue:
                    currentBNode = currentBNode.rightNode
                else:
                    currentBNode = currentBNode.leftNode
                                            # 100 root                                  100         root
                                            #     \                                    /    \
                                            #     150  rightNode                      8      200        root.rightNode
                                            #         \                              /          \
                                            #         200 rightNode                None         None        root.rightNode.rightnode
                                            #        /
                                            #        8       leftNode
BT1 = BinaryTree()
BT1.add2Tree(100)
BT1.add2Tree(150)
BT1.add2Tree(200)
BT1.add2Tree(8)

print(BT1.root.rightNode)



