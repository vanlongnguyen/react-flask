import React, {Component} from 'react';
import ReactDOM from "react-dom";

class Report extends Component {
    constructor(props) {
        super(props);
        this.showReport = this.showReport.bind(this);
        this.getStatistic = this.getStatistic.bind(this);
    }
    getStatistic() {
        fetch('/readFile')
            .then(res => res.json())
            .then((data) => {
                this.showReport(data);
            })
            .catch(console.log)
    }
    showReportBtn() {
        const html = (
            <div>
                <button type="button" onClick={ this.getStatistic }>Report</button>
                <div id="report-content"></div>
            </div>
        );
        ReactDOM.render(html, document.getElementById("report-block"));
    }
    hideReport() {
        const html = (
            <span></span>
        );
        ReactDOM.render(html, document.getElementById("report-block"));
    }
    showReport(data) {
        const html =
            (
                <div>
                    <p>Integers:{ data.int }</p>
                    <p>Alphabetical string:{ data.string }</p>
                    <p>Real numbers:{ data.real_number }</p>
                    <p>Alphanumberic:{ data.alphanumberic }</p>
                </div>
            );
        ReactDOM.render(html, document.getElementById("report-content"));
    }
}
export default Report;