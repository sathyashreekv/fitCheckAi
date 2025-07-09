import streamlit as st 
from PIL import Image 
import google.generativeai as genai 
import os
from dotenv import load_dotenv 

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("FitCheck AI- Your Fashion Expert")
uploaded_file=st.file_uploader("Upload your OOTD ",type=['jpg','png','jpeg'])
description=st.text_input("Optional:Add a short outfit description")
if uploaded_file:
    image=Image.open(uploaded_file).convert("RGB")
    st.image(image,caption="Uploaded Image",use_container_width=True)
    
    prompts=f"""
    You're a fashion stylist. Based on this image and the description:
    \"{description if description else 'No extra description provided'}\"
    - Rate the outfit out of 10
    - Suggest one improvement make 10 out of 10
    - 
    """
    with st.spinner("Analyzing..."):
        response=model.generate_content([prompts,image])
        feedback=response.text.strip()
    st.markdown("### AI feedback")
    st.write(feedback)
    




