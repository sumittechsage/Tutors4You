from .base import *

DEBUG = False

MIDDLEWARE.append(
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]



CSRF_TRUSTED_ORIGINS = [
    'https://tutors4you.onrender.com',
]
ALLOWED_HOSTS = ['https://tutors4you.onrender.com']
CORS_ALLOWED_ORIGINS = ['https://tutors4you.onrender.com']
