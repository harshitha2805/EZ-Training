lass Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr=head
        s=''
        while(curr):
           s+=str(curr.val)
           curr=curr.next
        return int(s,2)