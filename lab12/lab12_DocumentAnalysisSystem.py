# 1. Take input from the user
sentence = input("Enter a sentence: ")

# Header Banner
print("========================================")
print("       DOCUMENT ANALYSIS REPORT")
print("========================================")
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")

# 2. Initialize counters
vowels_count = 0
consonants_count = 0
digits_count = 0
spaces_count = 0
special_chars_count = 0

vowels_set = set("aeiouAEIOU")

# Analyze each character in the sentence
for char in sentence:
    if char.isalpha():
        if char in vowels_set:
            vowels_count += 1
        else:
            consonants_count += 1
    elif char.isdigit():
        digits_count += 1
    elif char.isspace():
        spaces_count += 1
    else:
        special_chars_count += 1

# Count words by splitting by whitespace
words_count = len(sentence.split())

# Calculate totals and percentage
total_letters = vowels_count + consonants_count
vowel_percentage = (vowels_count / total_letters * 100.0) if total_letters > 0 else 0.0

# 3. Display Character Breakdown
print("\n--- Character Breakdown ---")
print(f"Words:             {words_count}")
print(f"Vowels:            {vowels_count}")
print(f"Consonants:        {consonants_count}")
print(f"Digits:            {digits_count}")
print(f"Spaces:            {spaces_count}")
print(f"Special characters: {special_chars_count}")

# Summary Section
print("\n--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")

# Footer
print("========================================")
print("Analysis Complete!")
print("========================================")