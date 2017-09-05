from django import forms

from django.contrib.admin.widgets import AdminDateWidget

from datetime import date
from django.forms import widgets, SelectDateWidget


from .models import Message


class MessageForm(forms.ModelForm):
	class Meta:
		model = Message

		fields = [
			"emisor_nn",
			"emisor",
			"receptor",
			"fecha_inicio",

		]








