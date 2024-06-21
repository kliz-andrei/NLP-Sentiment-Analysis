let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(xhttp.responseText);
            if (response.error) {
                document.getElementById("system_response").innerHTML = `Error: ${response.error}`;
            } else {
                document.getElementById("system_response").innerHTML = `Label: ${response.label}, Score: ${response.score}`;
            }
        }
    };
    xhttp.open("GET", "sentimentAnalyzer?textToAnalyze=" + textToAnalyze, true);
    xhttp.send();
}
