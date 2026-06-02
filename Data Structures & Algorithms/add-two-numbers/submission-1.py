# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy head for the result list and a pointer to the current node
        dummy = ListNode(0)
        current = dummy
        carry = 0

         # Loop through both lists until both reach the end and there is no carry-over
        while l1 or l2 or carry:
            # Get the values of the current nodes or 0 if a list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the digits and the carry
            total_sum = val1 + val2 + carry

            # The new digit is the sum modulo 10
            carry = total_sum // 10
            new_digit = total_sum % 10
            
            # Create a new node with the digit and append it to the result list
            current.next = ListNode(new_digit)
            current = current.next

            # Move to the next nodes in the input lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # The result linked list starts from the next of the dummy head        
        return dummy.next



