"""
Django settings for my_test_dpedu project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 密钥配置
SECRET_KEY = 'xu%zt$3!zq-k$zyg4sr%g8724a33c-j9!u*+=!2kdnoab+re0#'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式，在开发阶段应置为True，调试过程中会自动检测代码是否发生更改，根据检测结果执行是否刷新重启系统。
# 如果项目部署上线，应将其改为False，否则容易泄露系统相关的信息
DEBUG = True

# 域名访问权限，默认为空。当DEBUG为True并且ALLOWED_HOSTS为空时，项目只允许以localhost或127.0.0.1在浏览器上访问。
# 当DEBUG为False时，allowed_hosts为必填项，否则程序无法启动。
ALLOWED_HOSTS = []
# 如果想允许所有域名访问，可设置
# ALLOWED_HOSTS = ['*']


# Application definition

#App列表
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 我的测试应用
    'my_test_dpedu',
    'index',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 该设定将中间件使用中文admin后台也使用中文
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'my_test_dpedu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'index/templates/templates'),
                 os.path.join(BASE_DIR, 'index/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_test_dpedu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),


        'USER':'root',
        'PASSWORD':'1234',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# 是必须配置的属性而且属性值不能为空，如果没有配置STATICFILES_DIRS,则STATIC_URL只能识别APP里的static静态资源文件夹。
STATIC_URL = '/static/'

# 如果想要在项目根目录下存放静态资源，可以配置以下属性。STATICFILES_DIRS是可选配置属性。
# 无论静态资源文件夹如何命名，在浏览器上静态资源的上级目录必须为static
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'public_static'),
                    # 设置APP(index)的静态资源文件夹index_static
                    os.path.join(BASE_DIR, 'index/index_static'),
                    ]

