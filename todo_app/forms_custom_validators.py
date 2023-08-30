import datetime

from wtforms import ValidationError


def DateCheck():
    message = f'Date must be after {datetime.date.today()}'

    def _DateCheck(field, form):
        if field.data.get('expire_date') < datetime.date.today():
            raise ValidationError(message)

    return _DateCheck
