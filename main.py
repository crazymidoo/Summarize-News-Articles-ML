import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# Creiamo una funzione per il bottone Summarize
def summarize():
    
    url = utext.get('1.0', 'end').strip() # Otteniamo URL dal TextBox

    # Creo un oggetto "articolo" partendo dal link
    article = Article(url)

    # Scarico il contenuto della pagina
    article.download()

    # Estraggo il testo e le informazioni
    article.parse()

    # Faccio un riassunto automatico con .nlp
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    authors = ", ".join(article.authors) if article.authors else "Unknown"
    author.delete('1.0', 'end')
    author.insert('1.0', authors)

    pub_date = str(article.publish_date) if article.publish_date else "Unknown"
    publication.delete('1.0', 'end')
    publication.insert('1.0', pub_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # Analizzo il testo per capire se positivo, negativo o neutro
    analysis = TextBlob(article.text)

    sentiment.delete('1.0', 'end')

    # In base al valore, mostriamo se il testo è positivo, negativo o neutro
    sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral" }')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# Creo una GUI
root = tk.Tk()
root.title("News Summarizer")  # Titolo
root.geometry('1200x600')      # Dimensione finestra

# --- Titolo ---
tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')  # Disabled perchè non vogliamo permettere all'utente di inserire qualcosa
title.pack()

# --- Autore ---
alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

# --- Data di pubblicazione ---
plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

# --- Riassunto ---
slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140) # Cambiamo height
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# --- Analizza Sentimenti ---
selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140) 
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# --- URL ---
ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

# --- Bottone --
btn = tk.Button(root, text = "Summarize", command = summarize)
btn.pack()

root.mainloop()
