FROM ghcr.io/g10f/blog-site:1.2.1

COPY michal_theme michal_theme
ENV DJANGO_SETTINGS_MODULE=blogsite.settings.production
ENV THEME=michal_theme
ARG SECRET_KEY=dummy
ARG RECAPTCHA_PUBLIC_KEY=dummy
ARG RECAPTCHA_PRIVATE_KEY=dummy
RUN ./manage.py collectstatic --noinput
