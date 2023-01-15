from django.forms import ModelForm
from .models import auction

class AuctionForm (ModelForm):
    class Meta:
        model=auction
        exclude = ('Date',)