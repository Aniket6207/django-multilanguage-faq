from django.db.models.signals import post_save,post_delete
from  django.dispatch import receiver
from .models import FAQ
from django.core.cache import cache

@receiver([post_save,post_delete],sender=FAQ)
def invalidate_faq_cache(sender,instance,**kwargs):
    """
    Invalidate FAQ list when New question is added or existing question is deleted.
    """
    cache.delete_pattern('*FAQ_list*')
    
