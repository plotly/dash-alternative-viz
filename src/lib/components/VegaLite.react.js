import React, {Component} from 'react';
import PropTypes from 'prop-types';
import vegaEmbed from 'vega-embed'

/**
 * VegaLite renders vega-lite visualizations.
 */
export default class VegaLite extends Component {

    constructor(props) {
        super(props);
        this.getRef = this.getRef.bind(this);
    }

    getRef(el) {
        this.el = el;
    }

    componentDidMount() {
        if (!this.props.spec){ return;}
        vegaEmbed(this.el, this.props.spec);
    }

    componentDidUpdate() {
        if (!this.props.spec){ return;}
        vegaEmbed(this.el, this.props.spec);
    }

    render() {
        return <div id="vis" ref={this.getRef} />;
    }
}

VegaLite.defaultProps = {};

VegaLite.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * A Vega-Lite spec.
     */
    spec: PropTypes.object,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func
};
