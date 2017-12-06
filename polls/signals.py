from django.db.models.signals import pre_delete
from django.dispatch import receiver
from polls.models import Wish

@receiver(pre_delete, sender=Wish)
def delete_wishlist(sender, instance, **kwargs):
    instance.delete()    

# pre_delete.connect(delete_wishlist, sender=Wish)
