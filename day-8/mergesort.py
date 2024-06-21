def mergesort(l,start,end):
    if start<end:
        mid=(start+end)//2
        mergesort(l,start,mid)
        mergesort(l,mid+1,end)
        merge(l,start,mid,end)
def merge(l,start,mid,end):
    