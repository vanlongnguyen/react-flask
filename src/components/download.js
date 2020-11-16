import React, {Component} from 'react';
import ReactDOM from "react-dom";
import Report from "./report";

class Download extends Component {
    constructor(props) {
        super();
        this.downloadTxtFile = this.downloadTxtFile.bind(this);
    }
    downloadTxtFile = (data, click = false) => {
        const url = window.URL.createObjectURL(new Blob([data],{type: 'text/plain'}));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'generated_file.txt');
        document.body.appendChild(link);
        link.click();
    }
    hideLinkDownload() {
        const htmlPlacement =
            (
                <span> Generating...</span>
            );
        ReactDOM.render(htmlPlacement, document.getElementById("download_link"));
    }

    showLinkDownload (data) {
        const htmlPlacement =
            (
                <a href="#" onClick={() => {
                    this.downloadTxtFile(data);
                }}
                >Download here</a>
            );
        ReactDOM.render(htmlPlacement, document.getElementById("download_link"));
    }
}

export default Download;