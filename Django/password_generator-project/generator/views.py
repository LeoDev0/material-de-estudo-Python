from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
  return render(request, 'generator/home.html')

def password(request):

  length = int(request.GET.get('length', 12))  # o 12 é o valor padrão da variável caso não tenha sido dado nenhuma valor pelo usuário

  characters = ''
  lower_characters = string.ascii_lowercase
  upper_characters = string.ascii_uppercase
  numbers = '0123456789'
  symbols = '!@#$%*()-'

  if request.GET.get('lowercase'):
    characters += lower_characters

  if request.GET.get('uppercase'):
    characters += upper_characters

  if request.GET.get('numbers'):
    characters += numbers

  if request.GET.get('symbols'):
    characters += symbols

  password = ''
  if characters:
    for i in range(length):
      password += random.choice(characters)
  else:
    password = 'You have to choose characters!'

  return render(request, 'generator/password.html', {'password': password})