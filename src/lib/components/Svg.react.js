import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * Svg is used to render arbitrary SVG content
 */
export default class Svg extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return <div
        dangerouslySetInnerHTML={{
            __html: this.props.contents
        }}
        />;
    }
}

Svg.defaultProps = {};

Svg.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * An SVG string
     */
    contents: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func
};
