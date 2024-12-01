# BlogGenAI ✍️  
**An AI-powered blog generation tool using Streamlit and Llama 2**

BlogGenAI is an interactive web app designed to help you create high-quality blog content effortlessly. Powered by the Llama 2 model via Hugging Face, it enables you to craft blogs tailored for different audiences like researchers, data scientists, or the general public.

---

## 🚀 Features  
- **Customizable Content**: Specify the topic, audience type, and word count for your blog.  
- **AI-Powered Writing**: Leverages the Llama 2 model for high-quality, coherent blog generation.  
- **Interactive UI**: Built with Streamlit for a seamless user experience.  
- **Flexible Output**: Suitable for researchers, professionals, and common readers.  

---

## 📂 Project Structure  

BlogGenAI/
│
├── app.py                # Main Streamlit app file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── HuggingFaceAPI.py     # Contains the Hugging Face API key
└── .gitignore            # Files and directories to ignore in Git

## Prerequisites
Python 3.8 or higher
A Hugging Face API token

## Clone the Repository:


## Install Dependencies:
-- pip install -r requirements.txt

## Set Up the Hugging Face API Key:
Create a file named HuggingFaceAPI.py with the following content:

access_key = "your_huggingface_api_key_here"

## Run the Streamlit App:

streamlit run mainBlog.py
