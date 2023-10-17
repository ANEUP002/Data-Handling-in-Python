def main():
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")

    try:
        with open(file1, "r") as file1_content, open(file2, "r") as file2_content:
            operation(file1_content, file2_content)
    except FileNotFoundError:
        raise FileExistsError
    

def operation(file1_content, file2_content):
    words1 = file1_content.read().split()
    words2 = file2_content.read().split()

    word_count1 = {}
    word_count2 = {}

    for word in words1:
        word_count1[word] = word_count1.get(word, 0) + 1

    for word in words2:
        word_count2[word] = word_count2.get(word, 0) + 1

    common_words = set(words1) & set(words2)

    sorted_common_words = sorted(common_words, key=lambda word: (word_count1.get(word, 0) + word_count2.get(word, 0)), reverse=True)

    for word in sorted_common_words:
        print(f"{word}: {word_count1.get(word, 0) + word_count2.get(word, 0)} times")

if __name__ == "__main__":
    main()