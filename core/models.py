from django.contrib.auth import get_user_model
from django.db import models
import chats.utils as chatsUtils
from chats.models import Chat

UserModel = get_user_model()


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    shortDescription = models.TextField(blank=True, null=True)
    content = models.TextField()
    cover = models.ImageField(upload_to='covers/')


class ProductPhoto(models.Model):
    image = models.ImageField(upload_to='products/')


class ProductTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    class ProductSex(models.TextChoices):
        male = 'Мужское'
        female = 'Женское'

    title = models.CharField(max_length=255)
    item = models.CharField(max_length=8)
    shortDescription = models.TextField(blank=True, null=True)
    description = models.TextField()
    price = models.FloatField()
    photos = models.ManyToManyField(ProductPhoto)

    sex = models.CharField(choices=ProductSex, max_length=20, null=True, blank=True)
    tags = models.ManyToManyField(ProductTag, blank=True, null=True)


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        created = "created", "Created"
        paid = "paid", "Paid"
        delivered = "delivered", "Delivered"
        cancelled = "cancelled", "Cancelled"
        delivering = "delivering", "Delivering"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now_add=True)
    delivered_date = models.DateTimeField(blank=True, null=True)

    status = models.CharField(choices=OrderStatus, max_length=20)

    products = models.JSONField(null=True, blank=True)

    totalPrice = models.FloatField(null=True, blank=True)


class SupportRequest(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255)
    description = models.TextField()
    isActive = models.BooleanField(default=True)
    chat = models.ForeignKey(Chat, on_delete=models.PROTECT, blank=True, null=True)

    def startChat(self):
        chat = chatsUtils.start_chat(byUser=self.user, toUser=UserModel.objects.get(mobilePhone='1234'),
                                     title=self.topic)
        chat.add_message(who=self.user, content=self.description)
        self.chat = chat
        self.save()
