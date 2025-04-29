# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Configure the Gemini API
# if GOOGLE_API_KEY is None:
#     raise ValueError("Please set the GOOGLE_API_KEY environment variable.")
# genai.configure(api_key=GOOGLE_API_KEY)

# # Select the Gemini 1.5 Pro model
# model = genai.GenerativeModel('gemini-1.5-pro-latest')

# def chat_with_gemini(prompt):
#     """
#     Sends a prompt to the Gemini 1.5 Pro model and returns the response.

#     Args:
#         prompt (str): The user's input.

#     Returns:
#         str: The model's response.
#     """
#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"An error occurred: {e}"

# if __name__ == "__main__":
#     print("Welcome to the Gemini 1.5 Pro Chatbot!")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             print("Goodbye!")
#             break
#         response = chat_with_gemini(user_input)
#         print(f"Gemini: {response}")


from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Gemini API
if GOOGLE_API_KEY is None:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Initialize Flask app
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to interact with Gemini 1.5 Pro model.
    Expects JSON with a 'prompt' key.
    """
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Missing "prompt" in request'}), 400

    prompt = data['prompt']
    try:
        response = model.generate_content(prompt)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
