from django.db.models.signals import post_save,post_delete
from  django.dispatch import receiver
from .models import FAQ
from django.core.cache import cache

@receiver([post_save,post_delete],sender=FAQ)
def invalidate_faq_cache(sender,instance,**kwargs):
    """
    Invalidate FAQ list when New question is added or existing question is deleted.
    """
    cache_keys = [
        f'faq_{instance.id}_question_en',
        f'faq_{instance.id}_answer_en',
        f'faq_{instance.id}_question_hi',
        f'faq_{instance.id}_answer_hi',
        f'faq_{instance.id}_question_bn',
        f'faq_{instance.id}_answer_bn',
    ]
    for key in cache_keys:
        cache.delete(key)
    cache.delete_pattern('*FAQ_list*')
    
