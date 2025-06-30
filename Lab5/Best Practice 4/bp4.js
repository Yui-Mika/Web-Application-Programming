function divide(a,b) {
    try {
        if (b === 0) {
            throw new Error("Division by zero");
        }
        return a / b;
    } catch (err) {
        console.error("Error:", err.message);
        return null; // or handle the error as needed
    }
}
console.log(divide(10, 2)); // 5
console.log(divide(10, 0)); // Error: Division by zero
