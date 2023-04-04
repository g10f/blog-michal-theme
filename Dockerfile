FROM ghcr.io/g10f/blog-site:1.0.0

COPY michal_theme michal_theme
ARG SECRET_KEY=dummy
RUN ./manage.py collectstatic --clear --noinput
