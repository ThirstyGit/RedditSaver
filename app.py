# Imports
from flask import Flask, jsonify
from threading import Thread
from reddit import get_new_images
from subreddit_names import subreddit_names
import time

# Initializing objects.
app = Flask('')

# Necessary Variables.
subreddit_images = {}
for name in subreddit_names:
	subreddit_images[name] = set()


# Routes for my server.
# Basic home route.
@app.route('/')
def home():
	return "Hello. I am alive!"

# Get all the saved images link.
@app.route('/get')
def get():
	# json jsonify cannot have set. Convert all set to lists.
	json_value = {}
	for subreddit in subreddit_images:
		json_value[subreddit] = [url for url in subreddit_images[subreddit]]
	# Return all images.
	return jsonify(json_value)

# Necessary Threads.
# This thread runs the server.
def run():
	# This is for repl.it
  # app.run(host='0.0.0.0',port=8080)
	# This is for localhost.
	app.run(host='127.0.0.1', port=3000)

# This Thread stores all the new images in reddit.
def store_images():
	while True:
		# for all the subreddits.
		for name in subreddit_names:
			# get all the image urls.
			images = get_new_images(name, 100)
			for image in images:
				subreddit_images[name].add(image.url)
			time.sleep(5)

# Starting all the threads.
server_thread = Thread(target=run)
store_data_thread = Thread(target=store_images)
server_thread.start()
store_data_thread.start()
