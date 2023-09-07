# bir app oluşturunca ekleyince
    . installed app lere ekle
    . url de path ekle

# TokenAuthentication için
    . settings.py a ekle
 REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}