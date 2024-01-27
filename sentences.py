import random
def main():
     sentence_1 = get_determiner(1).capitalize() + " " + get_adjective() + " " + get_noun(1) + " " + \
          get_prepositional_phrase(1) + " " + get_verb(1, "past") + " " + get_prepositional_phrase(1) + "."
     sentence_2 = get_determiner(1).capitalize() + " " + get_adjective() + " " + get_noun(1) + " " + \
          get_prepositional_phrase(1) + " " + get_verb(1, "present") + " " + get_prepositional_phrase(1) + "."
     sentence_3 = get_determiner(1).capitalize() + " " + get_adjective() + " " + get_noun(1) + " " + \
          get_prepositional_phrase(1) + " " + get_verb(1, "future") + " " + get_prepositional_phrase(1) + "."
     sentence_4 = get_determiner(2).capitalize() + " " + get_adjective() + " " + get_noun(2) + " " + \
          get_prepositional_phrase(2) + " " + get_verb(2, "past") + " " + get_prepositional_phrase(2) + "."
     sentence_5 = get_determiner(2).capitalize() + " " + get_adjective() + " " + get_noun(2) + " " + \
          get_prepositional_phrase(2) + " " + get_verb(2, "present") + " " + get_prepositional_phrase(2) + "."
     sentence_6 = get_determiner(2).capitalize() + " " + get_adjective() + " " + get_noun(2) + " " + \
          get_prepositional_phrase(2) + " " + get_verb(2, "future") + " " + get_prepositional_phrase(2) + "."
     print(sentence_1, sentence_2, sentence_3, sentence_4, sentence_5, sentence_6)

def get_determiner(quantity):
     """Return a randomly chosen determiner. A determiner is
     a word like "the", "a", "one", "two", "some", "many".
     If quantity == 1, this function will return either "a",
     "one", or "the". Otherwise this function will return
     either "two", "some", "many", or "the".

     Parameter
          quantity: an integer.
               If quantity == 1, this function will return
               a determiner for a single noun. Otherwise this
               function will return a determiner for a plural noun.
     Return: a randomly chosen determiner.
     """
     if quantity == 1:
          words = ["a", "one", "the"]
     else:
          words = ["two", "some", "many", "the"]

     # Randomly choose and return a determiner.
     global determiner
     determiner = random.choice(words)
     return determiner

def get_noun(quantity):
     """Return a randomly chosen noun.
     If quantity == 1, this function will
     return one of these ten single nouns:
          "bird", "boy", "car", "cat", "child",
          "dog", "girl", "man", "rabbit", "woman"
     Otherwise, this function will return one of
     these ten plural nouns:
          "birds", "boys", "cars", "cats", "children",
          "dogs", "girls", "men", "rabbits", "women"

     Parameter
          quantity: an integer that determines if
               the returned noun is single or plural.
     Return: a randomly chosen noun.
     """
     if quantity == 1:
          words = ["bird", "boy", "car", "cat", "child",\
               "dog", "girl", "man", "rabbit", "woman"]
     else:
          words = ["birds", "boys", "cars", "cats", "children",\
               "dogs", "girls", "men", "rabbits", "women"]

     # Randomly choose and return a determiner.
     word = random.choice(words)
     return word

def get_verb(quantity, tense):
     """Return a randomly chosen verb. If tense is "past",
     this function will return one of these ten verbs:
          "drank", "ate", "grew", "laughed", "thought",
          "ran", "slept", "talked", "walked", "wrote"
     If tense is "present" and quantity is 1, this
     function will return one of these ten verbs:
          "drinks", "eats", "grows", "laughs", "thinks",
          "runs", "sleeps", "talks", "walks", "writes"
     If tense is "present" and quantity is NOT 1,
     this function will return one of these ten verbs:
          "drink", "eat", "grow", "laugh", "think",
          "run", "sleep", "talk", "walk", "write"
     If tense is "future", this function will return one of
     these ten verbs:
          "will drink", "will eat", "will grow", "will laugh",
          "will think", "will run", "will sleep", "will talk",
          "will walk", "will write"

     Parameters
          quantity: an integer that determines if the
               returned verb is single or plural.
          tense: a string that determines the verb conjugation,
               either "past", "present" or "future".
     Return: a randomly chosen verb.
     """
     if tense == "past":
          words = ["drank", "ate", "grew", "laughed", "thought",\
               "ran", "slept", "talked", "walked", "wrote"]
     elif tense == "present":
          if quantity == 1:
               words = ["drinks", "eats", "grows", "laughs", "thinks",\
                    "runs", "sleeps", "talks", "walks", "writes"]
          else:
               words = ["drink", "eat", "grow", "laugh", "think",\
                    "run", "sleep", "talk", "walk", "write"]
     else:
          words = ["will drink", "will eat", "will grow", "will laugh",\
               "will think", "will run", "will sleep", "will talk",\
               "will walk", "will write"]
               
     # Randomly choose and return a determiner.
     word = random.choice(words)
     return word

def get_preposition():
     """Return a randomly chosen preposition
     from this list of prepositions:
          "about", "above", "across", "after", "along",
          "around", "at", "before", "behind", "below",
          "beyond", "by", "despite", "except", "for",
          "from", "in", "into", "near", "of",
          "off", "on", "onto", "out", "over",
          "past", "to", "under", "with", "without"

     Return: a randomly chosen preposition.
     """
     words = ["about", "above", "across", "after", "along",
          "around", "at", "before", "behind", "below",
          "beyond", "by", "despite", "except", "for",
          "from", "in", "into", "near", "of",
          "off", "on", "onto", "out", "over",
          "past", "to", "under", "with", "without"]

     # Randomly choose and return a determiner.
     word = random.choice(words)
     return word

def get_prepositional_phrase(quantity):
     """Build and return a prepositional phrase composed of three
     words: a preposition, a determiner, and a noun by calling the
     get_preposition, get_determiner, and get_noun functions.

     Parameter
          quantity: an integer that determines if the determiner
               and noun in the prepositional phrase returned from
               this function are single or pluaral.
     Return: a prepositional phrase.
     """
     prep = get_preposition()
     det = get_determiner(quantity)
     adj = get_adjective()
     noun = get_noun(quantity)

     return f'{prep} {det} {adj} {noun}'

def get_adjective():
     """Return a randomly chosen adjective
     from this list of adjectives:
          "bad", "blue", "bored", "brave", "calm", "clean",
          "crazy", "cute", "dark", "evil", "fair", "funny",
          "good", "happy", "helpful", "kind", "lazy", "lucky",
          "nice", "odd", "quick", "shy", "silly", "tired",
          "ugly", "upset", "wicked"

     Return: a randomly chosen adjective.
     """
     words = ["bad", "blue", "bored", "brave", "calm", "clean",
          "crazy", "cute", "dark", "evil", "fair", "funny",
          "good", "happy", "helpful", "kind", "lazy", "lucky",
          "nice", "odd", "quick", "shy", "silly", "tired",
          "ugly", "upset", "wicked"]
     
     # if the determiner is "a", remove the adjectives starting with vowels from the list,
     # preventing something like "a ugly cat" (instead of "an ugly cat").
     if determiner == "a":
          words = ["bad", "blue", "bored", "brave", "calm", "clean",
          "crazy", "cute", "dark", "fair", "funny", "good",
          "happy", "helpful", "kind", "lazy", "lucky", "nice",
          "quick", "shy", "silly", "tired", "wicked"]

     # Randomly choose and return an adjective.
     word = random.choice(words)
     return word

if __name__ == "__main__":
     main()