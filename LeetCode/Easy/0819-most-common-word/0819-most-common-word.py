class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = []
        currentword = ""
    
        for char in paragraph.lower():
            if char.isalpha():
                currentword += char
            elif currentword:
                words.append(currentword)
                currentword = ""
        if currentword:
            words.append(currentword)
            
        
        word_counts = {}
        for word in words:
            if word not in banned_set:
                word_counts[word] = word_counts.get(word, 0) + 1
                
        
        return max(word_counts, key=word_counts.get)


        