const questions = [
  {
    q: "What is 2 + 2?",
    a: ["3", "4", "5"],
    correct: 1
  },
  {
    q: "What is the capital of Vietnam?",
    a: ["Hanoi", "HCM City", "Hue"],
    correct: 0
  }
];
function renderQuiz() {
  const quizDiv = document.getElementById('quiz');
  quizDiv.innerHTML = "";
  questions.forEach((ques, i) => {
    quizDiv.innerHTML += `<div class="q">${i+1}. ${ques.q}</div>` +
      ques.a.map((ans, idx) =>
        `<label>
          <input type="radio" name="q${i}" value="${idx}"> ${ans}
        </label>`
      ).join("<br>") + "<br><br>";
  });
}
function showResult() {
  let score = 0;
  questions.forEach((q, i) => {
    const selected = document.querySelector(`input[name=q${i}]:checked`);
    if (selected && Number(selected.value) === q.correct) score++;
  });
  document.getElementById('score').textContent = `Score: ${score}/${questions.length}`;
}
renderQuiz();
