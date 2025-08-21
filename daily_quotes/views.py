import random
from django.shortcuts import render

quotes = [
    "Believe in yourself and all that you are.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Dream it. Wish it. Do it.",
]

def home(request):
    quote = random.choice(quotes)  # pick random quote
    return render(request, "daily_quotes/home.html", {"quote": quote})

def about(request):
    return render(request, "daily_quotes/about.html")

def contact(request):
    return render(request, "daily_quotes/contact.html")
