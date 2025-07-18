import openai
from django.shortcuts import render
from django.conf import settings
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def review_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        language = request.POST.get('language', 'python')
        prompt = f"Review the following {language} code and provide suggestions for improvement:\n\n{code}"     
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            store = True,
            messages=[
                {"role": "system", "content": "You are a helpful code reviewer."},
                {"role": "user", "content": prompt}
            ]
        )
        
        review = response.choices[0].message.content
        return render(request, 'reviewer/result.html', {'code': code, 'review': review})
    
    return render(request, 'reviewer/review.html')
