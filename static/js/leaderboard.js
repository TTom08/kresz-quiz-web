document.addEventListener("DOMContentLoaded", async () => {
    const list = document.getElementById("leaderboard-list");

    try {
        const response = await fetch("/api/quiz/leaderboard");
        if (!response.ok) {
            list.textContent = "Nem sikerült betölteni a ranglistát.";
            return;
        }

        const data = await response.json();
        const leaderboard = data.leaderboard;

        if (leaderboard && leaderboard.length > 0) {
            list.innerHTML = "";

            leaderboard.forEach((player, index) => {
                const li = document.createElement("li");
                li.innerHTML = `
                    <span class="rank">${index + 1}.</span>
                    <span class="name">${player.username}</span>
                    <span class="score">${player.score} pont</span>
                `;


                if (index === 0) li.classList.add("gold");
                else if (index === 1) li.classList.add("silver");
                else if (index === 2) li.classList.add("bronze");

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
