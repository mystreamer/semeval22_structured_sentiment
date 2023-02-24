import stanza
stanza.download('en')
# stanza.download('eu')
# stanza.download('es')
# stanza.download('no')
stanza_nlp = stanza.Pipeline('en')