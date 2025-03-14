# Cybersecurity Quiz App

Welcome to the Cybersecurity Quiz App! This application is designed to test your knowledge of cybersecurity concepts through a series of questions. The app is built using Streamlit and features a sleek, animated interface.

## Features

- **Animated Interface**: The app includes various animations and styles to enhance the user experience.
- **Multiple Questions**: Choose the number of questions you want to answer (3, 5, 8, or 10).
- **Real-time Feedback**: Get immediate feedback on your answers with success and error messages.
- **Score Tracking**: Keep track of your score and see a summary of your answers at the end of the quiz.
- **Play Again**: Option to reset the game and play again.

## Installation

To run the Cybersecurity Quiz App, you need to have Python and Streamlit installed. Follow the steps below to set up the app:

1. **Clone the repository**:

2. **Running the App**:

To start the app, navigate to the project directory and run the following command:
```bash
streamlit run src/ramadan_pyhton_challenges/day_8/main.py
```

## Usage

1. **Select the Number of Questions**: On the start screen, choose the number of questions you want to answer.
2. **Answer Questions**: Read each question carefully and select the correct answer from the options provided.
3. **Submit Answers**: Click the "Submit Answer" button to check if your answer is correct.
4. **View Results**: At the end of the quiz, view your final score and a summary of your answers.
5. **Play Again**: Click the "Play Again" button to reset the game and start a new quiz.

## Customization

You can customize the questions by editing the `questions` list in the `main.py` file. Each question is a dictionary with the following keys:
- `question`: The question text.
- `options`: A list of answer options.
- `answer`: The correct answer.
- `level`: The difficulty level of the question (e.g., "Beginner", "Intermediate").
 