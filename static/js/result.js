
document.addEventListener("DOMContentLoaded", () => {
    const scoreText = document.getElementById("score-text");

    const username = sessionStorage.getItem("username");
    const score = sessionStorage.getItem("score");

    sessionStorage.removeItem("username");
    sessionStorage.removeItem("score");

     if (username && score) {

        const formattedScore = parseFloat(score).toFixed(2);
        scoreText.textContent = `Pontszámod: ${formattedScore}`;
    } else {
        scoreText.textContent = "Nincs elérhető pontszám.";
    }
});
