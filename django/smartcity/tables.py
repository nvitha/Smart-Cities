import django_tables2 as tables
from .models import Topics, Data


class DjangoRivaTable(tables.Table):
    value_string = tables.Column(verbose_name='Simulation Command')
    ts = tables.Column(verbose_name='Datetime')

    def render_value_string(self, value):
        if value == '"st"':
            return 'Start Thrashing Test'
        elif value == '"et"':
            return 'End Thrashing Test'
        elif value == '"su"':
            return 'Start Flood Test'
        elif value == '"eu"':
            return 'End Flood Test'
        elif value == '"sr"':
            return 'Start Random Flood Test'
        elif value == '"er"':
            return 'End Random Flood Test'

    class Meta:
        model = Data
        fields = ('value_string', 'ts')
        attrs = {'class': 'table-center mdl-data-table mdl-js-data-table mdl-data-table--selectable mdl-shadow--2dp full-width'}
        row_attrs = {'class': 'mdl-data-table__cell--non-numeric'}


class RivaCommandsTable(tables.Table):
    ts = tables.Column(verbose_name='Datetime')
    topic_id = tables.Column(verbose_name='Switch to Mode')

    def render_topic_id(self, value):
        if value == 5:
            return 'Optimization Mode'
        if value == 6:
            return 'Building Mode'
        if value == 7:
            return 'Grid Mode'
        if value == 8:
            return 'Emergency Mode'


    class Meta:
        model = Data
        fields = ('topic_id', 'ts')
        attrs = {'class': 'table-center mdl-data-table mdl-js-data-table mdl-data-table--selectable mdl-shadow--2dp full-width'}
        row_attrs = {'class': 'mdl-data-table__cell--non-numeric'}


class BacTable(tables.Table):
    value_string = tables.Column(verbose_name='Building Mode')
    ts = tables.Column(verbose_name='Datetime')

    def render_value_string(self, value):
        if value == '"bm1"':
            return 'Optimization Mode'
        if value == '"bm2"':
            return 'Building Mode'
        if value == '"bm3"':
            return 'Grid Mode'
        if value == '"bm4"':
            return 'Emergency Mode'

    class Meta:
        model = Data
        fields = ('value_string', 'ts')
        attrs = {'class': 'table-center mdl-data-table mdl-js-data-table mdl-data-table--selectable mdl-shadow--2dp full-width'}
        row_attrs = {'class': 'mdl-data-table__cell--non-numeric'}

