import datetime
from abc import ABC, abstractmethod
from validators import String,DateTime



class User:
    name = String()
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.posts = []

    def create_post(self, post):
        self.posts.append(post)

    def view_post(self, post):
        print(f"{post.content}")

    def leave_comments(self, comment, post):
        post.comments.append(comment)

    def __repr__(self):
        return f'name is {self.name} contact info is {self.contact_info}'


class Post:
    date = DateTime()
    def __init__(self, user: User, content: str, date: datetime):
        self.user = user
        self.content = content
        self.date = date
        self.comments = []

    def __repr__(self):
        return f"user  {self.user} ,content is {self.content}, datetime is {self.date}"


class text(Post):
    pass


class image(Post):
    pass


class Comment:
    def __init__(self, user: User, post: Post, content: str):
        self.user = user
        self.post = post
        self.content = content

    def __repr__(self):
        return f" {self.user} post is {self.post} content is {self.content}"


class SocialMediaOperation:
    pass


class SocialMedia(SocialMediaOperation):
    pass


user = User("Alik", "+37498620852")
post1 = Post(user, "bnutyan het kapvac", datetime.datetime(2020, 5, 17))
post2 = Post(user, "bnutyan het kapvac", datetime.datetime.now())
user.create_post(post1)
user.create_post(post2)
for post in user.posts:
    print(post)

comment1 = Comment(user, post1, "shat lav nkara")
comment2 = Comment(user, post1, "shat lav nkaraaaaaaaa")

user.view_post(post1)

user.leave_comments(comment1, post2)
user.leave_comments(comment2, post2)

for comment in post1.comments:
    print(comment)
