from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
with open('verb.txt', 'r') as i:
	word_list = [word.strip() for word in i.readlines()]


wnl = WordNetLemmatizer()
st = LancasterStemmer()

with open('d.txt', 'w') as b:
	for word in word_list:
		word = wnl.lemmatize(word.strip())
		if word[-3:] == 'ing' or word[-2:] == 'ed':
			word = st.stem(word)
		b.write(word)
		b.write('\n')