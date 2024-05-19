import praw
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

def fetch_posts(keyword, limit=30):
    posts = []
    for submission in reddit.subreddit('all').search(keyword, limit=limit*2):
        if submission.selftext:
            post_data = {
                'title': submission.title,
                'url': submission.url,
                'body': submission.selftext,
            }
            posts.append(post_data)
            if len(posts) >= limit:
                break
    return posts

posts = fetch_posts('I did drug', limit=30)

with open('reddit_posts.txt', 'w', encoding='utf-8') as txtfile:
    for post in posts:
        txtfile.write(f"Title: {post['title']}\n")
        txtfile.write(f"URL: {post['url']}\n")
        if post['body']:
            txtfile.write(f"Body: {post['body']}\n")
        else:
            txtfile.write("Body: [This is a link post or the body is empty]\n")
        txtfile.write('--------------------------------------------------------------\n\n')