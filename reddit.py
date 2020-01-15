import praw
from secret import *
import random
def generate_text():
    print("Generating Text")
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, 
                        client_secret=REDDIT_CLIENT_SECRET, 
                        user_agent=REDDIT_APP_NAME, 
                        username=REDDIT_USERNAME,
                        password=REDDIT_PASSWORD)

    subreddit = reddit.subreddit('WritingPrompts')
    r = random.randint(3, 49)
    top_subreddit = subreddit.hot(limit = 50)
    submission = [i for i in top_subreddit][r]
    
    num = 1
    prompt = submission.title[5:]
    author = submission.author
    if author:
        print("author found")
        author = author.name
        print(author)
    else:
        author  = " a reddit user "
    comment_author = submission.comments[num].author
    if comment_author:
        comment_author = comment_author.name
    else:
        comment_author  = " a reddit user "
    story = submission.comments[num].body
    print(author)
    title = prompt[:20]
    text = "Hey Guys, This is the Writing Prompt Channel. Here, we take posts from reddit and read out loud the best stories with the help of a bot. Enjoy this amazing story.\n\n"
    print("Opening File")
    file = open("wp.txt", "w")
    text += "The Writing Prompt by user " + author + "\n" 
    text +=  prompt + "\n\n\n" 
    text += "Here is the amazing story made with the help of the prompt by user "+ comment_author + " \n\n\n"
    text += story +"\n\n THE END \n\n"
    text += "Thank you guys for checking out this channel. Please subscribe, like and share this video. See you in next one. Thank You and Good Bye."
    print("Writing File")
    file.write(text)
    file.close()
    print("Text generated")
    return {"text": text, "title":title}
