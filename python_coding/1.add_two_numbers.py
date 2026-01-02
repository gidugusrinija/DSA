
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        

class AddTwoNumbers:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total%10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


l1 = ListNode(2, ListNode(4, ListNode(6)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

AddTwoNumbers().add_two_numbers(l1, l2)
