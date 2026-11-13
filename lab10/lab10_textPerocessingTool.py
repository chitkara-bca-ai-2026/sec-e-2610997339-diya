# Header
print("========================================")
print("          TEXT PROCESSING TOOL")
print("========================================")

# 1. Accept a sentence from the user
sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

# 2. Display character at a specific position using indexing
index_pos = int(input("Enter position for indexing: "))
print(f"Character at position {index_pos} : '{sentence[index_pos]}'")

# 3. Extract a portion of the sentence using string slicing
start_idx = int(input("Enter start index for slicing : "))
end_idx = int(input("Enter end index for slicing   : "))
sliced_str = sentence[start_idx:end_idx]
print(f"Sliced string [{start_idx}:{end_idx}]         : '{sliced_str}'")

# 4. Convert to uppercase
print(f"Uppercase                      : {sentence.upper()}")

# 5. Convert to lowercase
print(f"Lowercase                      : {sentence.lower()}")

# 6. Replace a specified word with another word
word_to_replace = input("Enter word to replace          : ")
replacement_word = input("Enter replacement word         : ")
replaced_sentence = sentence.replace(word_to_replace, replacement_word)
print(f"After replace                  : {replaced_sentence}")

# 7. Length of sentence
print(f"Length of sentence             : {len(sentence)}")

# Footer
print("========================================")
print("Analysis Complete!")
print("========================================")