import openai
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import CodeReview
import os
import markdown

def review_code(request):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
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
        
        CodeReview.objects.create(code=code, language=language, review=review)
        
        review_html = markdown.markdown(review, extensions=['fenced_code'])
        
        return render(request, 'reviewer/result.html', {'code': code, 'review': mark_safe(review_html)})
    
    return render(request, 'reviewer/review.html')

