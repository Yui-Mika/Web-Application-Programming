const images = [
    "https://picsum.photos/id/237/300/200",
    "https://picsum.photos/id/238/300/200",
    "https://picsum.photos/id/239/300/200"
];

let idx = 0;
const imgTag = document.getElementById('slideshow');
function showImg(i) {
    imgTag.src = images[i];
}
function nextImg() {
    idx = (idx + 1) % images.length;
    showImg(idx);
}

function prevImg() {
    idx = (idx - 1 + images.length) % images.length;
    showImg(idx);
}
setInterval(nextImg, 3000); // Change image every 3 seconds