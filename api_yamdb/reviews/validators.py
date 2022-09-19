import datetime as dt

from django.core.exceptions import ValidationError


def validate_max_year(year_user):
    year = dt.datetime.today().year
    if year_user > year:
        raise ValidationError(
            'Год превышает нынешний'
        )
