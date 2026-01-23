from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    # どのモデルを使い、どの項目をフォームに出すかを指定します
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        
    # バリデーション（入力チェック）のカスタマイズ
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if '重要' in title and len(title) < 5:
            raise forms.ValidationError("「重要」という言葉を使う場合は、5文字以上で詳しく入力してください。")
        return title