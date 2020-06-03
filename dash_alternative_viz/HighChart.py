# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class HighChart(Component):
    """A HighChart component.
HighChart renders Highcharts.js JSON

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- constructorType (string; optional): 'chart', 'stockChart', 'mapChart', 'ganttChart'
- options (dict; optional): The highcharts chart description"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, constructorType=Component.UNDEFINED, options=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'constructorType', 'options']
        self._type = 'HighChart'
        self._namespace = 'dash_alternative_viz'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'constructorType', 'options']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(HighChart, self).__init__(**args)
