def numb_words(book):
  words = book.split()
  count = len(words)
  return count

def numb_charc(text):
  char_count = {}
  lowercase = text.lower()
  for char in lowercase:
    if char not in char_count:
      char_count[char] = 1
    else:
      char_count[char] += 1
  return char_count

def sorted_char_count(dict):
  sorted_list = []

  def sort_on(dict):
    return dict["num"]
  
  for key in dict:
    sorted_list.append({"char": key, "num": dict[key]})

  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list