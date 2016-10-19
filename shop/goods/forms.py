from django import forms


class Feedback(forms.Form):
    email = forms.EmailField(label="E-mail")
    name = forms.CharField(label="Имя")
    text = forms.CharField(label="Отзыв", widget=forms.Textarea)