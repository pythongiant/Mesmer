from django.forms import forms
from django import forms


class SignUp(forms.Form):
    """ Sign Up """
    Name = forms.CharField(label="Your Name",widget=forms.TextInput(attrs={"placeholder":"It's Nice to meet you"}))
    username = forms.CharField(max_length =255,widget=forms.TextInput(attrs={"placeholder":"Make it Creative"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"We wont sell it. "}),label="Password")
    email = forms.EmailField(label="Email Id")
    DateOfBirth = forms.DateField(label="Date of Birth")
    
    Bio = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Tell us about yourself"}))
    profilePic = forms.FileField()
    
class PostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(PostForm, self).__init__(*args, **kwargs)
    """Post Form"""
    Post = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"What's going on? Mesmerise us.","rows":"1","cols":"50","autocomplete":"on"}))
    Pic = forms.FileField(required=False,label="📷 ")
class LoginForm(forms.Form):
    username = forms.CharField(max_length =255,widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(),label="Password")