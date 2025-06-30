function sumArrray(arr) {
    return arr.reduce((sum, num) => sum + num, 0);
}
console.log(sumArrray([1, 2, 3])); // Output: 6