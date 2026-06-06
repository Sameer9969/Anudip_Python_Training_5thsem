"""Correct answers: 
correct = ['A', 'C', 'B', 'D', 'A'] 
Student answers: 
student = ['A', 'B', 'B', 'D', 'C'] 
Write a program to: 
• Calculate score.  
• Display incorrectly answered question numbers.  
• Count correct and wrong answers.  
• Determine pass/fail (minimum 60%). """

correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

correct_count = 0
wrong_count = 0

print("Wrong Question Numbers:")

for i in range(len(correct)):

    if correct[i] == student[i]:
        correct_count += 1

    else:
        wrong_count += 1
        print(i + 1)

print("\nCorrect Answers:", correct_count)
print("Wrong Answers:", wrong_count)

# Score
score = correct_count
print("Score:", score)

# Percentage
percentage = (correct_count / len(correct)) * 100

print("Percentage:", percentage)

# Pass / Fail
if percentage >= 60:
    print("Pass")
else:
    print("Fail")