from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        top5_categories = [
            Article.objects.filter(category__name='Jahon')[:6],
            Article.objects.filter(category__name='Iqtisodiyot')[:6],
            Article.objects.filter(category__name='Jamiyat')[:6],
            Article.objects.filter(category__name='Sport')[:6],
            Article.objects.filter(category__name='Fan-texnika')[:6],
        ]

        context = {
            "latest_news20": Article.objects.filter(published=True).order_by('-created_at')[:20],
            "top4_articles": Article.objects.filter(published=True).order_by('-views')[:4],
            "top9_articles": Article.objects.filter(published=True).order_by('-views')[:9],
            "top5_categories": top5_categories,
            'top5_category_names': ['Jahon', 'Iqtisodiyot', 'Jamiyat', 'Sport', 'Fan-texnika', ]
        }
        return render(request, 'index.html', context)

    def post(self, request):
        email = request.POST.get('email')
        if email is not None:
            NewsLetter.objects.create(email=email)
        return redirect('home')


class DetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        likes = Article.objects.filter(category=article.category).filter(published=True).order_by('-created_at')[:2]
        context = {
            'article': article,
            'likes': likes,
        }
        return render(request, 'detail-page.html', context)
