import nltk
nltk.download('punkt_tab')

text = "Hello, world! This is a test. Let's see how it works."
wtokens = nltk.word_tokenize(text)
#print("Word tokens: ", wtokens)

stokens = nltk.sent_tokenize(text)
#print("Sentence tokens: ", stokens)

text2 = "Shivi123$ !@####$%$%^%^&^&**(). India is a country. It has many states"
def preprocess_text(t):
    # Tokenize the text into words
    wtokens2 = nltk.word_tokenize(t.lower())
    print("Word tokens: ", wtokens2)

    return [word for word in wtokens2 if word.isalnum()]

print(' '.join(preprocess_text(text2)))
