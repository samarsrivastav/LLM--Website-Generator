from flask import Flask, request, jsonify
from flask_cors import CORS
from services.llm_chain import ask_llm
app= Flask(__name__)
CORS(allow_all=True)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question=data.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    return jsonify({"response":ask_llm(question)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)