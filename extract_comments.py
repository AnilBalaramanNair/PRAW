import praw

# Fill in your Reddit app details
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="Comment Extractor by u/YOUR_USERNAME"
)

# Load the Reddit post
submission = reddit.submission(url="REDDIT_POST_URL")
submission.comments.replace_more(limit=None)

# Write comment ID, score, and body to file
with open("comments.txt", "w", encoding="utf-8") as f:
    for comment in submission.comments.list():
        username = f"u/{comment.author}" if comment.author else "u/[deleted]"
        f.write(f"Username: {username}\n")
        f.write(f"Upvotes: {comment.score}\n")
        f.write(comment.body.strip() + "\n\n")


print("✅ Comments with IDs and upvotes saved to comments.txt")
