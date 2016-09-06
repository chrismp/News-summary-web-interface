# HOW TO USE
1. Make sure you have the following
	- Python 2.7 or higher
	- Python libraries (run `pip install` for those you don't have):
		- flask
		- urllib2
		- json
		- sys
		- os
		- dotenv
2. Make a file named `.env` in the same directory as `main.py`. In it, type `NYT_API_KEY="<YOUR_API_KEY_HERE>".
3. Open a terminal in the same directory as `main.py`, then run `python main.py`. 
4. Open a web browser, go to `http://127.0.0.1:5000/article-summary`.
5. You should see the NYT articles returned in JSON formats