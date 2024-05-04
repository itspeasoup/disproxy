from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/api/webhooks/<path:path>', methods=['POST'])
def proxy_request(path):
    # Replace 'discord.com' with the base URL of your Discord webhook
    base_url = 'https://discord.com'
    proxy_url = f'{base_url}/api/webhooks/{path}'
    
    headers = {'Content-Type': 'application/json'}
    data = request.json
    
    try:
        response = requests.post(proxy_url, headers=headers, json=data)
        return Response(response.content, status=response.status_code, headers=dict(response.headers))
    except Exception as e:
        return Response(str(e), status=500)

if __name__ == '__main__':
    app.run(debug=True)
