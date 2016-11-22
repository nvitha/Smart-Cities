from .models import ButtonPresses


class ChartData(object):

    @classmethod
    def get_value_counts(cls):

        table = ButtonPresses.objects.all()

        data = {}
        for row in table:
            if row.button_pressed not in data:
                data = row.button_pressed
            else:
                data[row.button_pressed] += 1

        return data
