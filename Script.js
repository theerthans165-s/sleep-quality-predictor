function predict() {
    let sleep = parseFloat(document.getElementById("sleep").value);
    let stress = parseInt(document.getElementById("stress").value);

    let result = "";

    if (sleep >= 7 && stress <= 5) {
        result = "✅ Good Sleep Expected";
    } else {
        result = "⚠️ Poor Sleep Expected";
    }

    document.getElementById("result").innerHTML = result;
}
