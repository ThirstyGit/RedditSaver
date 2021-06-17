import praw

reddit = praw.Reddit(
	client_id='xhed9qTI5oo_zw',
	client_secret='bRhleSsCA5qX6QKBjqz8fmtT4pi4VQ',
	user_agent='<data_collector_bot>'
)



def get_new_images(subreddit_name, post_limit):
	return reddit.subreddit(subreddit_name).new(limit=post_limit)