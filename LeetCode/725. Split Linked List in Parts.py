# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        res = [None]*k
        # length of each part
        part = length//k

        # if we have some remainder like for if length is 10 and k is 3 then, part=3 but 3+3+3=9 so our rmainder will be 1
        rem = length % k

        i = 0  # starting index

        while head != None:
            c = 1
            # lets calculate how much length we will use
            if rem > 0:
                total_length = part+1  # 1 cause max size difference should be 1
            else:
                total_length = part
            while c <= total_length:
                # if its starting again or like first time
                if c == 1:
                    res[i] = head
                if c < total_length:
                    # join
                    head = head.next
                if c == total_length:
                    curr = head
                    # here we move our head ptr but we want crea anothe ptr and last position so we can just point it to None-
                    head = head.next
                    curr.next = None
                c += 1
            i += 1
            if rem:
                rem -= 1
        return res
