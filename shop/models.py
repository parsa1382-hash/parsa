from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	code = models.IntegerField()

	def __str__(self):
		return self.user

STATUS = (
    (1, "قهوه های گانودرما"),
    (2, "ارایشی"),
    (3, "بهداشتی"),
    (4, "مواد غذایی"),
    (5, "شوینده بهداشتی"),
    (6, "منسوجات"),
    (7, "لوازم خانگی"),
    (8, "محصولات گشاورزی"),
   )

class Product(models.Model):
	name = models.CharField(max_length=500)
	image = models.ImageField()
	price = models.IntegerField()
	point = models.FloatField()
	review = models.TextField()
	usage = models.TextField()
	description = models.TextField()
	video = models.FileField()
	cid = models.IntegerField()
	inventory = models.BooleanField(default=True)

	category = models.IntegerField(choices=STATUS, default=1)

	def __str__(self):
		return self.name



class Bought(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bought')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)

class Buy(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.user

class Sell(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	phone = models.CharField(max_length=20)
	address = models.TextField()
	name = models.CharField(max_length=200)
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.name

