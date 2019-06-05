import React, {Component} from 'react';
import PropTypes from 'prop-types';
const BokehJS = require("bokehjs");

/**
 * BokehJSON renders Bokeh JSON.
 */
export default class BokehJSON extends Component {

    constructor(props) {
        super(props);
        this.getRef = this.getRef.bind(this);
        this.renderChart = this.renderChart.bind(this);
        this.num = 0;
    }

    getRef(el) {
        this.el = el;
    }

    renderChart() {
        if (!this.props.json){ return;}
        while (this.el.firstChild) {
            this.el.removeChild(this.el.firstChild);
        }
        const g = document.createElement('div');
        const id = 'bokehjson'+this.props.id + (this.num++);
        g.setAttribute("id", id);
        this.el.appendChild(g);
        BokehJS.embed.embed_item(this.props.json, id);
    }

    componentDidMount() {
        this.renderChart()
    }

    componentDidUpdate() {
        this.renderChart()
    }

    render() {
        return <div ref={this.getRef} />;
    }
}

BokehJSON.defaultProps = {};

BokehJSON.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * A Bokeh json object.
     */
    json: PropTypes.object,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func
};
