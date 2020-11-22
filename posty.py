class Post:

    def __init__(self,id,name,date,pictur,content) :
        self.id= id
        self.name = name
        self.date= date
        self.pictur = pictur
        self.content = content


Post1 = Post(name="Yaser",date="21/11/2020 at 21:00",pictur="https//img",content="First interesting topic goes here ")
Post2 = Post(name="Mohamed",date="22/11/2020 at 22:00",pictur="https//img",content=" second interesting topic goes here")
Post3 = Post(name="Sara",date="23/11/2020 at 23:00",pictur="https//img",content="third interesting topic goes here ")

print(Post1.name,Post1.date,"\n",Post1.pictur,Post1.content)
print(Post2.name,Post2.date,"\n",Post2.pictur,Post2.content)
print(Post3.name,Post3.date,"\n",Post3.pictur,Post3.content)


