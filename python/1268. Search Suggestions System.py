from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        # Sort products lexicographically
        products.sort()
        result = []
        prefix = ""
        start = 0  # Start index for binary search to optimize
        
        for char in searchWord:
            prefix += char
            # Find the first product >= prefix
            start = bisect_left(products, prefix, start)
            suggestions = []
            # Check next up to 3 products from start index
            for i in range(start, min(start + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            result.append(suggestions)
        
        return result
