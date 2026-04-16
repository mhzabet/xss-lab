from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Stock
# Define the validator function (as above)
def validate_no_html_closing_tag(value):
    """
    Validator to disallow HTML tags (opening and closing) in a field.
    """
    # Regex to find any HTML-like tags
    if re.search(r'<[^>]+>', value):
        raise ValidationError('HTML tags are not allowed in this field.')

def validate_no_html_tags(value):
    """
    Validator to disallow HTML tags in a field.
    
    """
    if re.search(r"<|>|/>", value):
        raise ValidationError('HTML tags are not allowed in this field.')

class xss_no_protection_form(forms.Form):
    query = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ice cream...'})
    )


class xss_brackets_protection_form(forms.Form):
    query = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ice cream...'}),
        validators=[validate_no_html_closing_tag]
    )

class xss_attributes_no_protection_form(forms.Form):
    query = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ice cream...'}),
        validators=[validate_no_html_tags]
    )

class xss_javascript_context_no_protection_form(forms.Form):
    query = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ice cream...'})
    )


class xss_javascript_context_brackets_escape_form(forms.Form):
    query = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ice cream...'}),
        validators=[validate_no_html_tags]

    )
    
class stored_xss_no_protection_form(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['item', 'quantity']
