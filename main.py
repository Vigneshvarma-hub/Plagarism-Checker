def check_plagiarism(text1, text2):
    if text1 == text2:
        return "100% Plagiarism"
    else:
        return "Not identical"

print(check_plagiarism("hello", "hello"))