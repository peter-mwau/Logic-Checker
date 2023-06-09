from django.shortcuts import render
from . models import Records_log
from . forms import LogiChecker
from gradio_client import Client
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

@csrf_exempt
def check(request):
    # if request.method == 'POST':
        form = LogiChecker(request.POST)
        if form.is_valid():
            userInput = form.cleaned_data.get("userInput")
            # output = form.cleaned_data.get("output")
            client = Client("https://jvictoria-logicchecker.hf.space/")
            result = client.predict(
				userInput,	# str representing input in 'ここに訂正してほしい英語の作文を置いてください。そして「Submit」を押してください:' Textbox component
				api_name="/predict"
                )
            # print(result)
            formoutput = LogiChecker(initial={'output': result, 'userInput': userInput})
            r = Records_log(Prompt=userInput, Response=result)
            r.save()
            return render(request, 'home.html', {'form': formoutput})
        else:
            return render(request, 'home.html', {'form': formoutput})
    # return render(request, 'home.html', {'form':formoutput})

