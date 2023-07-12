import nltk
import operator
import docx2txt

# extract text
path = input("DOCX document path: ")
text = docx2txt.process(path)
tokens = nltk.word_tokenize(text)

token_frequencies: dict[str, int] = {}
for word in tokens:
    lowered_token = word.lower()
    prev_frequency = token_frequencies.get(lowered_token, 0)
    token_frequencies[lowered_token] = prev_frequency + 1

token_frequency_tuples: list[tuple[str, int]] = [(k, v) for k, v in token_frequencies.items()]
token_frequency_tuples.sort(key=operator.itemgetter(1, 0)) # Frequency first, then token.

with open("output.txt", mode="w", encoding="utf-8") as f:
    for token, frequency in token_frequency_tuples:
        print(token, frequency, sep="\t", file=f)

print("Done! :D")
