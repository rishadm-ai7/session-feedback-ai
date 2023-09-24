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

    for i, question_data in enumerate(quiz_data, start=1):
        st.subheader(f"Question {i}: {question_data['question']}")
        
        selected_option = st.selectbox("Choose an option:", [""] + question_data['options'], key=f"q{i}")
        
        if selected_option:
            selected_option_index = question_data['options'].index(selected_option)
            if selected_option_index == question_data['correct_option']:
                question_flags[i - 1] = True
            else:
                pass

    # for i, flag in enumerate(question_flags, start=1):
    #     st.write(f"Q{i}_flag: {flag}")

if __name__ == "__main__":
    main()
