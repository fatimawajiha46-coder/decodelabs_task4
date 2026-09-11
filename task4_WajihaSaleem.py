# Project: The General Knowledge Quiz
# Goal: Ask 3 questions, keep a score counter (+1 per correct answer),
# and print the final score at the end.
# Key Skill: If-Else logic & Variables (Control Flow)

# --- Variable to keep track of the score ---
score = 0

print("Welcome to the General Knowledge Quiz!")
print("Answer each question. Let's begin.\n")

# --- Question 1 ---
answer1 = input("Q1: What is the capital of France? ")

if answer1.strip().lower() == "paris":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is Paris.\n")

# --- Question 2 ---
answer2 = input("Q2: What is 5 + 7? ")

if answer2.strip() == "12":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is 12.\n")

# --- Question 3 ---
answer3 = input("Q3: Which planet is known as the Red Planet? ")

if answer3.strip().lower() == "mars":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is Mars.\n")

# --- Print the final score ---
print("Quiz finished!")
print("Your final score is:", score, "out of 3")
