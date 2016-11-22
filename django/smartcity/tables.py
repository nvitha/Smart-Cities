import django_tables2 as tables
from .models import Topics, ButtonPresses


class TopicsTable(tables.Table):
    class Meta:
        model = Topics
        attrs = {'class': 'table-center mdl-data-table mdl-js-data-table mdl-data-table--selectable mdl-shadow--2dp'}
        row_attrs = {'class': 'mdl-data-table__cell--non-numeric'}


class RivaTable(tables.Table):
    class Meta:
        model = ButtonPresses
        attrs = {'class': 'table-center mdl-data-table mdl-js-data-table mdl-data-table--selectable mdl-shadow--2dp full-width'}
        row_attrs = {'class': 'mdl-data-table__cell--non-numeric'}

