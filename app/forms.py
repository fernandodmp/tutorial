from django import forms


class MessageForm(forms.Form):
    mensagem = forms.CharField(max_length=255)


from app.models import Usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'