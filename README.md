# djangocon-demos

Create a venv and install requirements


## Playwright

Dependicies:
* playwright

If you're running this on your personal device
```sh
playwright install
```

```sh
playwright codegen --target python https://djangoproject.com
```

If playwright install doesn't work you can specify your browser
```sh
playwright codegen --target python --browser chromium --channel chrome https://djangoproject.com
```

## μDjango (micro Django)

Dependicies:
* django
* uvicorn


https://www.paulox.net/2023/10/26/udjango_micro_django/

```sh
uvicorn micro_django_main:app --reload
```

## HTMX

Dependicies:
* django-htmx

https://htmx.org/examples/