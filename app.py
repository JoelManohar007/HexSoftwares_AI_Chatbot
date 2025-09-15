import streamlit as st

st.title("HexSoftwares AI Chatbot by Joel Manohar")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return ("Hello! Welcome to HexSoftwares. As a software development intern, "
                "you have the opportunity to work on real-world projects using modern technologies. "
                "How may I assist you today?")
    elif "hexsoftwares" in user_input:
        return ("HexSoftwares is a leading software development company, committed to excellence and innovation. "
                "We offer internships in various domains including AI, web and app development, and cybersecurity. "
                "Our interns work in a dynamic environment where learning and growth are encouraged.")
    elif "internship" in user_input:
        return ("Our internship program is designed to give hands-on experience in cutting-edge tech projects. "
                "You will receive mentorship, work on live assignments like AI chatbots and fraud detection systems, "
                "and gain exposure to modern development workflows. Upon completion, interns receive a certificate, recommendation letter, and resume support.")
    elif "software developer" in user_input or "developer" in user_input:
        return ("As a software developer at HexSoftwares, you'll learn coding best practices, agile project management, and collaboration skills. "
                "Developers use languages like Python, JavaScript, and frameworks such as Django and React. "
                "You will participate in team stand-ups, review code, and contribute to projects that solve real business problems.")
    elif "project experience" in user_input or "real-world projects" in user_input:
        return ("Interns at HexSoftwares work on real-world applications—such as building AI chatbots, virtual assistants, and fraud detection tools. "
                "Projects follow industry standards: requirements analysis, design, coding, testing, deployment, and documentation. "
                "This experience prepares you for future roles in tech companies, startups, or freelance work.")
    elif "career guidance" in user_input or "google" in user_input or "future" in user_input:
        return (
            "Career guidance for software developers includes building a strong portfolio, mastering one or two programming languages deeply, and learning problem solving with algorithms and data structures. "
            "For a career at major tech companies like Google, focus on coding interviews, system design concepts, and contributing to open source projects. "
            "Internships and freelance work at HexSoftwares give you valuable experience that can help you stand out to top employers."
        )
    elif "more about ai chatbot" in user_input or "ai chatbot" in user_input:
        return (
            "An AI chatbot is a software application designed to simulate human conversation using natural language processing (NLP). "
            "At HexSoftwares, we build chatbots that answer user questions, automate customer support, and provide information in real time. "
            "Interns learn to design conversation flows, implement backend logic, and ensure security and privacy of user data."
        )
    elif "help" in user_input or "support" in user_input:
        return (
            "I am here to support you with queries about HexSoftwares, our internship program, software development roles, and project experience. "
            "You can ask specific questions about skills, technologies, application processes, or company culture to get detailed guidance."
        )
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have more questions or need advice about your tech career, feel free to ask."
    else:
        return ("Sorry, I am a demo chatbot and I do not understand that yet. "
                "Try asking about HexSoftwares, software developer roles, project experience, or type 'help' for more information.")

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    reply = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)
