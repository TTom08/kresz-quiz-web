
document.addEventListener("DOMContentLoaded", async () => {
    const scoreText = document.getElementById("score-text");

    try {

        const username = sessionStorage.getItem("username");
        const score = sessionStorage.getItem("score");

        if (!username || !score) {
            scoreText.textContent = "Nincs elérhető pontszám.";
            return;
        }


        const response = await fetch("/submit", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, score: parseFloat(score) })
        });

        if (!response.ok) {
            const errorData = await response.json();
            scoreText.textContent = `Hiba: ${errorData.error}`;
            return;
        }


        scoreText.textContent = `Pontszámod: ${score}`;

    } catch (error) {
        console.error("Hiba a pontszám beküldésekor:", error);
        scoreText.textContent = "Hiba történt az eredmény betöltésekor.";
    }
});
