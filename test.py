import nltk
nltk.download('punkt')
nltk.download('wordnet')
import pymorphy2

def create_lemmatization_dict(text):
    lemmatization_dict = {}
    tokens = nltk.word_tokenize(text)
    morph = pymorphy2.MorphAnalyzer()

    for token in tokens:
        lemma = morph.parse(token)[0].normal_form
        if lemma not in lemmatization_dict:
            lemmatization_dict[lemma] = [lemma]
        else:
            lemmatization_dict[lemma].append(lemma)

    return lemmatization_dict

def generate_text(text, lemmatization_dict):
    sentences = nltk.sent_tokenize(text)
    morph = pymorphy2.MorphAnalyzer()

    generated_sentences = []
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        generated_tokens = []
        for token in tokens:
            lemma = morph.parse(token)[0].normal_form
            if lemma in lemmatization_dict:
                generated_tokens.append(lemmatization_dict[lemma].pop(0))  # Берем первую лемму из списка и удаляем ее
            else:
                generated_tokens.append(lemma)

        generated_sentence = ' '.join(generated_tokens)
        generated_sentences.append(generated_sentence)

    return '\n'.join(generated_sentences)

with open('C:/Users/pasha/OneDrive/Рабочий стол/IAD/лаб_6/ras_arbitr.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lemmatization_dict = create_lemmatization_dict(text)
generated_text = generate_text(text, lemmatization_dict)

with open('generated_text.txt', 'w', encoding='utf-8') as file:
    file.write(generated_text)