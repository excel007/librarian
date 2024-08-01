import streamlit as st
import taskingai
from taskingai.assistant.message import Message

def main():
    st.title("Chat with Librarian assistant bot")
    st.caption("_Model ที่นำมาใช้งาน ได้แก่ openai/text-embedding-3-small-512 และ openai/gpt-3.5-turbo_")
    st.write("สอนไป A.I. ไป 2 เล่ม ได้แก่ ...")
    st.page_link("https://archive.org/details/zero-to-one-peter-thiel/The-Lean-Startup-/mode/2up", label="The Lean Startup โดย Eric Ries", icon="📕")
    st.page_link("https://archive.org/details/zero-to-one-peter-thiel/Zero%20to%20One%20-%20Peter%20Thiel/", label="Zero to One โดย Peter Thiel", icon="📔")
    st.caption(f'คุณสามารถพูดคุยเกี่ยวกับหนังสือทั้ง 2 เล่มได้ เช่น :blue["_สรุปหนังสือ Zero to one ให้ด้วย_"] :red["_หนังสือ The lean startup กับ Zero to one มีเนื้อหาอะไรที่สัมพันธ์กัน_"] :green["_Elon Musk ถูกพูดถึงว่าอย่างไร_"]')
    st.divider()
    # Define your model ID here
    taskingai.init(api_key=st.secrets["TASKINGAI_API_KEY"])
    assistant_id="X5lMR29D6xy5A2snTkYkkhq4"
    # chat_id="SdELmFo8IVol4wNGHJvWY1fh"
    chat_id="$$CHAT_ID$$"

    # Use Streamlit chat input to get user input
    prompt = st.chat_input("พิมพ์ข้อความที่นี่")


    if prompt:
               
        with st.chat_message("User"):
            st.write(prompt)
       
       # Perform assistant action 
        result = assistant_action(assistant_id, chat_id, prompt)

        # Display the chat completion result
        with st.chat_message("assistant"):            
            st.write("Librarian: ",f'{result.content.text}')


def assistant_action(assistant_id, chat_id, messages):
    user_message = taskingai.assistant.create_message(
        assistant_id,
        chat_id,
        text=messages,
    )

    assistant_message: Message = taskingai.assistant.generate_message(
        assistant_id,
        chat_id
    )
    return assistant_message

if __name__ == "__main__":
    main()
