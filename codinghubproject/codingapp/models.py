from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

# Create your models here.


# USER MODEL FOR SIGNING IN
class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
# USER PROFILE MODEL TO SHOW USER DETAILS
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    bio = models.TextField(blank=True, null=True)
    score = models.IntegerField(default=0)
    rank = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[
        ('Easy','Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ])

    tags = models.ManyToManyField('Tag', related_name='challenges', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class TestCase(models.Model):
    challenge = models.ForeignKey(Challenge, related_name='test_cases', on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f'Test case for {self.challenge.title}'
    
class Solution(models.Model):
    challenge = models.ForeignKey(Challenge, related_name='solutions', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return 'Solution by {self.author.username} for {self.challenge.title}'
    
class Comment(models.Model):
    solution = models.ForeignKey(Solution, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username}'
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.name


