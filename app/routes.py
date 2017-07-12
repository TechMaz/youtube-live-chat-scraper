import os
import json
from flask import Flask, render_template, Response
import scraper
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/scrape/<id>', methods=['GET'])
def scrape(id=None):
	if(id == None):
		return "<html>No id provided</html>"
	else:
		chats = scraper.run_scraper(id)
		return Response(json.dumps(chats), mimetype='application/json')
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)