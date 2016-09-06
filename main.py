from flask import Flask, render_template, flash, redirect, jsonify, request
import urllib2
import json
import dotenv
import os
import sys


app=	Flask(__name__, static_url_path='')


@app.route('/', methods=["GET","POST"])
def homepage():
	return "Hello Earth!"


@app.route("/article-summary", methods=["GET"])
def getArticleSummary():
	nytAPIKey=	dotenv.get("NYT_API_KEY")
	url=		"https://api.nytimes.com/svc/topstories/v2/home.json?api-key="+nytAPIKey
	response=	urllib2.urlopen(url)
	data=		json.load(response)
	return jsonify({"results": data["results"]})


if __name__=='__main__':
	dotenv.load()
	app.run(debug=True)