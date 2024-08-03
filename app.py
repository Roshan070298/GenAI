from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)




headers = {'Content-Type' : 'application/json',}
url = 'http://localhost:11434/api/generate'

history = []

def generate_response(model, prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": model,
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
        # print(actual_response)
    else:
        return response.text

@app.route('/genAI', methods=['POST'])
def handle_request():
    data = request.get_json()

    if not data or 'endpoint_name' not in data or 'prompt' not in data:
        return jsonify({'error': 'Invalid request. "endpoint_name" and "prompt" are required.'}), 400

    endpoint_name = data['endpoint_name']
    prompt = data['prompt']

    new = data.get('new', False)
    if new:
        global history
        history=[]
    response = generate_response(endpoint_name, prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
