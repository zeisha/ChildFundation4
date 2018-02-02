from django import forms
from .models import ContactMessage
from karbar.models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'title', 'text', ]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "نام و نام خانوادگی"
        self.fields['email'].label = "پست الکترونیکی"
        self.fields['title'].label = "عنوان"
        self.fields['text'].label = "متن"
        self.fields['name'].widget.attrs[
            'style'] = 'width:400px; height:20px; border-radius=5px; direction:rtl; float:left;'
        self.fields['email'].widget.attrs['style'] = 'width:400px; height:20px; border-radius=5px; float:left;'
        self.fields['title'].widget.attrs[
            'style'] = 'width:400px; height:20px; border-radius=5px; direction:rtl; float:left;'
        self.fields['text'].widget.attrs[
            'style'] = 'width:400px; height20px; border-radius=5px; direction:rtl; float:left;'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text',]

