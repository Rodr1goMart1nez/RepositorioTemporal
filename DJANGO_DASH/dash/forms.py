from django import forms
from .models import WalleBpm

IMPACTO_CHOICES = [
    ('ALTO', 'ALTO'),
    ('MEDIO', 'MEDIO'),
    ('BAJO', 'BAJO'),
]

BLOQUEO_CHOICES = [
    ('SI', 'SI'),
    ('NO', 'NO'),
]

BLOQUEO_OTRO_CHOICES = [
    ('NINGUNO', 'NINGUNO'),
    ('OTRO', 'OTRO'),
]

STATUS_CHOICES = [
    (1.0, '1 - Nuevo'),
    (2.0, '2 - En Proceso'),
    (3.0, '3 - Pendiente'),
    (4.0, '4 - Resuelto'),
    (5.0, '5 - Cerrado'),
]

PRIORITY_CHOICES = [
    (1.0, '1 - Baja'),
    (2.0, '2 - Media'),
    (3.0, '3 - Alta'),
    (4.0, '4 - Crítica'),
]

class WalleBpmForm(forms.ModelForm):
    class Meta:
        model = WalleBpm
        fields = [
            'process_id', 'nombre', 'impacto', 'comentario', 'status_id', 'priority_id',
            'operacion', 'op_desc', 'gerente', 'ingresante', 'agencia',
            'bloqueo_canal', 'bloqueo_tc_td', 'bloqueo_fondo', 'bloqueo_otro'
        ]
        widgets = {
            'process_id': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'ID del Proceso'}),
            'comentario': forms.Textarea(attrs={'rows': 4, 'class': 'form-input'}),
            'nombre': forms.TextInput(attrs={'class': 'form-input'}),
            'impacto': forms.Select(choices=IMPACTO_CHOICES, attrs={'class': 'form-input'}),
            'status_id': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'form-input'}),
            'priority_id': forms.Select(choices=PRIORITY_CHOICES, attrs={'class': 'form-input'}),
            'operacion': forms.TextInput(attrs={'class': 'form-input'}),
            'op_desc': forms.TextInput(attrs={'class': 'form-input'}),
            'gerente': forms.TextInput(attrs={'class': 'form-input'}),
            'ingresante': forms.TextInput(attrs={'class': 'form-input'}),
            'agencia': forms.TextInput(attrs={'class': 'form-input'}),
            'bloqueo_canal': forms.Select(choices=BLOQUEO_CHOICES, attrs={'class': 'form-input'}),
            'bloqueo_tc_td': forms.Select(choices=BLOQUEO_CHOICES, attrs={'class': 'form-input'}),
            'bloqueo_fondo': forms.Select(choices=BLOQUEO_CHOICES, attrs={'class': 'form-input'}),
            'bloqueo_otro': forms.Select(choices=BLOQUEO_OTRO_CHOICES, attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['process_id'].disabled = True
            self.fields['process_id'].widget.attrs['class'] += ' bg-gray-100'
