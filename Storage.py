class meme:
    def __init__(self, user_id):
        self.user_id = user_id
        self.image = 0
        self.image_data = 0
        self.textup = ""
        self.textdown = ""
        self.i = 0
    
    def Printvalues(self):
        print (self.user_id, self.image, self.textup, self.textdown)


templates = {"1. deadskeleton":"deadskeleton.jpg","2. mjcry":"mjcry.jpg", 
             "3. mrbean":"mrbean.jpg", "4. politecat": "politecat.jpg", 
             "5. sadpepe": "sadpepe.jpg", "6. stonks": "stonks.png"}

memedict = {}
memeStorage = {}
defaultReply = "Use command '!make a meme' to make your own meme"
