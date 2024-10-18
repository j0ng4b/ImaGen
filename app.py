import os
import json
import requests

from dotenv import load_dotenv
from flask import Flask, render_template, request
from typing import cast


def create_app():
    app = Flask(__name__.split('.')[0])

    MONSTER_API_KEY = os.environ.get('MONSTER_API_KEY')

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def generate():
        prompt = request.form['prompt']
        url = "https://api.monsterapi.ai/v1/generate/txt2img"

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {MONSTER_API_KEY}"
        }

        payload = {
            "prompt": prompt,
            "safe_filter": False,
            "aspect_ratio": "square",
            "style": "realism",
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            error = json.loads(response.text)['message']
            return render_template('index.html', error=error)

        process_id = json.loads(response.text)['process_id']

        url = f"https://api.monsterapi.ai/v1/status/{process_id}"
        status = 'IN_PROGRESS'
        while status != 'COMPLETED':
            response = requests.get(url, headers=headers)
            status = json.loads(response.text)['status']

        image = json.loads(response.text)['result']['output'][0]
        return render_template('index.html', image=image, prompt=prompt)

    return app


def main():
    # Load environment variables from .env file
    load_dotenv('.env')

    SERVER_PORT = os.environ.get('SERVER_PORT', default=5000)

    app = create_app()
    app.run(port=cast(int, SERVER_PORT), debug=True)


if __name__ == '__main__':
    main()

