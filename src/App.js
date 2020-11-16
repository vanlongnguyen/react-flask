import React, {Component} from 'react';
import './App.css'
import ReactDOM from 'react-dom';
import './components/report';
import Report from "./components/report";
import Download from "./components/download";
class App extends Component {

    state = {
        generateData: []
    }

    constructor(props) {
        super(props);
        this.generateFile = this.generateFile.bind(this);
    }

    generateFile() {
        fetch('/generate')
            .then(res => res.json())
            .then((data) => {
                this.setState({ generateData: data  })
                // console.log(data);
                new Report().showReportBtn();
                new Download().showLinkDownload(data);
            })
            .catch(console.log)
    }

    render() {
        return (
            <div class="main">
                <center><h3>Generate random string into file
                </h3></center>
                <div class="container center">
                    <button type="button" onClick={() => {
                        this.generateFile();
                        new Download().hideLinkDownload();
                        new Report().hideReport();
                    }}>Generate</button>
                    <br/>
                    <div>
                        <span>Link:</span>
                        <span id="download_link"></span>
                    </div>
                    <br/>
                    <div id="report-block">
                    </div>
                </div>
            </div>
        )
    }
}

export default App;