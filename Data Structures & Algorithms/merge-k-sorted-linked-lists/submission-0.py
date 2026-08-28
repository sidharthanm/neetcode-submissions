# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head  = ListNode()
        temp = head
        # print(lists)
        while True:
            curmax = float("inf")
            track = None
            # x+=1
            
            for i in range(len(lists)):
                # x+=1
                if lists[i] and lists[i].val < curmax:
                    curmax = lists[i].val
                    track = i
            # print(track,curmax)
            # print(temp)
            if track==None:
                return temp.next
            head.next = lists[track]
            head = head.next
            lists[track] = lists[track].next
        
        return temp.next

        
