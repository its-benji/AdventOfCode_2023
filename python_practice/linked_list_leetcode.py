
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        l1 = list1
        l2 = list2
        ret = None
        retHead = None

        if l1 == None and l2 == None:
            return ret
        elif l1 == None:
            ret = ListNode(l2.val, None)
            l2 = l2.next
        elif l2 == None:
            ret = ListNode(l1.val, None)
            l1 = l1.next
        elif l1.val <= l2.val:
            ret = ListNode(l1.val, None)
            l1 = l1.next
        else:
            ret = ListNode(l2.val, None)
            l2 = l2.next
        retHead = ret
        while l1 != None or l2 != None:
            if l1 == None:
                ret.next = ListNode(l2.val, None)
                ret = ret.next
                l2 = l2.next
                continue
            if l2 == None:
                ret.next = ListNode(l1.val, None)
                ret = ret.next
                l1 = l1.next
                continue
            
            if l1.val <= l2.val:
                ret.next = ListNode(l1.val, None)
                ret = ret.next
                l1 = l1.next
            else:
                ret.next = ListNode(l2.val, None)
                ret = ret.next
                l2 = l2.next

        return retHead

def dict_to_listnode(dict):
    if not dict:
        return None
    head = ListNode(dict['val'])
    current = head
    next_dict = dict.get('next')
    while next_dict is not None:
        current.next = ListNode(next_dict['val'])
        next_dict = next_dict.get('next')
        current = current.next
    return head 

t1 = {"val": 1, "next": {"val": 1, "next": {"val": 4, "next": None}}}
t2 = {"val": 1, "next": {"val": 2, "next": {"val": 3, "next": None}}}
list1 = dict_to_listnode(t1)
list2 = dict_to_listnode(t2)
mtl1 = Solution()
ret = mtl1.mergeTwoLists(list1, list2)

while ret != None:
    print(ret.val)
    ret = ret.next
