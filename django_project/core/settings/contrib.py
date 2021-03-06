# -*- coding: utf-8 -*-
from .base import *  # noqa

# Extra installed apps
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',  # enable Raven plugin
    'pipeline',
    'user_map',
    'leaflet',
    'bootstrapform'
)

# User map sets up auth where users are identified by their email,
# not by their user name.
AUTH_USER_MODEL = 'user_map.User'
AUTHENTICATION_BACKENDS = [
    'user_map.auth_backend.UserMapAuthBackend',
    'django.contrib.auth.backends.ModelBackend']

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'user_map.context_processors.user_map_settings',
)

LEAFLET_CONFIG = {
    'TILES': [
        (
            'OpenStreetMap',
            'http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
            ('© <a href="http://www.openstreetmap.org" '
             'target="_parent">OpenStreetMap</a> and contributors, under an '
             '<a href="http://www.openstreetmap.org/copyright" '
             'target="_parent">open license</a>')
        )]

}
