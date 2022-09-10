# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        """
        idea is to simply use next node of the Linked list
		
        Currently, we have
        4-->5-->1-->9
		
        we want to delete 5
        So node 5 is pointing to node 1
        so our LinkedList looks like this -
            -------         -------         -------
           | 5 | --|-----> | 1 | --|-----> | 9 | --|----->
            -------         -------         -------
            
            now what we can do here, put/copy the value of node 1 in node 5
            
            -------         -------         -------
           | 1 | --|-----> | 1 | --|-----> | 9 | --|----->
            -------         -------         -------
        
        now we can just point new node 1 (which was
        earlier holding val 5) to the next of initial node 1 (which 
        is 9)
        
                       .--------------.        
            -------    |    -------   |      -------
           | 1 | --|---`   | 1 | --|  `---->| 9 | --|----->
            -------         -------          -------
                
            In python, we dont have worry about GC, so yeah, Thats it
        
        """
#       Initial
#            -------         -------         -------
#           | 5 | --|-----> | 1 | --|-----> | 9 | --|----->
#            -------         -------         -------

        node.val = node.next.val
#       data copied
#            -------         -------         -------
#           | 1 | --|-----> | 1 | --|-----> | 9 | --|----->
#            -------         -------         -------

        node.next = node.next.next
#       final
#                       .--------------.
#           -------    |    -------   |      -------
#          | 1 | --|---`   | 1 | --|  `---->| 9 | --|----->
#           -------         -------          -------
