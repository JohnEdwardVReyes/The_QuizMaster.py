# "The QuizMaster"

The system we provided here is coded based on the Python Programming Language. Aside from a bit of challenge or fun for yourself with all the questions, it serves as a structure code for when others want to twist and change its contents, more or less a skeleton to help people work with similar projects they have on mind.

With that said, we have inputs of our own within the questions which can explain the variety in the questions. Without further ado, let us get on with the details.


## Code Lines and their Respective Features


1.) **Lines 1-24**

![Line 1 - 24](https://github.com/JohnEdwardVReyes/JohnEdwardVReyes/assets/153410042/02b05286-55ca-488c-8edf-1a58a63d6413)

- The keys are strings representing different Sustainable Development Goals (SDGs). The values associated with each key are lists containing strings, where each string represents a multiple-choice question related to their respective SDG.

- Each SDG has a list of choices within the questions related to a specific goal while each question is a string that includess the question itself and three possible answers (A,B,C).

This part of our code demonstrates the use of dictionaries in Python to organize and structure information in a hierachical manner.

It also showcases the use of lists to store the multiple-choice questions related to different categories,

2.) **Lines 26 - 47** and **Lines 33 - 47**

![Lines 26 - 31](https://github.com/JohnEdwardVReyes/JohnEdwardVReyes/assets/153410042/c2bb2aa9-7540-4945-a9ca-5b3f4a7d8089)

*Correct Answers Dictionary*

This dictionary, named "correct_answers", associates each category (SDG) with a list of correct answers corresponding to the questions in that category.

![Lines 33 - 47](https://github.com/JohnEdwardVReyes/JohnEdwardVReyes/assets/153410042/04577d27-974d-4f56-9eb6-f1be95484bf6)

*Functions Definitions*

The "ask_questions function" takes two parameters: category (representing the SDG category). It iterates through each question in the category, prints the question, prompts the user for an answer, and checks if the answer is correct.

"If the user's answer is correct, it increments the correct counter."

Here it illustrates the use of functions in Python for modularizing code. The ask_question function encapsulates the logic for asking questions and evaluation answers, making the code more readable and maintainable. It demonstrates the integration of user input (input function) and the use of conditionals to check correctness and handle user interactions.

3.) **Lines 49 - 75**

![Lines 49 - 75](https://github.com/JohnEdwardVReyes/JohnEdwardVReyes/assets/153410042/1e4478af-9038-46bd-a9cc-00a2f641a023)

- The "start_quiz function" initiates the quiz by providing a welcome message. It runs a loop that prompts the user to choose a quiz category or exit.

- The user's choice is obtained using the input function. If the user chooses to exit, the function prints a thank-you message and break out of the loop.

- If the user enters a valid category choice (1,2,3), it maps the choice to the corresponding category key ("Gender Equality","Sustainable Energy", or "Health").

With regards to all that, the code demonstrates the use of a loop (while True) to keep the quiz running until the user chooses to exit. It also shows how to obtain user input and use conditionals to handle different cases.

The part here illustrates how functions can be used to organize code into modular and reusable components.

## Process and Inputs

**Categories**

![Category Choices](https://github.com/JohnEdwardVReyes/JohnEdwardVReyes/assets/153410042/f3db043d-adfe-44de-b850-9f53a40dc597)

As shown, you can pick between choice 1,2,3 or whether you want to exit (Note that it is case sensitive)


**Questions**

![Questions](https://github.com/JohnEdwardVReyes/JohnEdwardVReyes/assets/153410042/a021a1da-9d85-4b35-9613-3e8ec22832bb)

The input you provide affects the results, 1 of the choices is the correct answer while the rest is incorrect, simple enough.


A.) **Correct Answer**

![Correct Answer](https://github.com/JohnEdwardVReyes/JohnEdwardVReyes/assets/153410042/9f458884-b38a-4619-aa05-a31314d7ed79)

Upon entering the right answer, you will move on the next question, it will go on till you get the answer wrong or the questions ran out.


B.) **Wrong Answer**

![Wrong Answer](https://github.com/JohnEdwardVReyes/JohnEdwardVReyes/assets/153410042/0a7cdab5-3f46-4231-909b-eea6ba308f99)

When placing the wrong answer in, you have the option to try again or exit depending whether you input Yes or No.


**Exit**

![Exit](https://github.com/JohnEdwardVReyes/JohnEdwardVReyes/assets/153410042/8ab36f57-7ab3-4651-961b-bd21666e51d2)

The end of the program, it should pop up when you choose "No' when getting the wrong answer or pick "Exit" at the Category selection.


## Members Involved (UPDATED)

1.) **Edward Reyes** - 40%
- Created and managed the files to be submitted as well as presented the video demo for project.
  

2.) **James Natanauan** - 40 %
- Provided the source code for the project.
  

3.) **Kenneth Bagting** - 10 %
- Proof reader on the script for the video.
  

4.) **Joshua Braza** - 10 %
- Worked with debugging the raw source code provided by James.
  

## Link the Source Code and Demo

**For Google Drive:** https://drive.google.com/drive/folders/1a3pBQ75g37S1Fwh3KqL_Kh0Zs1Aamt16?usp=drive_link
