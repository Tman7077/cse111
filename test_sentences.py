from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import random
import pytest

def main():
     test_get_determiner()
     test_get_noun()
     test_get_verb()
     test_get_preposition()
     test_get_prepositional_phrase()
     test_get_adjective()

def test_get_determiner():
     # 1. Test the single determiners.

     global single_determiners
     single_determiners = ["a", "one", "the"]

     # This loop will repeat the statements inside it 4 times.
     # If a loop's counting variable is not used inside the
     # body of the loop, many programmers will use underscore
     # (_) as the variable name for the counting variable.
     for _ in range(4):

          # Call the get_determiner function which
          # should return a single determiner.
          word = get_determiner(1)

          # Verify that the word returned from get_determiner
          # is one of the words in the single_determiners list.
          assert word in single_determiners

     # 2. Test the plural determiners.

     global plural_determiners
     plural_determiners = ["two", "some", "many", "the"]

     # This loop will repeat the statements inside it 4 times.
     for _ in range(4):

          # Get a random number between 2 and 10 inclusive.
          quantity = random.randint(2, 11)

          # Call the get_determiner function which
          # should return a plural determiner.
          word = get_determiner(quantity)

          # Verify that the word returned from get_determiner
          # is one of the words in the plural_determiners list.
          assert word in plural_determiners

def test_get_noun():
     # 1. Test the single nouns.

     global single_nouns
     single_nouns = ["bird", "boy", "car", "cat", "child",\
               "dog", "girl", "man", "rabbit", "woman"]

     # This loop will repeat the statements inside it 4 times.
     for _ in range(4):

          # Call the get_noun function which
          # should return a single noun.
          word = get_noun(1)

          # Verify that the word returned from get_noun
          # is one of the words in the single_nouns list.
          assert word in single_nouns

     # 2. Test the plural nouns.

     global plural_nouns
     plural_nouns = ["birds", "boys", "cars", "cats", "children",\
               "dogs", "girls", "men", "rabbits", "women"]

     # This loop will repeat the statements inside it 4 times.
     for _ in range(4):

          # Get a random number between 2 and 10 inclusive.
          quantity = random.randint(2, 11)

          # Call the get_noun function which
          # should return a plural noun.
          word = get_noun(quantity)

          # Verify that the word returned from get_noun
          # is one of the words in the plural_nouns list.
          assert word in plural_nouns

def test_get_verb():
     past_verbs = ["drank", "ate", "grew", "laughed", "thought",\
               "ran", "slept", "talked", "walked", "wrote"]
     present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks",\
                    "runs", "sleeps", "talks", "walks", "writes"]
     present_plural_verbs = ["drink", "eat", "grow", "laugh", "think",\
                    "run", "sleep", "talk", "walk", "write"]
     future_verbs = ["will drink", "will eat", "will grow", "will laugh",\
               "will think", "will run", "will sleep", "will talk",\
               "will walk", "will write"]

     # Runs through a list of each tense, "past", "present", and "future".
     for tense in ["past, present, future"]:

          # This loop will repeat the statements inside it 4 times.
          for _ in range(4):

               # Call the get_verb function which
               # should return a singular verb,
               # based on the tense from the "for tense in..." loop.
               word = get_verb(1, tense)

               # Verify that the word returned from get_verb
               # is one of the words in the associated singular list.
               if tense == "past":
                    assert word in past_verbs
               elif tense == "present":
                    assert word in present_single_verbs
               else:
                    assert word in future_verbs

          # Get a random number between 2 and 10 inclusive.
          quantity = random.randint(2, 11)

          # This loop will repeat the statements inside it 4 times.
          for _ in range(4):

               # Call the get_verb function which
               # should return a plural verb,
               # based on the tense from the "for tense in..." loop.
               word = get_verb(quantity, tense)

               # Verify that the word returned from get_verb
               # is one of the words in the associated plural list.
               if tense == "past":
                    assert word in past_verbs
               elif tense == "present":
                    assert word in present_plural_verbs
               else:
                    assert word in future_verbs

def test_get_preposition():
     # 1. Test the prepositions.

     global prepositions
     prepositions = ["about", "above", "across", "after", "along",
          "around", "at", "before", "behind", "below",
          "beyond", "by", "despite", "except", "for",
          "from", "in", "into", "near", "of",
          "off", "on", "onto", "out", "over",
          "past", "to", "under", "with", "without"]

     # This loop will repeat the statements inside it 4 times.
     for _ in range(4):

          # Call the get_preposition function which
          # should return a preposition.
          word = get_preposition()

          # Verify that the word returned from get_preposition
          # is one of the words in the prepositions list.
          assert word in prepositions

def test_get_prepositional_phrase():
     # 1. Test the single prepositional phrases.

     # This loop will repeat the statements inside it 4 times.
     for _ in range(4):

          # Call the get_prepositional_phrase function which
          # should return three words: a preposition, a singular determiner,
          # and a singular noun, then split each word into its own variable.
          preposition, determiner, adjective, noun = get_prepositional_phrase(1).split()

          # Verify that each word returned from get_prepositional_phrase
          # is one of the words in its respective list.
          assert preposition in prepositions
          assert determiner in single_determiners
          assert adjective in adjectives
          assert noun in single_nouns

     # 2. Test the plural prepositional phrases.

     # This loop will repeat the statements inside it 4 times.
     for _ in range(4):

          # Call the get_prepositional_phrase function which
          # should return three words: a preposition, a plural determiner,
          # and a plural noun, then split each word into its own variable.
          preposition, determiner, adjective, noun = get_prepositional_phrase(2).split()

          # Verify that each word returned from get_prepositional_phrase
          # is one of the words in its respective list.
          assert preposition in prepositions
          assert determiner in plural_determiners
          assert adjective in adjectives
          assert noun in plural_nouns

def test_get_adjective():
     # 1. Test the adjectives.
     global adjectives
     adjectives = ["bad", "blue", "bored", "brave", "calm", "clean",
          "crazy", "cute", "dark", "evil", "fair", "funny",
          "good", "happy", "helpful", "kind", "lazy", "lucky",
          "nice", "odd", "quick", "shy", "silly", "tired",
          "ugly", "upset", "wicked"]

     # This loop will repeat the statements inside it 4 times.
     for _ in range(4):

          # Call the get_adjective function which
          # should return an adjective.
          adjective = get_adjective()

          # Verify that the word returned from get_adjective
          # is one of the words in the adjectives list.
          assert adjective in adjectives
     
pytest.main(["-v", "--tb=line", "-rN", __file__])