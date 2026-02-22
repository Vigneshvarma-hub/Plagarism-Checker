def check_plagiarism(text1, text2):
    words1 = text1.split()
    words2 = text2.split()
    
    common = set(words1) & set(words2)
    
    similarity = (len(common) / max(len(set(words1)), 1)) * 100
    
    return f"Similarity: {round(similarity, 2)}%"


text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

result = check_plagiarism(text1, text2)
print(result)