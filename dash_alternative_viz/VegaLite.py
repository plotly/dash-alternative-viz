# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class VegaLite(Component):
    """A VegaLite component.
VegaLite renders vega-lite visualizations.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- spec (dict; optional): A Vega-Lite spec."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, spec=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'spec']
        self._type = 'VegaLite'
        self._namespace = 'dash_alternative_viz'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'spec']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(VegaLite, self).__init__(**args)
