import { resultMock } from "./mock_data.js";

document.addEventListener("DOMContentLoaded", () => {
    const scoreText = document.getElementById("score-text");

    if (resultMock && scoreText) {
        scoreText.textContent = `Pontszámod: ${resultMock.score}`;
    } else {
        scoreText.textContent = "Hiba történt az eredmény betöltésekor.";
    }
});
