def group_anagrams(words):
    # replace this with your implementation
    pass

if __name__ == "__main__":
    input_words = input("Enter words separated by spaces: ").split()
    anagrams_grouped = group_anagrams(input_words)
    print("Grouped Anagrams:")
    for group in anagrams_grouped:
        print(group)
