from django.db import models


class Newsletter(models.Model):
    email_address = models.EmailField(max_length=254)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email_address
