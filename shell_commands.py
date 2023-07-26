from news.models import *

user1 = User.objects.create(username='Kris', first_name='Kristina')
Author.objects.create(authorUser=user1)
user2 = User.objects.create(username='Mary', first_name='Maria')
Author.objects.create(authorUser=user2)
Category.objects.create(name='IT')
Category.objects.create(name='Nature')
Category.objects.create(name='Politics')
Category.objects.create(name='Science')

Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Kris')), categoryType='AR', title='Lorum ipsum', text='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')

Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Mary')), categoryType='AR', title='Lorum ipsum Reloaded', text='Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.')

Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Kris')), categoryType='NW', title='Lorum ipsum Revolutions', text='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')

p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)

c1 = Category.objects.get(name='IT')
c2 = Category.objects.get(name='Nature')
c3 = Category.objects.get(name='Politics')
c4 = Category.objects.get(name='Science')

p1.postCategory.add(c1)
p2.postCategory.add(c2, c3)
p3.postCategory.add(c1, c4)

Comment.objects.create(commentUser=User.objects.get(username='Kris'), commentPost=Post.objects.get(pk=1), text='Nice!')
Comment.objects.create(commentUser=User.objects.get(username='Kris'), commentPost=Post.objects.get(pk=2), text='Boring...')
Comment.objects.create(commentUser=User.objects.get(username='Mary'), commentPost=Post.objects.get(pk=1), text='THNX!')
Comment.objects.create(commentUser=User.objects.get(username='Mary'), commentPost=Post.objects.get(pk=3), text='No comments')

Post.objects.get(pk=1).like()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=3).like()
Post.objects.get(pk=1).like()

Comment.objects.get(pk=1).like()
Comment.objects.get(pk=4).dislike()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=4).dislike()
Comment.objects.get(pk=3).like()

Author.objects.get(authorUser=User.objects.get(username='Kris')).update_rating()
Author.objects.get(authorUser=User.objects.get(username='Mary')).update_rating()

a = Author.objects.get(authorUser=User.objects.get(username='Kris'))
a.authorRating

Author.objects.get(authorUser=User.objects.get(username='Mary')).authorRating

bestAuthor = Author.objects.all().order_by('-authorRating').first()
print(bestAuthor.authorUser.username, bestAuthor.authorRating)

bestPost = Post.objects.all().order_by('-rating').first()

print(bestPost.creationDate, bestPost.author.authorUser.username, bestPost.rating, bestPost.title, bestPost.preview(), sep="\n")

bestComments = Comment.objects.all().filter(commentPost=bestPost)

for comment in bestComments: print(comment.dateCreation, comment.commentUser, comment.rating, comment.text)
