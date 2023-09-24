import streamlit as st

quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "London"],
        "correct_option": 0,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_option": 1,
    }
]

def main():
    st.title("Quiz App")

    question_flags = [False] * len(quiz_data)

    selected_options = [-1] * len(quiz_data)

    for i, question_data in enumerate(quiz_data, start=1):
        st.subheader(f"Question {i}: {question_data['question']}")

        selectbox_key = f"q{i}_selectbox"

        selected_option = st.selectbox("Choose an option:", [""] + question_data['options'], key=selectbox_key)

        if selected_option:
            selected_option_index = question_data['options'].index(selected_option)
            selected_options[i - 1] = selected_option_index

    if st.button("Submit"):
        for i, question_data in enumerate(quiz_data):
            if selected_options[i] == question_data['correct_option']:
                question_flags[i] = True

        st.write(f"Your quiz score is:{question_flags.count(True)}")
        

if __name__ == "__main__":
    main()
