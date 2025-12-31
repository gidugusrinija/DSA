class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    def add_two_numbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        if not l1 and not l2 and not carry:
            return None

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        node = ListNode(total % 10)

        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None
        node.next = self.add_two_numbers(next1, next2, carry)

        return node


l1 = ListNode(2, ListNode(4, ListNode(6)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = AddTwoNumbers().add_two_numbers(l1, l2)  


