from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ

class FAQListView(APIView):
    @method_decorator(cache_page(60 * 2 ,key_prefix="FAQ_list"))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        data = [
            {
                'id': faq.id,
                'question': faq.get_translated_question(lang_code=lang),
                'answer': faq.get_translated_answer(lang_code=lang)
            } for faq in faqs
        ]
        return Response(data, status=status.HTTP_200_OK)