class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        vowels = {'a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"}

        sentence = sentence.split()
        ans = []
        for i,word in enumerate(sentence):
            if word[0] in vowels:
                curr = word[0:] + "ma" + (i+1) * "a"
            else:
                curr = word[1:] + word[0] + "ma" + (i+1) * "a"
            ans.append(curr)

        return " ".join(ans)