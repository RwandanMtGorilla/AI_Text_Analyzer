import json
import requests

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)

@app.route('/generate_txt', methods=['POST'])

def generate_txt():
    # Your OpenAI API Key
    data = request.get_json()
    NLprompt = data.get('prompt', 'hello!')
    api_key = "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"
    # The text prompt you want to generate a response
    promptGPT=f"i'm going to send you some text,which include the information of \"name\"\"gender\"\"birthday\",please return in json format.example:{{\"name\": \"张三\",\"gender\": \"male\",\"birthday\": \"20200306\"}},the birthday should be in num. if you didn't receive relevant information,fill Unknown. here is your prompt:\"{NLprompt}\""
        #f"  -Here is your input prompt:”{NLprompt}“"
    # The URL for OpenAI's API
    url = "https://api.openai.com/v1/chat/completions"
    # The headers for the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": promptGPT}],
        "max_tokens": 3300,
        "temperature": 0.5,
        "frequency_penalty": 0,
        "presence_penalty": 0}
    # Make the API request
    response = requests.post(url, headers=headers, json=data)
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the generated text from the response
        generated_text = response.json()['choices'][0]['message']['content']
        print(generated_text)
        return jsonify({"success": True, "txt": generated_text})

    else:

        # Handle the error
        print(f"Request failed with status code e{response.status_code}")
        return jsonify({"success": False, "error": f"Request failed with status code {response.status_code}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

