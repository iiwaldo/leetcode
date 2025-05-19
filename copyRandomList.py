
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old_to_new = {}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            copy_node = old_to_new[current]
            copy_node.next = old_to_new.get(current.next)
            copy_node.random = old_to_new.get(current.random)
            current = current.next
        
        return old_to_new.get(head)



