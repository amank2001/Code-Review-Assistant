from django.db import models

class CodeReview(models.Model):
    code = models.TextField()
    language = models.CharField(max_length=50)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.language} review on {self.created_at.strftime('%Y-%m-%d %H:%M')}"

