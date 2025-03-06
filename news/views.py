import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import NewsArticle
from django.shortcuts import render

# Endpoint to fetch and store news articles containing "Trump"
@require_http_methods(["GET"])
def store_news(request):
    url = "https://rssvercel.vercel.app/yle"
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch news"}, status=500)

    news_data = response.json()
    stored_count = 0

    for item in news_data:
        title = item.get("title", "")
        link = item.get("link", "")

        # Check if the title contains "Trump" and the article is not already stored
        if "Trump" in title and not NewsArticle.objects.filter(link=link).exists():
            NewsArticle.objects.create(title=title, link=link)
            stored_count += 1

    return JsonResponse({"message": f"Stored {stored_count} new articles"})

# Endpoint to read stored news articles
@require_http_methods(["GET"])
def read_news(request):
    articles = NewsArticle.objects.all()
    data = [{"title": article.title, "link": article.link} for article in articles]
    return JsonResponse(data, safe=False)

def index(request):
    return render(request, 'index.html')