class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d={}
        a="abcdefghijklmnopqrstuvwxyz"
        m=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(len(a)):
            d[a[i]]=m[i]
        l=[]
        for i in words:
            s=''
            for j in i:
                s+=d[j]
            l.append(s)
        return len(set(l))            