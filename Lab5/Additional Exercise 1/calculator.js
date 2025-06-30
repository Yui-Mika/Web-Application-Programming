function calculate(op) {
    const n1 = parseFloat(document.getElementById("num1").value) || 0;
    const n2 = parseFloat(document.getElementById("num2").value) || 0;
    let res;
    if (op === "+") {
        res = n1 + n2;
    }
    else if (op === "-") {
        res = n1 - n2;
    }
    else if (op === "*") {
        res = n1 * n2;
    }
    else if (op === '/') {
    if (n2 !== 0) {
        res = n1 / n2;
    } else {
        res = "Error: Division by zero";
    }
} else {
    res = "Error: Invalid operation";
}
    document.getElementById('result').textContent = 'Result: ' + res;
}