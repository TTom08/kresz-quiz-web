
document.addEventListener("DOMContentLoaded", async () => {
    const list = document.getElementById("leaderboard-list");

    try {
        const response = await fetch("/leaderboard");
        if (!response.ok) {
            list.textContent = "Nem sikerült betölteni a ranglistát.";
            return;
        }

        const data = await response.json();
        const leaderboard = data.leaderboard;

        if (leaderboard && leaderboard.length > 0) {
            list.innerHTML = "";
            leaderboard.forEach(player => {
                const li = document.createElement("li");
                li.innerHTML = `<span>${player.username}</span> ${player.best_score} pont`;
                list.appendChild(li);
            });
        } else {
            list.textContent = "Nincs elérhető ranglista adat.";
        }
    } catch (error) {
        console.error("Hiba a ranglista betöltésekor:", error);
        list.textContent = "Hiba történt a ranglista lekérésekor.";
    }
});
