# config.py

"""
Archivo de configuración.
Contiene parámetros de conexión a InfluxDB y otras configuraciones globales.
"""

# Configuración para InfluxDB 1.8
INFLUXDB1_CONFIG = {
    'host': 'smartsetdb.brazilsouth.cloudapp.azure.com',
    'port': 7195,
    'username': 'mpoliti',
    'password': 'GenInti23',
    'database': 'ss_genrod',
    'ssl': True,
    'timeout': 300,
    'verify_ssl': False
}

# Configuración para InfluxDB 2.7
INFLUXDB2_CONFIG = {
    'url': "http://149.78.55.22:10010",
    'token': "z66S7YKFLYmofPczzaKMCSbWNlowKGytBYBdmnPwxGyU5ueOZK288-Q_1GLjXjNlSBn8uc4bG6Dq-jmxUVOTQQ==",
    'org': "97d58b9470b74eb5",
    'timeout': 90000,
    'ssl': True,
    'verify_ssl': False,
    'bucket': "ss_genrod"
}

# Otros parámetros globales
LOCAL_TIMEZONE = 'America/Argentina/Buenos_Aires'

