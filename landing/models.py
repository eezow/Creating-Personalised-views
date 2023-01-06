from django.db import models
import uuid

###########
# SCHEMAS #
###########


class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(null=False, blank=False, max_length=30)
    first_name = models.CharField(null=False, blank=False, max_length=30)
    last_name = models.CharField(null=False, blank=False, max_length=30)
    email = models.EmailField(null=False, blank=False, max_length=30)
    address = models.JSONField(null=False, blank=False, default=dict)
    membership = models.CharField(null=False, blank=False, max_length=3)
    date_joined = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    

class AppUsage(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usage_type = models.CharField(null=False, blank=False, max_length=3)
    session_start = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    session_end = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    clicks = models.IntegerField(default=0, null=False, blank=False)
    pages_visited = models.IntegerField(default=0, null=False, blank=False)
    device = models.JSONField(null=True, blank=True, default=dict)


class Transactions(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(null=False, blank=False, max_length=3)
    amount = models.FloatField(default=0.0, null=False, blank=False)
    status = models.CharField(null=False, blank=False, max_length=3)
