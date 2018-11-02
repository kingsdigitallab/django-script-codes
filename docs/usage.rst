=====
Usage
=====

To use Django Script Codes (ISO 15924) in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'script_codes.apps.ScriptCodesConfig',
        ...
    )

To reference Script Codes in your models:

.. code-block:: python

    from django.db import models
    from script_codes.models import Script


    class MyModel(models.Model):
        ...
        script = models.ForeignKey(Script, on_delete=models.CASCADE)
        ...
    ]
