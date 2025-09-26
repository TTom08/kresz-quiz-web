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

            leaderboard.forEach((player, index) => {
                const li = document.createElement("li");
                li.innerHTML = `<span>${player.username}</span> ${player.best_score} pont`;


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
