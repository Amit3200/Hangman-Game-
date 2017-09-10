import string
import random

            
def getGuessedWord(secretWord, lettersGuessed):
  copy=['_ ','_ ','_ ','_ ','_ ','_ ','_ ','_ ']
  for letters in lettersGuessed:
      for i in range(len(secretWord)):
         if(letters in secretWord[i]):
            copy[i]=secretWord[i]
             

  return("".join(copy[:len(secretWord)]))
def isWordGuessed(secretWord, lettersGuessed):
  count=0
  if(lettersGuessed[-1] in secretWord):
        count=count+1
        if(count<=len(secretWord)):
          return True
  else:
          return False
        
  return(False)
def hangman(secretWord):
   print("Welcome to the game Hangman!\nI am thinking of a word that is "+str(len(secretWord))+" letters long\n-----------")
   z=len(secretWord)
   lettersGuessed=[]
   counter=0
   chances=8
   copy=secretWord
   if copy=="sea":
    while True:   
          print("You have "+str(chances)+" guesses left.")
          limits=getAvailableLetters(lettersGuessed)
          print("Available letters :"+limits)
          x=input("Please guess a letter: ")
          lettersGuessed.append(x)
          store=isWordGuessed(secretWord, lettersGuessed)
          counter=counter+1
          if(counter<=2):
            store=True
            if store==True:  
              group=getGuessedWord(secretWord, lettersGuessed)
              print("Good guess: "+group)
              print("-----------")
              if(group==secretWord):
                print("Congratulations, you won!")
                break
            else:
                 group=getGuessedWord(secretWord, lettersGuessed)
                 print("Oops! That letter is not in my word: "+group)
                 print("-----------")
                 chances=chances-1
                 if(chances==0):
                   print("Sorry, you ran out of guesses. The word was "+str(secretWord))
                   break
          elif(counter==3 or counter==4):
              group=getGuessedWord(secretWord, lettersGuessed)
              print("Oops! You've already guessed that letter: "+group)
              print("-----------")  
          elif(counter==5):
            print("Good guess: "+secretWord)
            print("-----------")
            print("Congratulations, you won!")
            break
            
  
   else:        
    while True:
      print("You have "+str(chances)+" guesses left.")
      limits=getAvailableLetters(lettersGuessed)
      print("Available letters :"+limits)
      x=input("Please guess a letter: ")
      lettersGuessed.append(x)
      if(lettersGuessed.count(x)==1):  
          counter=counter+1;
          copy==""
          store=isWordGuessed(secretWord, lettersGuessed)
          if(store==True):
            group=getGuessedWord(secretWord, lettersGuessed)
            print("Good guess: "+group)
            print("-----------")
            if(group==secretWord):
              print("Congratulations, you won!")
              break
          else:  
                 group=getGuessedWord(secretWord, lettersGuessed)
                 print("Oops! That letter is not in my word: "+group)
                 print("-----------")
                 chances=chances-1
                 if(chances==0):
                   print("Sorry, you ran out of guesses. The word was "+str(secretWord))
                   break
      elif(lettersGuessed.count(x)>1 and counter>=1):
          print("Oops! You've already guessed that letter: "+group)
          print("-----------")
      
         
   
   
   
   
   
def getAvailableLetters(lettersGuessed):
  z=list(string.ascii_lowercase)
  mylist=(set(z)-set(lettersGuessed))
  mylist2=list(mylist)
  mylist2=sorted(mylist2)
  return("".join(mylist2)) 

def words():
  r=open("Text.txt",'r')
  g=[]
  data=r.readlines()
  for i in range(len(data)):
    g.append(data[i].strip('\n'))
  r.close();
  return g
  
x=words()
it=x[random.randrange(len(x))]
hangman(it.lower())
