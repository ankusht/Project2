from django import forms

class fb_url_live(forms.Form):
	url = forms.CharField()

class fb_url_nonlive(forms.Form):
	url = forms.CharField()

class yt_url(forms.Form):
	url = forms.CharField()	