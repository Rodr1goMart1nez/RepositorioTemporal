from django import forms
from .models import WalleBpm

# --- Choice Definitions ---

TIPO_CUENTA_CHOICES = [
    ('', '--- Seleccione Tipo de Cuenta ---'),
    ('Cuenta Corriente', 'Cuenta Corriente'),
    ('Tarjeta de Crédito', 'Tarjeta de Crédito'),
    ('Caja de Ahorro', 'Caja de Ahorro'),
]

MONEDA_CHOICES = [
    ('', '--- Seleccione Moneda ---'),
    ('Dólares', 'Dólares'),
    ('Euros', 'Euros'),
    ('Guaranies', 'Guaranies'),
]

MOTIVO_RECLAMO_CHOICES = [
    ('', '--- Seleccione Motivo ---'),
    ('ALTA TC/TD (NO SOLICITADO)', 'ALTA TC/TD (NO SOLICITADO)'),
    ('CONTRACARGO TC', 'CONTRACARGO TC'),
    ('CONTRACARGO TD', 'CONTRACARGO TD'),
    ('EMISION DE CHEQUES/CHEQUERAS', 'EMISION DE CHEQUES/CHEQUERAS'),
    ('EXTRACCIONES EN VENTANILLA', 'EXTRACCIONES EN VENTANILLA'),
    ('PHISHING POR EMAIL', 'PHISHING POR EMAIL'),
    ('PHISHING POR RRSS', 'PHISHING POR RRSS'),
    ('PHISHING POR SMS', 'PHISHING POR SMS'),
    ('PHISHING TELEFONICO', 'PHISHING TELEFONICO'),
    ('PHISHING POR MALWARE', 'PHISHING POR MALWARE'),
    ('SOLICITUDES APERTURA CAJA DE AHORRO O CTA CTE', 'SOLICITUDES APERTURA CAJA DE AHORRO O CTA CTE'),
    ('SOLICITUDES DE PRESTAMOS', 'SOLICITUDES DE PRESTAMOS'),
    ('TRANSACCIONES DESCONOCIDAS EN IHB', 'TRANSACCIONES DESCONOCIDAS EN IHB'),
    ('TRANSFERENCIAS DESCONOCIDAS SIPAP/SPI', 'TRANSFERENCIAS DESCONOCIDAS SIPAP/SPI'),
    ('TRANSFERENCIAS DESCONOCIDAS/ITAU', 'TRANSFERENCIAS DESCONOCIDAS/ITAU'),
]

RESUMEN_FRAUDE_CHOICES = [
    ('', '--- Seleccione Resumen ---'),
    ('Fraudes TD', 'Fraudes TD'),
    ('Fraudes TC', 'Fraudes TC'),
    ('Fraude documental Cheques', 'Fraude documental Cheques'),
    ('Fraude documental Cuentas', 'Fraude documental Cuentas'),
    ('Fraude documental Depositos', 'Fraude documental Depositos'),
    ('Fraude documental Extracciones', 'Fraude documental Extracciones'),
    ('Fraude documental Prestamos', 'Fraude documental Prestamos'),
    ('Fraude documental Formularios', 'Fraude documental Formularios'),
    ('Fraude Transferencias', 'Fraude Transferencias'),
    ('Fraude Interno', 'Fraude Interno'),
    ('PHISHING', 'PHISHING'),
    ('Fraude Amigable', 'Fraude Amigable'),
    ('Fraude Pago de Servicios', 'Fraude Pago de Servicios'),
    ('Fraude Robo de Identidad', 'Fraude Robo de Identidad'),
    ('Fraude Sim Swapping', 'Fraude Sim Swapping'),
]

CANAL_CHOICES = [
    ('', '--- Seleccione Canal ---'),
    ('DIGITAL', 'DIGITAL'),
    ('NO DIGITAL', 'NO DIGITAL'),
]

SUB_CANAL_CHOICES = [
    ('', '--- Seleccione Sub Canal ---'),
    ('Itaú Pagos', 'Itaú Pagos'),
    ('Gpay', 'Gpay'),
    ('Express', 'Express'),
    ('IHB', 'IHB'),
    ('CNB', 'CNB'),
    ('Agencias', 'Agencias'),
    ('Itaú Negocios', 'Itaú Negocios'),
    ('POS', 'POS'),
    ('Pago Móvil', 'Pago Móvil'),
    ('Multisesión', 'Multisesión'),
    ('ATM', 'ATM'),
    ('Apple Pay', 'Apple Pay'),
    ('SuperApp', 'SuperApp'),
]

