import pandas as pd

# Suponiendo que algunos elementos son dataframes y otros son 0
dataframes = [df_LOGS, 0, df_PIN_TRANS, None, df_PAGO_SERVICIOS, df_ITOKEN, 0, df_OTP_ITOKEN]
nombres = ["LOGS", "PIN_ACCESO", "PIN_TRANS", "TRANS_REALIZADAS", "PAGO_SERVICIOS", "ITOKEN", "TOKENIZATION", "OTP_ITOKEN"]

# Filtrar solo los que son DataFrame
dataframes_filtrados = []
nombres_filtrados = []

for df, nombre in zip(dataframes, nombres):
    if isinstance(df, pd.DataFrame):
        dataframes_filtrados.append(df)
        nombres_filtrados.append(nombre)

# Resultado: solo los dataframes y sus nombres asociados
print(nombres_filtrados)
print(dataframes_filtrados)
