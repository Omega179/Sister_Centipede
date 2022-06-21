import praw
import os
from keep_alive import keep_alive

reddit = praw.Reddit(
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    username=os.environ['username'],
    password=os.environ['password'],
    user_agent="<SisterCentipede_1.0>"
)

footer = "\n***\n *I am a bot, and this action was performed automatically.* \n\n [Creator](https://www.reddit.com/user/ArcticFox19)|[Commands](https://www.reddit.com/user/Sister_Centipede/comments/vbxprn/commands_for_sister_centipede/)"

def clean_string(raw_string):
    cleaned_string = " " + raw_string
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace(">!", "")
    cleaned_string = cleaned_string.lower()
    return cleaned_string


class response:
    def __init__(self, filename):
        self.command = "!" + filename.replace(".txt", "")
        with open(filename) as response:
            self.text = response.read()
            
    def comment_reply(self, comment):
        if self.command in clean_string(comment.body) and comment.author.name != "Sister_Centipede":
            print(self.command)
            try:
                comment.reply(self.text + footer)
            except:
                pass       
        else:
            pass
                   

keep_alive()
subreddit = reddit.subreddit("OmegaTest")
commentstream = subreddit.stream.comments(skip_existing = True)

responselist = [response("sciadv.txt"), 
                response("prereqs.txt"),
                response("anime.txt"),
                response("spinoffs.txt"),  
                response("sgwatchorder.txt"),
                response("chaoshead.txt"),
                response("steinsgate0.txt"),
                response("steinsgate.txt"),
                response("roboticsnotesdash.txt"),
                response("roboticsnotes.txt"),
                response("chaoschild.txt"),
                response("occulticnine.txt"),
                response("anonymouscode.txt"),
                response("steins???.txt")                
               ]
     
while True:
    for comment in commentstream:
        for response in responselist:
            response.comment_reply(comment)
            if response.command in clean_string(comment.body) and comment.author.name != "Sister_Centipede":
                break
