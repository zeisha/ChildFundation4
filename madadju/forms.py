from madadju.models import Report
from django import forms


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "عنوان"
        self.fields['content'].label = "محتوا"
        self.fields['title'].widget.attrs['style'] = 'width:400px; height:20px; border-radius=5px; direction:rtl; float:left;'
        self.fields['content'].widget.attrs['style'] = 'width:400px; height20px; border-radius=5px; direction:rtl; float:left;'