import { leaderboardMock } from "./mock_data.js";

document.addEventListener("DOMContentLoaded", () => {
    const list = document.getElementById("leaderboard-list");

    if (list && leaderboardMock && leaderboardMock.length > 0) {
        leaderboardMock.forEach(player => {
            const li = document.createElement("li");
            li.textContent = `${player.username} - ${player.score} pont`;
            list.appendChild(li);
        });
    } else {
        list.textContent = "Nincs elérhető ranglista adat.";
    }
});
