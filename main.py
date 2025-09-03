import nltk
from textblob import TextBlob
from newspaper import Article

# Scarico i pacchetti necessari per analizzare il testo
nltk.download('punkt')
nltk.download('punkt_tab')

# Link della pagina da cui voglio prendere l’articolo
url = 'https://www.ilfoglio.it/tecnologia/2025/09/03/news/nell-ultimo-anno-gli-attacchi-hacker-in-italia-sono-aumentati-del-98-per-cento-8051593/'

# Creo un oggetto "articolo" partendo dal link
article = Article(url)

# Scarico il contenuto della pagina
article.download()

# Estraggo il testo e le informazioni
article.parse()

# Faccio un riassunto automatico con .nlp
article.nlp()

print(f"Title: {article.title}") # Stampa il titolo
print(f"Authors: {article.authors}") # Stampa gli autori
print(f"Publication Date: {article.publish_date}")  # Stampa la data di pubblicazione
print(f"Summary: {article.summary}") # Stampa il riassunto
