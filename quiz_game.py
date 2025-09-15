questions = ("What is the name of the national bird of Bangladesh?: ",
             "Speed of light__:  ",
             "Who gives us foods?: ",
             "How many bones human body have?: ",
             "2+2 = ?: ",
             "What is the color of the national flag of Bangladesh?: ")

options = (("A.magpie-robin", "B.Crow", "C.Parrot", "D.Owl"),
           ("A.3x10^8 m/s", "B.3x10^9 m/s", "C.2x10^8 m/s", "D.3x10^10 m/s"),
           ("A.Angels", "B.Allah", "C.Father", "D.Farmers"),
           ("A.203", "B.179", "C.300", "D.206"),
           ("A.22", "B.BnP", "C.4", "D.33"),
           ("A.Black and White", "B.Green and Red", "C.Blue and Yello", "D.NONE"))

answers = ("A", "A", "B", "D", "C", "B")
guesses = []
score = 0 
question_num = 0 

for question in questions:
    print("________________________________________________________")
    print(question)

    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1 
        print("CORRECT")
    else:
        print("WRONG!")
    
    question_num += 1 

print("_______________________________")    
print("            RESULT             ")    
print("_______________________________")    

print("answers: ", end="" ) 
for answer in answers:
    print(answer, end=", ") 
print()    

print("guesses: ", end="" ) 
for guess in guesses:
    print(guess, end=", ") 
print()    
print()

print(f"You got {score}/6 ")

if score > 0.7:
    print(" 🙀 ")
else:
    print(" 🫣 ")