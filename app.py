import streamlit as st

st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Interview Preparation Assistant")

st.write("Practice interview questions and evaluate your performance.")

# Question Bank
questions = {
    "Data Scientist": [
        "What is Machine Learning?",
        "Explain Overfitting and Underfitting.",
        "What is the difference between supervised and unsupervised learning?",
        "What is cross-validation?",
        "Explain precision and recall."
    ],

    "Python Developer": [
        "What are Python decorators?",
        "Difference between list and tuple?",
        "What is OOP in Python?",
        "Explain exception handling.",
        "What are lambda functions?"
    ],

    "AI Engineer": [
        "What is Deep Learning?",
        "Explain Neural Networks.",
        "Difference between CNN and RNN?",
        "What is NLP?",
        "What is Transfer Learning?"
    ],

    "Web Developer": [
        "Difference between HTML, CSS and JavaScript?",
        "What is responsive design?",
        "What is API?",
        "Difference between GET and POST?",
        "What is React?"
    ]
}

role = st.selectbox(
    "Select Job Role",
    list(questions.keys())
)

st.subheader("Interview Questions")

answers = []

for i, question in enumerate(questions[role]):
    st.write(f"Q{i+1}. {question}")

    ans = st.text_area(
        f"Your Answer {i+1}",
        key=i
    )

    answers.append(ans)

# Evaluation Function
def evaluate(ans):
    if len(ans.split()) > 30:
        return 20

    elif len(ans.split()) > 15:
        return 15

    elif len(ans.split()) > 5:
        return 10

    else:
        return 5

if st.button("Evaluate Performance"):

    total = 0

    st.subheader("Results")

    for i, ans in enumerate(answers):

        score = evaluate(ans)

        total += score

        st.write(f"Question {i+1}: {score}/20")

        if score < 10:
            st.warning(
                "Try giving more detailed and technical answers."
            )

        elif score < 15:
            st.info(
                "Good answer. Add examples for improvement."
            )

        else:
            st.success(
                "Excellent answer!"
            )

    percentage = total

    st.subheader("Overall Performance")

    st.progress(percentage / 100)

    st.metric(
        "Interview Score",
        f"{percentage}%"
    )

    if percentage >= 80:
        st.success("Excellent Interview Readiness 🚀")

    elif percentage >= 60:
        st.info("Good Performance 👍")

    else:
        st.error("Needs More Practice 📚")
