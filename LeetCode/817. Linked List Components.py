class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        first = head
        second = head.next
        c = len(set(nums))
        while second:
            if first.val in nums and second.val in nums:
                c -= 1
            first = second
            second = second.next
        return c
