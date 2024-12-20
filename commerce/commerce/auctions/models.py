from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE, ManyToManyField



class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category}"

class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', blank=True, related_name="follower")


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    starting_bid = models.IntegerField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=1)
    category = models.ForeignKey(Category, on_delete=CASCADE, default=1, related_name="inside_category")
    creator = models.ForeignKey('User', on_delete=CASCADE, default=1, related_name="creates")
    is_open = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.title}:  price: {self.starting_bid}"
    @property
    def bid_price(self):
        highest_bid = self.bids_for_listing.order_by('-bid_price').first()
        return highest_bid.bid_price if highest_bid else self.starting_bid

    def winner(self):
        highest_bid = self.bids_for_listing.order_by('-bid_price').first()
        return highest_bid.bidder if highest_bid else "No Winner"


class Bid(models.Model):
    listing = models.ForeignKey('Listing', on_delete=CASCADE, default=1, related_name="bids_for_listing")
    bid_price = models.IntegerField()
    bidder = models.ForeignKey('User', on_delete=CASCADE, default=1, related_name="my_bids")

    def __str__(self):
        return f"{self.listing}: {self.bid_price} by {self.bidder}"

class Comment(models.Model):
    commenter = models.ForeignKey('User', on_delete=CASCADE, default=1, related_name="comments_of_user")
    content = models.CharField(max_length=1000)
    listing = models.ForeignKey('Listing', on_delete=CASCADE, default=1, related_name="comments_of_listing")

