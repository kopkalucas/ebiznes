from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM


model = OllamaLLM(model="llama3.1:8b")


app = Flask(__name__)


def generate_response(prompt):
    try:

        result = model.invoke(input=prompt)
        return result
    except Exception as e:

        return f"Error: {str(e)}", 500


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')

    if not user_input:
        return jsonify({"error": "No message provided"}), 400


    response_text = generate_response(user_input)


    return jsonify({"response": response_text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
