with open("books/frankenstein.txt") as f:
  file_content = f.read()

  def word_length(file):
    return len(file.split())

  def count_chars(file):
    chars = {}
    lowered = file.lower()
    for char in lowered:
      if char in chars:
        chars[char] += 1
      else:
        chars[char] = 1
    return chars

  def book_report(file):
    # --- Begin report of books/frankenstein.txt ---
    # 77986 words found in the document
    # The 'e' character was found 46043 times
    # result = [[k, len(v)] for k,v in Dict.items()]

    word_len = word_length(file)
    char_count = count_chars(file)
    letters_count = []
    for letter, count in char_count.items():
      if letter.isalpha():
        letters_count.append((letter, count))

    sorted_letters_count = sorted(letters_count, key=lambda letters: letters[0])
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_len} words found in the document")
    for letter, count in sorted_letters_count:
      print(f"The letter '{letter}' was found {count} times")
    print("--- End report ---")

  book_report(file_content)