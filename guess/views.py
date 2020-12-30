import random

from django.http import HttpResponse
from django.template import loader

from .models import Word

words_on_page = 3
correct_number = random.randint(1, words_on_page)
correct = 0

def regenerate(request):
    global correct_number
    global correct

    correct = 0
    correct_number = random.randint(1, words_on_page)

    return HttpResponse(True)

def answer(request):
    if request.POST.get('answer'):
        global correct

        if int(request.POST.get('answer')) == correct_number:
            correct = 1
        else:
            correct = 0

    return HttpResponse(correct)

def index(request):
    words = Word.objects.all()
    random_words = random.sample(list(words), words_on_page)
    correct_word = random_words[correct_number - 1]

    template = loader.get_template('game.html')
    context = { 'words': random_words, 'description': correct_word.description, 'answer': correct }
    return HttpResponse(template.render(context, request))