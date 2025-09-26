
document.addEventListener("DOMContentLoaded", () => {
    const scoreText = document.getElementById("score-text");

    const username = sessionStorage.getItem("username");
    const score = sessionStorage.getItem("score");

    sessionStorage.removeItem("username");
    sessionStorage.removeItem("score");

    if (username && score) {
        scoreText.textContent = `Pontszámod: ${score}`;
    } else {
        scoreText.textContent = "Nincs elérhető pontszám.";
    }
});
