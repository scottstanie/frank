"""
This file us used for site setup and multi-site configuration.

"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define your sites here:

SITES = {
    'default': {
        'SITE_NAME': 'Frank',
        'SITE_DOMAIN': 'frankapi.herokuapp.com',
        'SITE_ID': 1,

        # The following are database settings for your app.
        # For more info on databases in Django, see:
        # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

        # For Postgres, replace the related lines under DATABASE:
        # DB_ENGINE = 'django.db.backends.postgresql_psycopg2'
        # DB_NAME = 'yourappdbname'
        # etc.

        # DATABASE is the production database, used when DB_ENV = 'prod'
        # LOCAL_DATABASE is used when DB_ENV = 'dev'
        # There is no need to touch the settings for LOCAL_DATABASE.

        # 'LOCAL_DATABASE': {
        #     'DB_ENGINE': 'django.db.backends.sqlite3',
        #     'DB_NAME': os.path.join(BASE_DIR, 'wolfhound_dev_database.db'),
        #     'DB_USER': '',
        #     'DB_PASSWORD': '',
        #     'DB_HOST': '',
        #     'DB_PORT': ''
        # }
    }
}


def generate_cors_whitelist(site_dict):
    domain_list = ['localhost:4200', 'localhost:3000']
    for key in site_dict.keys():
        domain_list.append(site_dict[key]['SITE_DOMAIN'])
    return tuple(domain_list)
