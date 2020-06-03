import React, {Component} from 'react';
import PropTypes from 'prop-types';
import HighchartsReact from 'highcharts-react-official';
/**
 * HighChart renders Highcharts.js JSON
 */
export default class HighChart extends Component {
    render() {
        const {constructorType, options} = this.props;
        return (
            <HighchartsReact
                highcharts={window.Highcharts}
                options={options}
                constructorType={constructorType}
            />
        );
    }
}
HighChart.defaultProps = {};
HighChart.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    /**
     * 'chart', 'stockChart', 'mapChart', 'ganttChart'
     */
    constructorType: PropTypes.string,
    /**
     * The highcharts chart description
     */
    options: PropTypes.object,
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
