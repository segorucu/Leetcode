from collections import deque
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def createline(length,left,right):
            nspace = right - left
            totspace = maxWidth - length
            if nspace == 0:
                return words[left] + totspace * " "
            rem = totspace % nspace
            gap = totspace // nspace
            count = 0
            if rem > 0: 
                count = 1
            txt = words[left] + (count+gap) * " "
            for i in range(left+1,right):
                if count < rem:
                    txt += words[i] + (gap+1) * " "
                    count += 1
                else:
                    txt += words[i] + (gap) * " "

            txt += words[right]
            
            return txt

        left = 0
        right = 0
        length = space = 0
        ans = []
        while right < len(words):
            length += len(words[right])
            if left != right:
                space += 1
            if length + space > maxWidth:
                length -= len(words[right])
                txt = createline(length,left,right-1)
                ans.append(txt)
                left = right
                length = 0
                space = 0
            else:
                right += 1
            if right == len(words):
                txt = words[left] 
                sm = len(words[left])
                for i in range(left+1,right):
                    txt += " " + words[i]
                    sm += len(words[i]) + 1
                txt += (maxWidth - sm) * " "
                
                ans.append(txt)

        return ans


        