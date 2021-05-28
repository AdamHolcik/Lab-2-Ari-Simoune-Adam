#Problem 1
binary = False # sets binary to false
while binary == False: # while binary is false it will keep asking the user to input a binary number
  a=input("My binary number is: ") #Ask for user to input a binary number
  length = a# a copy of a is made to stay as a script to allow the code to iterate through its length
  i=0 # i is set to zero
  b=0 # b is set to zero
  for i in range(len(length)): # loops for the length of the inputer number
    if length[i] == "1" or length[i] == "0": # if all the inputed digets are 1's and 0's it will contine with the code
      binary = True # binary is set to true to stop the loop
      a = int(a) # a is set to an integer so it can be calcualted
    else: # if the if statement was false this is run instead
      print("Number invalid, please try again :)") # tells the user that they did not input a binary number
      binary = False # binary is set to false is the inputed number is not a binary number
      break # stops the for loop if the input is not a binary number so the program does not try to convert it to binary
    while a!=0: # loops code while a is not equal to 0
      c = a%10 # c is equal to the remainder of a divided by 10
      c = c*(2**i) # c is equal to c times 2 to the power of if
      i += 1 # i increses by 1
      b += c # c is added to variable b
      a = a//10 # a becomes equal to the quotient of a divided by 10
  if binary == True: # if binary is true(the number is a binary number) do the next line of code
    print("The decimal equivalent is:",b) # prints out what the decimal equivalent of the inputed binary number is


#Problem 2
correct = False # sets correct to false
while correct == False: # while correct is false it will keep asking the user to input the sentance
  word = input('please enter a sentence with words seperated by a question mark(?): \n')# takes user input(the /n makes their input be entered on a new line(for aesthetics purposes))
  if word.find(' ') <0: # if the words are not seperated by spaces contine with the code
    correct = True # correct is set to true to stop the loop
    words = word.count('?')+1 # counts how many ?'s there are plus 1, this allows it to count the words
    word = word.replace('?', ' ') # replaces all the question marks into spaces
    print(word) # prints out the new sentence with the words seperated by question marks
    print('you wrote',words, 'word(s)') # prints out how many words were written
  else: # if the words were seperated by spaces
    print('please seperate your words with question marks') #asks the user to use the correct format to write the sentence



