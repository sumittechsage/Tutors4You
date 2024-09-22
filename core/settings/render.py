from .base import *

DEBUG = False



STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


ALLOWED_HOSTS = ['https://tutors4you.onrender.com']
CORS_ALLOWED_ORIGINS = ['https://tutors4you.onrender.com']

# CSRF_TRUSTED_ORIGINS = [
#     'https://tutors4you.onrender.com',
# ]
