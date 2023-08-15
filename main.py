from flask import Flask, request
from urllib3.util.url import parse_url
from bs4 import BeautifulSoup
import re
import requests


ALLOWED_HOSTS = ["google.com", "checkmarx.com"]

app = Flask(__name__)

@app.route('/')
def proxy():
        
        url = request.args.get('url')

parsed_url = urlparse(url)

if parsed_url.scheme not in allowed_schemes:
    return "Invalid URL scheme"

if parsed_url.hostname not in allowed_hosts:
    return "Not allowed"

try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request success
except requests.exceptions.RequestException as e:
    return f"Error: {e}"

soup = BeautifulSoup(response.text, 'html.parser')
        
        to_change = soup.find_all(text = re.compile('o'))
        
        for element in to_change:
            fixed_text = element.replace('o', 'O')
            element.replace_with(fixed_text)
            
        return str(soup)

    

if __name__ == '__main__':
        app.run(port=8080)
