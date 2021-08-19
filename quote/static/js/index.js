const getQuote = async () => {
    const response = await fetch('/quote');
    const myJson = await response.json(); //extract JSON from the http response
    // do something with myJson
    console.log(myJson)

    // Get container.
    element = document.getElementById('quotes');

    element.insertAdjacentHTML(
        "afterbegin",
        "" +
        "<div class=\"card\">\n" +
        "    <div class=\"card-header\">\n" +
        "        " + myJson["author"] + "\n" +
        "    </div>" +
        "    <div class=\"card-body\">\n" +
        "        " + myJson["quote"] + "\n" +
        "    </div>\n" +
        "</div>"
    )
}