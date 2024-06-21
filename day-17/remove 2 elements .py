def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        front=ListNode()
        front.next=head
        curr=front
        prev=None
        while curr!=None:
            if curr.val==val:
                if(prev!=None):
                    prev.next=prev.next.next
                    curr=prev
                else:
                    prev=None
                    break
            prev=curr
            curr=curr.next
        return front.next