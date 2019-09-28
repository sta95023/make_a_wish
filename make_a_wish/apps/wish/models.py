from django.db import models
import re

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['user_email']):    # test whether a field matches the pattern
            errors['user_email'] = ("Invalid email address!")
        return errors
        if len(postData['user_email']) < 15:
            errors['user_email'] = "Users email MUST be at least 15 characters long"
        if len(postData['user_password']) < 12:
            errors['user_password'] = "Users password MUST be at least 12 characters long"
        return errors

class Users (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

class WishesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['wish_thing']) < 5:
            errors['wish_thing'] = "Shows title should be at least 5 characters"
        if len(postData['wish_description']) < 5:
            errors['wish_description'] = "Shows description should be at least 5 characters"
        return errors

class Wishes (models.Model):
    thing = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    posted_by = models.ForeignKey(Users, related_name="wishs")
    granted_by = models.ForeignKey(Users, related_name="wishes_granted", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishesManager()