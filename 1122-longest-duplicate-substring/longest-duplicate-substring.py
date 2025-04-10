class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def rabin_karp(text, length):
            d = 26  # number of characters in the input alphabet
            q = 101111  # a prime number
            n = len(text)
            m = length
            h = pow(d, m - 1) % q
            t = 0  # hash value for text

            # Preprocessing: calculate hash value of pattern and first window of text
            for i in range(length):
                t = (d * t + ord(text[i])) % q

            # Slide the pattern over text one by one
            visited = {}
            for i in range(n - m + 1):
                # Check the hash values
                if t in visited:
                    # If hash values match, check characters one by one
                    if t in visited and  text[i:i+length] == visited[t]:
                        return text[i:i+length]
                # Calculate hash value for next window
                visited[t] = text[i:i+length]
                if i < n - m:
                    t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                    if t < 0:
                        t += q

            return -1

        # Example usage
        # text = "abedabcabcabc"
        # pattern = "abc"
        l = 0
        r = len(s)-1
        res = ""
        while l <= r:
            mid = (l+r) // 2
            result = rabin_karp(s, mid)
            # print(mid ,result)
            if result != -1:
                res = result
                l = mid + 1
            else:
                r = mid - 1

        return res

                