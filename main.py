import sys
from stats import numb_words, numb_charc, sorted_char_count

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents
  
def main():
  if len(sys.argv) < 2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    content = get_book_text(sys.argv[1])
    num_words = numb_words(content)
    num_char = numb_charc(content)
    sorted_char = sorted_char_count(num_char)
    print(f"Found {num_words} total words")
    print(num_char)
    for item in sorted_char:
      if item["char"].isalpha():
        print(f"{item["char"]}: {item["num"]}")


main()