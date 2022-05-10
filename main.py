file = open('morse_code.txt', 'r', encoding='UTF-8')
lines = file.readlines()

morse_code_dict = {}

for line in lines:
  (k,v) = line.split()
  morse_code_dict[k] = v

def converter(word):
  word_m = ""
  word = word.upper()
  for letter in word:
    word_m += f"{morse_code_dict[letter]}  "

  return word_m