from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        text = request.POST['text']
        translation_table = str.maketrans("ёЁ", "еЕ")
        new_text = text.translate(translation_table)
        return render(request, 'yo_app/index.html', {'new_text': new_text})
    else:
        return render(request, 'yo_app/index.html')

