from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

def chatbot_view(request):
    return render(request, 'chatbot/chat.html')

def process_user_input(user_input):
    # This function will process the user input and generate a bot response
    # For simplicity, let's just echo back the user input as the bot response
    return user_input

def chatbot_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        bot_response = process_user_input(user_input)
        return JsonResponse({'response': bot_response})
    else:
        return JsonResponse({'error': 'Invalid request'})

    