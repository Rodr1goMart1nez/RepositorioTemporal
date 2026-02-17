import random
from django.db import models
from django.utils import timezone

class WalleBpm(models.Model):
    process_id = models.FloatField(db_column='PROCESS_ID', primary_key=True)
    nro_doc = models.CharField(db_column='NRO_DOC', max_length=255, blank=True, null=True)
    nro_cliente = models.CharField(db_column='NRO_CLIENTE', max_length=255, blank=True, null=True)
    impacto = models.CharField(db_column='IMPACTO', max_length=255, blank=True, null=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=255, blank=True, null=True)
    cta = models.CharField(db_column='CTA', max_length=255, blank=True, null=True)
    brinda_dato = models.CharField(db_column='BRINDA_DATO', max_length=255, blank=True, null=True)
    dato_tipo = models.CharField(db_column='DATO_TIPO', max_length=255, blank=True, null=True)
    op_desc = models.CharField(db_column='OP_DESC', max_length=255, blank=True, null=True)
    fecha_hora = models.DateTimeField(db_column='FECHA_HORA', blank=True, null=True)
    bloqueo_canal = models.CharField(db_column='BLOQUEO_CANAL', max_length=255, blank=True, null=True)
    bloqueo_tc_td = models.CharField(db_column='BLOQUEO_TC_TD', max_length=255, blank=True, null=True)
    bloqueo_fondo = models.CharField(db_column='BLOQUEO_FONDO', max_length=255, blank=True, null=True)
    bloqueo_otro = models.CharField(db_column='BLOQUEO_OTRO', max_length=255, blank=True, null=True)
    operacion = models.CharField(db_column='OPERACION', max_length=255, blank=True, null=True)
    process_type_id = models.FloatField(db_column='PROCESS_TYPE_ID', blank=True, null=True)
    id_relacionado = models.FloatField(db_column='ID_RELACIONADO', blank=True, null=True)
    status_id = models.CharField(db_column='STATUS_ID', max_length=100, blank=True, null=True)
    priority_id = models.FloatField(db_column='PRIORITY_ID', blank=True, null=True)
    creation_date = models.DateTimeField(db_column='CREATION_DATE', blank=True, null=True)
    comentario = models.TextField(db_column='COMENTARIO', blank=True, null=True)
    gerente = models.CharField(db_column='GERENTE', max_length=255, blank=True, null=True)
    ingresante = models.CharField(db_column='INGRESANTE', max_length=255, blank=True, null=True)
    agencia_ingresante = models.CharField(db_column='AGENCIA_INGRESANTE', max_length=255, blank=True, null=True)
    monto_total = models.FloatField(db_column='MONTO_TOTAL', blank=True, null=True)
    cantidad_comprobantes = models.FloatField(db_column='CANTIDAD_COMPROBANTES', blank=True, null=True)
    tipo_de_cuenta = models.CharField(db_column='TIPO_DE_CUENTA', max_length=255, blank=True, null=True)
    moneda = models.CharField(db_column='MONEDA', max_length=255, blank=True, null=True)
    nombre_proceso = models.CharField(db_column='NOMBRE_PROCESO', max_length=255, blank=True, null=True)
    empresa_pgs = models.CharField(db_column='EMPRESA_PGS', max_length=255, blank=True, null=True)
    agencia = models.CharField(db_column='AGENCIA', max_length=255, blank=True, null=True)
    pin_acceso = models.CharField(db_column='PIN_ACCESO', max_length=255, blank=True, null=True)
    pin_transaccion = models.CharField(db_column='PIN_TRANSACCION', max_length=255, blank=True, null=True)
    giros = models.DecimalField(db_column='GIROS', max_digits=18, decimal_places=2, blank=True, null=True)
    otros = models.DecimalField(db_column='OTROS', max_digits=18, decimal_places=2, blank=True, null=True)
    td = models.DecimalField(db_column='TD', max_digits=18, decimal_places=2, blank=True, null=True)
    tc = models.DecimalField(db_column='TC', max_digits=18, decimal_places=2, blank=True, null=True)
    transferencias_internas_sipap = models.DecimalField(db_column='TRANSFERENCIAS_INTERNAS_SIPAP', max_digits=18, decimal_places=2, blank=True, null=True)
    prestamos_electronicos = models.DecimalField(db_column='PRESTAMOS_ELECTRONICOS', max_digits=18, decimal_places=2, blank=True, null=True)
    recargas_billetera = models.DecimalField(db_column='RECARGAS_BILLETERA', max_digits=18, decimal_places=2, blank=True, null=True)
    activacion_chat_online = models.CharField(db_column='ACTIVACION_CHAT_ONLINE', max_length=50, blank=True, null=True)
    alta_tc = models.CharField(db_column='ALTA_TC', max_length=50, blank=True, null=True)
    asiento_mes = models.CharField(db_column='ASIENTO_MES', max_length=50, blank=True, null=True)
    asumido_por_proveedores = models.CharField(db_column='ASUMIDO_POR_PROVEEDORES', max_length=50, blank=True, null=True)
    ban_rdis = models.CharField(db_column='BAN_RDIS', max_length=50, blank=True, null=True)
    canal = models.CharField(db_column='CANAL', max_length=50, blank=True, null=True)
    cheques_pagados = models.CharField(db_column='CHEQUES_PAGADOS', max_length=50, blank=True, null=True)
    debito_automatico = models.CharField(db_column='DEBITO_AUTOMATICO', max_length=50, blank=True, null=True)
    dictamen = models.CharField(db_column='DICTAMEN', max_length=100, blank=True, null=True)
    fecha_asiento = models.CharField(db_column='FECHA_ASIENTO', max_length=50, blank=True, null=True)
    fecha_cierre = models.CharField(db_column='FECHA_CIERRE', max_length=50, blank=True, null=True)
    ultima_modificacion = models.DateTimeField(db_column='ULTIMA_MODIFICACION', blank=True, null=True)
    fecha_respuesta = models.CharField(db_column='FECHA_RESPUESTA', max_length=50, blank=True, null=True)
    fondos_cliente_protegido = models.CharField(db_column='FONDOS_CLIENTE_PROTEGIDO', max_length=50, blank=True, null=True)
    importe_acreditado_cta = models.CharField(db_column='IMPORTE_ACREDITADO_CTA', max_length=50, blank=True, null=True)
    importe_afectado_perdidas = models.CharField(db_column='IMPORTE_AFECTADO_PERDIDAS', max_length=50, blank=True, null=True)
    importe_reclamado = models.DecimalField(db_column='IMPORTE_RECLAMADO', max_digits=12, decimal_places=2, blank=True, null=True)
    importe_salvado_protegido = models.CharField(db_column='IMPORTE_SALVADO_PROTEGIDO', max_length=50, blank=True, null=True)
    mes_reclamo = models.CharField(db_column='MES_RECLAMO', max_length=100, blank=True, null=True)
    motivo_reclamo = models.CharField(db_column='MOTIVO_RECLAMO', max_length=100, blank=True, null=True)
    numero_asiento = models.CharField(db_column='NUMERO_ASIENTO', max_length=50, blank=True, null=True)
    otras_perdidas_pyg = models.CharField(db_column='OTRAS_PERDIDAS_PYG', max_length=50, blank=True, null=True)
    observacion = models.CharField(db_column='OBSERVACION', max_length=100, blank=True, null=True)
    pagos_qr = models.CharField(db_column='PAGOS_QR', max_length=50, blank=True, null=True)
    pagos_servicios = models.CharField(db_column='PAGOS_SERVICIOS', max_length=50, blank=True, null=True)
    pago_tc = models.CharField(db_column='PAGO_TC', max_length=50, blank=True, null=True)
    pais = models.CharField(db_column='PAIS', max_length=50, blank=True, null=True)
    responsable_analisis = models.CharField(db_column='RESPONSABLE_ANALISIS', max_length=50, blank=True, null=True)
    resumen_fraude = models.CharField(db_column='RESUMEN_FRAUDE', max_length=100, blank=True, null=True)
    sub_canal = models.CharField(db_column='SUB_CANAL', max_length=100, blank=True, null=True)
    tecnologia_usada = models.CharField(db_column='TECNOLOGIA_USADA', max_length=100, blank=True, null=True)
    tipo_cambio_bcp = models.DecimalField(db_column='TIPO_CAMBIO_BCP', max_digits=10, decimal_places=2, blank=True, null=True)
    usuario_modificacion = models.CharField(db_column='USUARIO_MODIFICACION', max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.process_id:
            # Generar un ID aleatorio de 8 dígitos
            self.process_id = float(random.randint(10000000, 99999999))
        
        if not self.creation_date:
            # Asignar la fecha y hora actual en la creación
            self.creation_date = timezone.now()
        
        # Siempre actualizar la última modificación al guardar
        self.ultima_modificacion = timezone.now()
            
        super().save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'WALLE_BPM'
