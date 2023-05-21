def addTwoNumbers(nbr_lit1:list[int],nbr_lit2:list[int]) -> list[int]:
    nbr1 = int(''.join(str(num) for num in nbr_lit1))
    nbr2 = int(''.join(str(num) for num in nbr_lit2))
    return [int(digit) for digit in str(nbr1+nbr2)][::-1]

def addTwoNumbers2(nbr_lit1: list[int], nbr_lit2: list[int]) -> list[int]:
    result = []
    carry = 0
    i, j = 0, 0

    while i < len(nbr_lit1) or j < len(nbr_lit2) or carry != 0:
        digit_sum = carry

        if i < len(nbr_lit1):
            digit_sum += nbr_lit1[i]
            i += 1

        if j < len(nbr_lit2):
            digit_sum += nbr_lit2[j]
            j += 1

        digit = digit_sum % 10
        carry = digit_sum // 10

        result.append(digit)

    return result



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def convert_to_list(self):
        result = []
        node = self  
        while node:
            result.append(node.val)
            node = node.next
        return result

    def __str__(self) -> str:
        return str(self.convert_to_list())


def addTwoNumbers_node(l1:ListNode, l2:ListNode) ->ListNode :
    dummy = ListNode()  
    curr = dummy  
    
    carry = 0  
    
    while l1 or l2 or carry:
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        
        carry = sum_val // 10
        curr.next = ListNode(sum_val % 10)
        curr = curr.next
    
    return dummy.next  

def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = addTwoNumbers_node(l1, l2)
    l=addTwoNumbers([2,4,3],[5,6,4])
    z =  addTwoNumbers2([2,4,3],[5,6,4])

    print(l)
    print(z)
    print(result)
