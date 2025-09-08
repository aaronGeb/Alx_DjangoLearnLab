from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Author(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # Extending Book Model with Custom Permissions
    class Meta(models.Model):
        permissions = [
            ("can_add_book", "can add book"),
            ("can_change_book", "can change book"),
            ("can_delete_book", "can delete book"),
        ]
        permissions = models.CharField(max_length=50, choices="permissions")
        meta = models.TextField()

        def __str__(self):
            return f"{self.user.username} - {self.permissions}"


class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book)


class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    def __str__(self):
        return f"{self.user.username} - {self.role}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
