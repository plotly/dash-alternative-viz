# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Svg(Component):
    """A Svg component.
Svg is used to render arbitrary SVG content

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- contents (string; optional): An SVG string"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, contents=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'contents']
        self._type = 'Svg'
        self._namespace = 'dash_vis'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'contents']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Svg, self).__init__(**args)
