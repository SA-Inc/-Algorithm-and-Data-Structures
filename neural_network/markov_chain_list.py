import random
import string
from collections import defaultdict


def remove_punctuations(text):
  return text.translate(str.maketrans('\n', ' ', string.punctuation))


def learn_words(text):
  text = remove_punctuations(text)
  words = text.split(' ')
  markov_dict = defaultdict(list)

  end_word = ''

  for current_word, next_word in zip(words[0:-1], words[1:]):
    markov_dict[current_word].append(next_word)
    end_word = next_word

  markov_dict[end_word].append(None)
  markov_dict = dict(markov_dict)
  return markov_dict


def predict_words(chain, first_word, number_of_words = 5):
  if(first_word in list(chain.keys())):
    word1 = str(first_word)
    predictions = word1.capitalize()

    for i in range(number_of_words - 1):
      word2 = random.choice(chain[word1])

      if(word2 is None):
        continue

      word1 = word2
      predictions += ' ' + word2

    predictions += '.'
    return predictions
  else:
    return "Word not in corpus"


text = 'ты уехал на юг а здесь настали теплые дни нагревается мост ровно плещет вода пыль витает я теперь прохожу в переулке все в тени все в тени все в тени и вблизи надо мной твой пустой самолет пролетает'

d = learn_words(text)
print(predict_words(d, 'я', 1000))
