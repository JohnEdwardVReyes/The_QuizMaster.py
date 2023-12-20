# Define SDG categories and their questions with multiple choices (A, B, C)
sdg_categories = {
    "Gender Equality": [
        "What does 'SDG 5' specifically address?\n(A) Poverty\n(B) Gender Equality\n(C) Education",
        "Which of the following is a key focus area of gender equality?\n(A) Environmental Sustainability\n(B) Equal pay and ending discrimination\n(C) Infrastructure development",
        "Which international organization primarily focuses on gender equality?\n(A) UNICEF\n(B) UN Women\n(C) WHO",
        "Which term refers to the belief that women and men should have equal rights and opportunities?\n(A) Gender Equality\n(B) Gender Parity\n(C) Gender Equity",
        "What is the percentage of women on average represented in national parliaments worldwide?\n(A) Around 10%\n(B) Around 25%\n(C) Around 50%"
    ],
    "Sustainable Energy": [
        "Which SDG aims to ensure access to affordable, reliable, sustainable, and modern energy for all?\n(A) SDG 5\n(B) SDG 7\n(C) SDG 9",
        "Which renewable energy source does not produce greenhouse gas emissions during energy production?\n(A) Wind energy\n(B) Solar energy\n(C) Biomass energy",
        "What does 'SDG 7' primarily focus on in terms of energy consumption?\n(A) Energy conservation\n(B) Energy efficiency\n(C) Energy equality",
        "Which country is the largest producer of wind energy?\n(A) United States\n(B) Germany\n(C) China",
        "Which technology allows buildings to generate their own energy from sunlight?\n(A) Wind turbines\n(B) Hydroelectric power\n(C) Solar panels"
    ],
    "Health": [
        "Which SDG aims to ensure healthy lives and promote well-being for all ages?\n(A) SDG 2\n(B) SDG 3\n(C) SDG 4",
        "Which disease is targeted by 'SDG 3' for elimination?\n(A) Tuberculosis\n(B) HIV/AIDS\n(C) Malaria",
        "What is the primary focus of 'SDG 3' in terms of maternal health?\n(A) Prenatal care\n(B) Reducing maternal mortality\n(C) Neonatal care",
        "Which organization leads global efforts to eradicate diseases like polio and malaria?\n(A) UNICEF\n(B) Red Cross\n(C) World Health Organization",
        "What is the meaning of 'WHO' in the context of global health?\n(A) World Health Organization\n(B) World Humanitarian Organization\n(C) World Hunger Organization"
    ]
}

# Define correct answers for each question
correct_answers = {
    "Gender Equality": ["B", "B", "B", "A", "B"],
    "Sustainable Energy": ["B", "B", "B", "C", "C"],
    "Health": ["B", "B", "B", "C", "A"]
}

def ask_questions(category, questions):
    print(f"\n{category}:")
    correct = 0
    for i, question in enumerate(questions):
        print(question)
        user_answer = input("Your answer (Enter A, B, or C): ").upper()
        if user_answer == correct_answers[category][i]:
            print("Correct!")
            correct += 1
        else:
            print("Incorrect! Would you like to try again? (Yes/No)")
            try_again = input().lower()
            if try_again != 'yes':
                return
    print(f"You answered {correct} out of {len(questions)} questions correctly in {category}.")

def start_quiz():
    print("Welcome to the Sustainable Development Goals (SDG) Quiz!")
    while True:
        print("\nChoose a category or enter 'exit' to end:")
        print("1. Gender Equality\n2. Su stainable Energy\n3. Health")
        choice = input("Enter your choice (1, 2, 3) or 'exit': ")
        if choice.lower() == 'exit':
            print("Thank you for participating!")
            break
        elif choice in ['1', '2', '3']:
            category_key = ""
            if choice == '1':
                category_key = "Gender Equality"
            elif choice == '2':
                category_key = "Sustainable Energy"
            else:
                category_key = "Health"
            
            if category_key in sdg_categories:
                ask_questions(category_key, sdg_categories[category_key])
            else:
                print("Invalid category choice. Please select again.")
        else:
            print("Invalid input. Please enter a valid option.")

# Start the quiz
start_quiz()