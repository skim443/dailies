# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Here is the function signature as a starting point (in Python):
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        # Fill this in.
        int_result = self.listnode_list_to_integer(
            l1) + self.listnode_list_to_integer(l2)
        print("int result:{}".format(int_result))
        result = self.int_to_listnode_list(int_result)
        return result

    def int_to_listnode_list(self, int_result):
        int_str = str(int_result)
        int_str = "".join(reversed(int_str))

        result = None
        prevNode = None
        for idx, char in enumerate(int_str):
            newNode = ListNode(char)
            # first time through, so store pointer to first node
            if idx == 0:
                result = newNode
            else:
                prevNode.next = newNode
            prevNode = newNode

        return result

    def listnode_list_to_integer(self, l1):
        stack = []
        node = l1
        while node:
            stack.append(node.val)
            node = node.next

        int_str = ""
        for idx in range(0, len(stack)):
            int_str += str(stack.pop())

        print("list to int: {}".format(int_str))
        return int(int_str)


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
