from django.shortcuts import render
import re

def index(request):
    if request.method == 'POST':
        text = request.POST['text']
        
        # Замена ё на е и Ё на Е
        translation_table = str.maketrans("ёЁ", "еЕ")
        text = text.translate(translation_table)
        
        # Удаление всех кавычек
        text = text.replace("'", "").replace('"', "")
        
        # Замена всех слэшей (/) и обратных слэшей (\) на пробелы
        text = text.replace('/', ' ').replace('\\', ' ')
        
        # Функция для замены всех заглавных букв на строчные, если слово написано капсом
        def lower_case_if_caps(word):
            return word.lower() if word.isupper() else word

        # Функция для обработки одного предложения
        def process_sentence(sentence):
            words = sentence.split()
            processed_words = [lower_case_if_caps(word) for word in words]
            return ' '.join(processed_words)
        
        # Разбиваем текст на предложения
        sentences = re.split(r'(?<=\.)', text)

        # Обрабатываем каждое предложение и сохраняем заглавные буквы в начале предложений
        new_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            # Обрабатываем предложение
            processed_sentence = process_sentence(sentence)
            # Восстанавливаем заглавную букву в начале предложения
            if processed_sentence:  # Ensure the sentence is not empty
                processed_sentence = processed_sentence[0].upper() + processed_sentence[1:]
            new_sentences.append(processed_sentence)
        
        # Объединяем предложения обратно в текст
        new_text = ' '.join(new_sentences)

        return render(request, 'yo_app/index.html', {'new_text': new_text})
    else:
        return render(request, 'yo_app/index.html')
