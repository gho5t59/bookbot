def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    #print(file_contents)
    words = file_contents.split()
    #print(len(words))
    lower_strings = file_contents.lower()
    letters = {}
    for key in lower_strings:
      if key in letters:
        letters[key] += 1
      else:
        letters[key] = 1
    #print(letters)
    a = []
    for letter in letters:
      a.append({letter:letters[letter]})
    a.sort(reverse=True, key=sort_on)
    for dict in a:
      for i in dict:
        if i.isalpha():
          print(f"The '{i}' character was found {dict[i]} times")    

    return letters

def sort_on(dict):
  for i in dict:
    return dict[i]
main()