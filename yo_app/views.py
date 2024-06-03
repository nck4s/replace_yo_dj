from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        text = request.POST['text']
        new_text = text.replace('ё', 'е')
        return render(request, 'yo_app/index.html', {'new_text': new_text})
    else:
        return render(request, 'yo_app/index.html')
