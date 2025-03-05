from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Karnataka', 'Karnataka'),
		('Maharashtra', 'Maharashtra'),
		('Goa', 'Goa '),
	)

	DISCRICT_CHOICES = (
		('shivamogga', 'shivamogga'),
		('mysore', 'Mysore'),
		('Bengaluru', 'Bengaluru'), 
		('Panaji', 'Panaji'),
		('Mumbai', 'Mumbai'),
	)

	PAYMENT_METHOD_CHOICES = (
		('gpay', 'Gpay'),
		('PhonePe','PhonePe'),
		('cashon delivery','Cash on Delivery')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
