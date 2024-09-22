from .base import *

DEBUG = False

MIDDLEWARE.append(
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'