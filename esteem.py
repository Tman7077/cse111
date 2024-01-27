def main():
     print('This is the Rosenberg self-esteem test.' + '\n' +
          '10 questions will follow, and you should answer with one of four options:' + '\n' +
          '"A" = Strongly Agree' + '\n' +
          '"a" = Agree' + '\n' +
          '"d" = Disagree' + '\n' +
          '"D" = Strongly Disagree.' + '\n' +
          'At the end of the test, a score between 1 and 30 will be reported.' + '\n' +
          'Someone with a score of 15 or below may have problematically low self-esteem.\n\n')
     questions  = [
          "I feel that I am a person of worth, at least on an equal plane with others. ",
          "I feel that I have a number of good qualities. ",
          "All in all, I am inclined to feel that I am a failure. ",
          "I am able to do things as well as most other people. ",
          "I feel I do not have much to be proud of. ",
          "I take a positive attitude toward myself. ",
          "On the whole, I am satisfied with myself. ",
          "I wish I could have more respect for myself. ",
          "I certainly feel useless at times. ",
          "At times I think I am no good at all. "]

     answers = []
     for i in range(10):
          answers.append(ask_q(questions[i]))
     
     answers = convert(answers)
     
     score = calc_score(answers)
     if score < 16:
          result = "You could have problematically low self-esteem."
     else:
          result = "You have pretty good self-esteem."
     print(f'\nYour score is {score}. {result}')


def ask_q(q):
     a = input(q)
     if a in ["a", "A", "d", "D"]:
          return a
     else:
          print(f'Please enter "a", "A", "d", or "D".\n')
          ask_q(q)

def pos_q(a):
     if a == "A":
          return 3
     elif a == "a":
          return 2
     elif a == "d":
          return 1
     else:
          return 0

def neg_q(a):
     if a == "A":
          return 0
     elif a == "a":
          return 1
     elif a == "d":
          return 2
     else:
          return 3

def convert(answers):
     new_answers = []

     for i in answers:
          if answers.index(i) in [0, 1, 3, 5, 6]:
               new_answers.append(pos_q(answers[answers.index(i)]))
               answers.remove(i)
          else:
               new_answers.append(neg_q(answers[answers.index(i)]))
               answers.remove(i)
               
     return new_answers

def calc_score(answers):
     s = 0
     for i in answers:
          s += answers[i]
     return s

if __name__ == "__main__":
     main()