import openai
from django.shortcuts import render
from django.conf import settings

openai_api_key = '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'
openai.api_key = openai_api_key

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
