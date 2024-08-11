# Quiz Game in Python

# Questions and Answers
questions = (
    "What is the capital of India?",
    "Who is the author of the Indian national anthem?",
    "What is the largest state in India by area?",
    "Who was the first Prime Minister of India?",
    "What is the chemical symbol for the element named after an Indian scientist?",
    "Who was the founder of the Indian National Congress?",
    "What is the smallest state in India by area?",
    "Who wrote the famous Indian novel 'The God of Small Things'?",
    "What is the highest mountain peak in India?",
    "Who was the first Indian to win the Nobel Prize in Physics?"
)

answers = (
    ("A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"),
    ("A. Rabindranath Tagore", "B. Bankim Chandra Chattopadhyay", "C. Sarojini Naidu", "D. Subramania Bharati"),
    ("A. Rajasthan", "B. Maharashtra", "C. Uttar Pradesh", "D. Madhya Pradesh"),
    ("A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Subhas Chandra Bose", "D. Sardar Vallabhbhai Patel"),
    ("A. Bm", "B. Cn", "C. Rf", "D. Bo"),
    ("A. Allan Octavian Hume", "B. Lala Lajpat Rai", "C. Bal Gangadhar Tilak", "D. Bipin Chandra Pal"),
    ("A. Goa", "B. Sikkim", "C. Nagaland", "D. Mizoram"),
    ("A. Arundhati Roy", "B. Salman Rushdie", "C. Vikram Seth", "D. Amitav Ghosh"),
    ("A. Mount Kanchenjunga", "B. Mount Kamet", "C. Mount Trisul", "D. Mount Shivling"),
    ("A. C.V. Raman", "B. S.N. Bose", "C. H.J. Bhabha", "D. M.N. Saha")
)

# Correct answers
correct_answers = ("A", "A", "A", "A", "B", "A", "A", "A", "A", "A")

# Initialize score
score = 0

# Game loop
for i in range(len(questions)):
    print(f"\nQuestion {i+1}: {questions[i]}")
    for answer in answers[i]:
        print(answer)
    user_answer = input("Enter your answer (A, B, C, D): ")
    if user_answer.upper() == correct_answers[i]:
        print("Correct!")
        score += 1
    else:
        print(f"Sorry, the correct answer was {correct_answers[i]}.")

# Display final score
print(f"\nGame over! Your final score is {score} out of {len(questions)}.")
input("Press Enter to close...")