TECNOLOGIA_USADA_CHOICES = [
    ('', '--- Seleccione Tecnología ---'),
    ('BANDA MAGNETICA', 'BANDA MAGNETICA'),
    ('CHIP', 'CHIP'),
    ('CONTACTLESS', 'CONTACTLESS'),
    ('ITOKEN', 'ITOKEN'),
    ('PIN DE ACCESO', 'PIN DE ACCESO'),
    ('PIN DE TD/TC', 'PIN DE TD/TC'),
    ('PIN DE TRANSACCION', 'PIN DE TRANSACCION'),
    ('QR', 'QR'),
    ('WALLETS/CONTACTLESS', 'WALLETS/CONTACTLESS'),
]

SI_NO_CHOICES = [
    ('', '--- Seleccione ---'),
    ('SI', 'SI'),
    ('NO', 'NO'),
]

STATUS_ID_CHOICES = [
    ('', '--- Seleccione Status ---'),
    ('PENDIENTE', 'PENDIENTE'),
    ('PENDIENTE DE RESPUESTA OTRAS AREAS', 'PENDIENTE DE RESPUESTA OTRAS AREAS'),
    ('SUSPENDIDO', 'SUSPENDIDO'),
    ('CERRADO', 'CERRADO'),
]

IMPACTO_CHOICES = [
    ('', '--- Seleccione Impacto ---'),
    ('AGENCIAS', 'AGENCIAS'),
    ('CAJEROS', 'CAJEROS'),
    ('CALIDAD', 'CALIDAD'),
    ('CNB/EXPRESS', 'CNB/EXPRESS'),
    ('COLABORADORES', 'COLABORADORES'),
    ('ERRORES OPERATIVOS', 'ERRORES OPERATIVOS'),
    ('PREVENCION DE FRAUDES', 'PREVENCION DE FRAUDES'),
    ('SAC', 'SAC'),
    ('TRUNCAMIENTO', 'TRUNCAMIENTO'),
]

DICTAMEN_CHOICES = [
    ('', '--- Seleccione Dictamen ---'),
    ('FRAUDE POR PHISHING SIN IMPACTO', 'FRAUDE POR PHISHING SIN IMPACTO'),
    ('RESPONSABILIDAD DEL CLIENTE', 'RESPONSABILIDAD DEL CLIENTE'),
    ('FRAUDE TD TP', 'FRAUDE TD TP'),
    ('PERDIDA POR DECISION COMERCIAL', 'PERDIDA POR DECISION COMERCIAL'),
    ('FRAUDE TC TP', 'FRAUDE TC TP'),
    ('FRAUDE TC TNP', 'FRAUDE TC TNP'),
    ('FRAUDE POR PHISHING CON IMPACTO', 'FRAUDE POR PHISHING CON IMPACTO'),
    ('FRAUDE POR HURTO', 'FRAUDE POR HURTO'),
    ('FRAUDE TD TNP', 'FRAUDE TD TNP'),
    ('FRAUDE ECOMMERCE', 'FRAUDE ECOMMERCE'),
    ('NO POSEE CARACTERISTICAS FRAUDULENTAS', 'NO POSEE CARACTERISTICAS FRAUDULENTAS'),
    ('FRAUDE INTERNO', 'FRAUDE INTERNO'),
    ('FRAUDE POR FALSIFICACIÓN DE DOCUMENTOS', 'FRAUDE POR FALSIFICACIÓN DE DOCUMENTOS'),
    ('FRAUDE POR ROBO DE IDENTIDAD', 'FRAUDE POR ROBO DE IDENTIDAD'),
    ('FRAUDE POR FALSIFICACIÓN DE CHEQUES', 'FRAUDE POR FALSIFICACIÓN DE CHEQUES'),
    ('PERDIDA POR ERRORES OPERATIVOS', 'PERDIDA POR ERRORES OPERATIVOS'),
]

