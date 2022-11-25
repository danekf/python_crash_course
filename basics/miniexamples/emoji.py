message = input(">")

words = message.split(' ')

emojis = {
  ":)": "😃",
  ":(": "😞"
}
output = ""

for word in words:
  #search for the word in emojis, if non found, default to the word
  output += emojis.get(word, word) + " "

print(output)