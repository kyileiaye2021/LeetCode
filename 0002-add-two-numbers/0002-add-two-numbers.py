# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # 2, 4, 3
        # 5, 6, 4
        # 7, 0, 8

        # 9, 9, 9
        # 9, 9, 9, 9
        # 8, 9, 9, 0, 1

        # 1
        # 0, 1
        # 1, 1

        # recur(i, j, carry)
        # base case
        # if not i and not j and carry = 0:
        #   return None

        # recursive step
        # if not i:
        #   i val = 0 else i val = i.val
        # if not j
        #   j val = 0 else j val = j.val
        # total = i val + jval + carry
        # new node = ListNode(total % 10)
        # new carry = total // 10
        # new_node.next = recur(i.next, j.next, new carry)
        # return new node

        def recur(i, j, carry):
            if not i and not j and carry == 0:
                return None

            i_val = i.val if i else 0
            j_val = j.val if j else 0

            total = i_val + j_val + carry
            new_node = ListNode(total % 10)
            new_carry = total // 10

            next_i = i.next if i else None
            next_j = j.next if j else None

            new_node.next = recur(next_i, next_j, new_carry)
            return new_node

        i = l1
        j = l2
        carry = 0
        return recur(i, j, carry)

        # i = l1
        # j = l2
        # carry = 0
        # dummy = ListNode()
        # curr = dummy

        # while i and j:
        #     new_node_val = (i.val + j.val + carry) % 10
        #     carry = (i.val + j.val + carry) // 10
        #     new_node = ListNode(new_node_val)
        #     curr.next = new_node
        #     curr = curr.next
        #     i = i.next
        #     j = j.next

        # while i:
        #     new_node_val = (i.val + carry) % 10
        #     carry = (i.val + carry) // 10
        #     new_node = ListNode(new_node_val)
        #     curr.next = new_node
        #     curr = curr.next
        #     i = i.next

        # while j:
        #     new_node_val = (j.val + carry) % 10
        #     carry = (j.val + carry) // 10
        #     new_node = ListNode(new_node_val)
        #     curr.next = new_node
        #     curr = curr.next
        #     j = j.next

        # if carry > 0:
        #     new_node = ListNode(carry)
        #     curr.next = new_node


        # return dummy.next