class WalleBpmForm(forms.ModelForm):
    class Meta:
        model = WalleBpm
        fields = '__all__'
        exclude = [
            'id_relacionado', 'process_type_id', 
            'cantidad_comprobantes', 'nombre_proceso', 
            'mes_reclamo', 'asiento_mes'
        ]

        widgets = {
            'process_id': forms.NumberInput(attrs={'class': 'form-input'}),
            'nro_doc': forms.TextInput(attrs={'class': 'form-input'}),
            'nro_cliente': forms.TextInput(attrs={'class': 'form-input'}),
            'nombre': forms.TextInput(attrs={'class': 'form-input'}),
            'agencia': forms.TextInput(attrs={'class': 'form-input'}),
            'cta': forms.TextInput(attrs={'class': 'form-input'}),
            
            # Selects
            'tipo_de_cuenta': forms.Select(choices=TIPO_CUENTA_CHOICES, attrs={'class': 'form-input'}),
            'moneda': forms.Select(choices=MONEDA_CHOICES, attrs={'class': 'form-input'}),
            'motivo_reclamo': forms.Select(choices=MOTIVO_RECLAMO_CHOICES, attrs={'class': 'form-input'}),
            'resumen_fraude': forms.Select(choices=RESUMEN_FRAUDE_CHOICES, attrs={'class': 'form-input'}),
            'canal': forms.Select(choices=CANAL_CHOICES, attrs={'class': 'form-input'}),
            'sub_canal': forms.Select(choices=SUB_CANAL_CHOICES, attrs={'class': 'form-input'}),
            'tecnologia_usada': forms.Select(choices=TECNOLOGIA_USADA_CHOICES, attrs={'class': 'form-input'}),
            'status_id': forms.Select(choices=STATUS_ID_CHOICES, attrs={'class': 'form-input'}),
            'impacto': forms.Select(choices=IMPACTO_CHOICES, attrs={'class': 'form-input'}),
            'dictamen': forms.Select(choices=DICTAMEN_CHOICES, attrs={'class': 'form-input'}),
            'brinda_dato': forms.Select(choices=SI_NO_CHOICES, attrs={'class': 'form-input'}), # Nuevo Select

            'pin_acceso': forms.TextInput(attrs={'class': 'form-input'}),
            'pin_transaccion': forms.TextInput(attrs={'class': 'form-input'}),
            'fecha_hora': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
            'creation_date': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
            'ingresante': forms.TextInput(attrs={'class': 'form-input'}),
            'comentario': forms.Textarea(attrs={'rows': 2, 'class': 'form-input'}),
            'operacion': forms.TextInput(attrs={'class': 'form-input'}),
            'monto_total': forms.NumberInput(attrs={'class': 'form-input'}),
            
            'importe_reclamado': forms.NumberInput(attrs={'class': 'form-input'}),
            'tipo_cambio_bcp': forms.NumberInput(attrs={'class': 'form-input'}),
            'fecha_asiento': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'fecha_respuesta': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'ultima_modificacion': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
            'giros': forms.NumberInput(attrs={'class': 'form-input'}),
            'otros': forms.NumberInput(attrs={'class': 'form-input'}),
            'td': forms.NumberInput(attrs={'class': 'form-input'}),
            'tc': forms.NumberInput(attrs={'class': 'form-input'}),
            'transferencias_internas_sipap': forms.NumberInput(attrs={'class': 'form-input'}),
            'prestamos_electronicos': forms.NumberInput(attrs={'class': 'form-input'}),
            'recargas_billetera': forms.NumberInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Aplicar clase form-input a todos los campos
        for field in self.fields:
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs['class'] = 'form-input'

        # Campos No Modificables
        # Agregados 'ingresante' y 'fecha_hora' a la lista
        readonly_fields = [
            'process_id', 'nro_doc', 'nro_cliente', 'nombre', 
            'creation_date', 'comentario', 'ultima_modificacion',
            'usuario_modificacion', 'ingresante', 'fecha_hora',
            'agencia_ingresante'
        ]
        
        for field_name in readonly_fields:
            if field_name in self.fields:
                # Siempre deshabilitar process_id, creation_date y ultima_modificacion
                if field_name in ['process_id', 'creation_date', 'ultima_modificacion']:
                    self.fields[field_name].disabled = True
                    self.fields[field_name].widget.attrs['style'] = 'background-color: #f3f4f6; cursor: not-allowed;'
                    self.fields[field_name].required = False
                    if field_name == 'process_id':
                         self.fields[field_name].help_text = "Generado automáticamente"
                
                elif self.instance and self.instance.pk:
                    self.fields[field_name].disabled = True
                    self.fields[field_name].widget.attrs['style'] = 'background-color: #f3f4f6; cursor: not-allowed;'
                elif field_name in ['fecha_hora']:
                    self.fields[field_name].disabled = True
