class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        mp = collections.defaultdict(list)
        m = len(searchWord)
        products.sort()
        for product in products:
            n = min(len(product),m)
            for i in range(n):
                if product[i] == searchWord[i]:
                    if len(mp[i]) < 3:
                        mp[i].append(product)
                else:
                    break

        ans = []
        for i in range(m):
            ans.append(mp[i])

        return ans
        