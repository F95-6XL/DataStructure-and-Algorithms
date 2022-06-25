# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 21:21:10 2022

@author: Yimin Zhang
"""

class node:
    def __init__(self, data, pointer=None):
        self.data = data
        self.next = pointer
    
class list:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        
    def __len__(self):
        return self.length
        
    def __getitem__(self, index):
        return self.at(index).data
    
    def at(self, index) -> node:
        if self.length == 0 or index >= self.length or index < 0:
            raise ValueError("List index out of range!")
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur
    
    def push_back(self, data):
        cur = node(data)
        if self.head == None:
            self.head = cur
        else:
            self.tail.next = cur
        self.tail = cur
        self.length += 1
    
    def insert(self, index:int, data):
        if index == 0:
            new = node(data, self.head)
            self.head = new
        else:
            cur = self.at(index-1)
            new = node(data, cur.next)
            cur.next = new
        self.length += 1
        
    def delete(self, index:int):
        if self.length == 0:
            raise ValueError("Empty List")
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.at(index-1)
            cur.next = cur.next.next
        self.length -= 1
        
    def reverse(self):
        if self.length == 0:
            raise ValueError("Cannot reverse empty list!")
        prev = self.head
        cur = self.head.next
        for i in range(1, self.length):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        self.tail = self.head
        self.tail.next = None
        self.head = prev
        
    def find(self, data, index = 0) -> int:
        if self.length == 0 or index >= self.length:
            raise ValueError("List index out of range!")
        cur = self.at(index) 
        while cur != None:
            if cur.data == data:
                return index
            cur = cur.next
            index += 1
        return -1
    
    def isin(self, data) ->bool:
        return self.find(data) != -1
            
    def isempty(self) -> bool:
        return self.length==0
    
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

  
    
