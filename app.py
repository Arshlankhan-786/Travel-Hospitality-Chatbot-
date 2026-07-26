import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(
    page_title="Travel & Hospitality Chatbot",
    page_icon="✈️"
)

st.title("🌍 Travel & Hospitality AI Chatbot ✈️")

st.write("This is an AI Travel & Hospitality Chatbot.")
st.write("Ask anything related to travel, hotels, tourism, restaurants, visas, or trip planning.")

question = st.text_area(
    "Enter your travel related question"
)

if st.button("Ask AI"):

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert Travel and Hospitality Assistant.

Your job is to answer ONLY Travel and Hospitality related questions.

Topics include:
- Travel planning
- Trip itineraries
- Tourist attractions
- Hotel booking guidance
- Restaurant recommendations
- Budget travel planning
- Packing tips
- Adventure tourism
- Visa information (general guidance only)
- Transportation
- Flights and trains
- Local culture and customs
- Weather suggestions for travel
- Travel safety
- Family trips
- Honeymoon planning
- Solo travel
- Business travel
- Holiday planning

If the user asks anything outside the Travel and Hospitality domain, reply:

"Sorry, I only answer Travel and Hospitality related questions."

Question:
{question}

Provide your answer in the following format:

1. Simple Explanation

2. Step-by-Step Guidance

3. Best Recommendations

4. Travel Tips

5. Safety Precautions (if needed)

6. Budget Tips (if applicable)

Keep the answer simple, clear, and beginner-friendly.
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question
        }
    )

    st.subheader("Answer")

    st.write(response.content)