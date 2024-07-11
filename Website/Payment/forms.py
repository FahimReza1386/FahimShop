from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['class'] = 'form-control text-center'
            item.field.widget.attrs['style'] = 'text-align: center;'
            item.field.widget.attrs['style'] = 'font-family: "Vazir";'

    Shipping_full_name = forms.CharField(label = 'نام کامل  :' , required=True )
    Shipping_email = forms.CharField(label = 'ایمیل  :' , required=True )
    Shipping_address1 = forms.CharField(label = 'ادرس اول :' , required=True )
    Shipping_address2 = forms.CharField(label = 'ادرس دوم :' , required=False )
    Shipping_city = forms.CharField(label = 'شهر :' , required=True )
    Shipping_country = forms.CharField(label = 'کشور :' , required=True )
    Shipping_state = forms.CharField(label = 'وضعیت :' , required=False )
    Shipping_zip_Code= forms.CharField(label = 'کدپستی :' , required=False )
    Shipping_phone_number = forms.CharField(label = 'شماره تماس :' , required=True )

    class Meta:
        model = ShippingAddress
        fields = ('Shipping_full_name' , 'Shipping_email' , 'Shipping_address1' , 'Shipping_address2' , 'Shipping_city' , 'Shipping_country' , 'Shipping_state' , 'Shipping_zip_Code' , 'Shipping_phone_number' )
        exclude = ['user' , ]