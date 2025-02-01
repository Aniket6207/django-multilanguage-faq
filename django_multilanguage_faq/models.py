from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from googletrans import Translator
from asgiref.sync import sync_to_async
import asyncio

class FAQ(models.Model):
    question = models.TextField(verbose_name=_("Question"))
    answer = RichTextField(verbose_name=_("Answer"))

    # Translated fields
    question_hi = models.TextField(null=True, blank=True, verbose_name=_("Question in Hindi"))
    question_bn = models.TextField(null=True, blank=True, verbose_name=_("Question in Bengali"))
    answer_hi = models.TextField(null=True, blank=True, verbose_name=_("Answer in Hindi"))
    answer_bn = models.TextField(null=True, blank=True, verbose_name=_("Answer in Bengali"))


    def get_translated_question(self, lang_code='en'):
        """
        Retrieves the translated question for the given language code.
        If lang_code is not valid, Retrieves default question in English
        """

        cache_key = f'faq_{self.id}_question_{lang_code}'
        translation = cache.get(cache_key)
        if translation is not None:
            return translation
        
        if lang_code == 'hi':
            translation = self.question_hi or self.question
        elif lang_code == 'bn':
            translation = self.question_bn or self.question
        else:
            translation = self.question

        cache.set(cache_key, translation, timeout=60 * 60 * 2) 
        return translation
    
    def get_translated_answer(self,lang_code='en'):
        """
        Retrieves the translated answer for the given language code.
        If lang_code is not valid, Retrieves default answer in English
        """
        cache_key = f'faq_{self.id}_answer_{lang_code}'
        translation = cache.get(cache_key)
        if translation is not None:
            return translation
        
        
        if lang_code == 'hi':
            translation = self.answer_hi or self.answer
        elif lang_code == 'bn':
            translation = self.answer_bn or self.answer
        else:
            translation = self.answer
        cache.set(cache_key, translation, timeout=60 * 60 * 2) 
        return translation


    def save(self, *args, **kwargs):
        """
        Automatically translate the question to Hindi and Bengali on save
        if translations are missing.
        """
        translator = Translator()
        async def translate_text():
            if not self.question_hi:
                translation_hi = await translator.translate(self.question, dest='hi')
                self.question_hi = translation_hi.text
            if not self.question_bn:
                translation_bn = await translator.translate(self.question, dest='bn')
                self.question_bn = translation_bn.text
            if not self.answer_bn:
                translation_hi = await translator.translate(self.answer, dest='hi')
                self.answer_hi = translation_hi.text
            if not self.answer_bn:
                translation_bn = await translator.translate(self.answer, dest='bn')
                self.answer_bn = translation_bn.text

        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(translate_text())
        # await asyncio.sleep(2.0)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
