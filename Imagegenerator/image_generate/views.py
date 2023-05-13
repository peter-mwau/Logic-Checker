from django.shortcuts import render
from . forms import LogiChecker
from gradio_client import Client
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

@csrf_exempt
def check(request):
    if request.method == 'POST':
        form = LogiChecker(request.POST)
        if form.is_valid():
            userInput = form.cleaned_data.get("userInput")
            response = requests.post("https://jvictoria-logicchecker.hf.space/", json={
            "data": [
                userInput,
            ]
            }).json()
            data = response["data"]
            return render(request, 'home.html', {'form': form})
        else:
            return render(request, 'home.html', {'form': form})
    return render(request, 'home.html')

