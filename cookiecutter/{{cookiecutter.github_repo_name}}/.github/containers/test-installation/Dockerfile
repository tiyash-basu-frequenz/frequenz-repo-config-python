# License: {{cookiecutter.license}}
# Copyright © {% now 'utc', '%Y' %} {{cookiecutter.author_name}}
{% raw -%}

# This Dockerfile is used to test the installation of the python package in
# multiple platforms in the CI. It is not used to build the package itself.

FROM --platform=${TARGETPLATFORM} python:3.11-slim

RUN python -m pip install --upgrade --no-cache-dir pip

COPY dist dist
RUN pip install dist/*.whl && \
    rm -rf dist
{%- endraw %}
