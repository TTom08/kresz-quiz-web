let questions = [];
let currentQuestionIndex = 0;
let score = 0;
let username = '';
let timerInterval;

const quizArea = document.getElementById('quiz-area');
const resultScreen = document.getElementById('result-screen');
const questionText = document.getElementById('question-text');
const answersContainer = document.getElementById('answers-container');
const feedbackElement = document.getElementById('feedback');
const nextButton = document.getElementById('next-button');
const timeLeftElement = document.getElementById('time-left');
const finalScoreElement = document.getElementById('final-score');

// Managing errors
function showMessage(message, isError = false) {
    console.error(message);
    if (quizArea) {
        quizArea.innerHTML = `<p class="${isError ? 'error-message' : 'info-message'}">${message}</p>`;
    } else {
        document.body.innerHTML = `<p class="${isError ? 'error-message' : 'info-message'}">${message}</p>`;
    }
}

// Register the user and start the quiz
async function registerUserAndStartQuiz() {
    try {
        console.log("Regisztrálás felhasználónévvel:", username);
        
        const response = await fetch('/api/quiz/start', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: username })
        });

        const data = await response.json();
        
        if (response.status === 409) {
            console.log("Felhasználó már létezik, kvíz folytatása...");
            return true;
        }
        
        if (!response.ok) {
            throw new Error(data.error || 'Ismeretlen hiba a felhasználó regisztrációjában.');
        }

        console.log("Felhasználó előkészítve a kvízhez.");
        return true;
    } catch (error) {
        console.error('Hiba a kvíz előkészítésekor:', error);
        showMessage(`Hiba a kvíz indításakor: ${error.message}. Kérjük, próbálja újra.`, true);
        setTimeout(() => window.location.href = '/', 3000);
        return false;
    }
}

// Main loading
window.onload = async () => {
    let tempUsername = typeof FLASK_USERNAME !== 'undefined' ? FLASK_USERNAME : '';
    
    if (typeof tempUsername === 'string' && (tempUsername.startsWith('"') && tempUsername.endsWith('"')) || (tempUsername.startsWith('\'') && tempUsername.endsWith('\''))) {
        tempUsername = tempUsername.substring(1, tempUsername.length - 1);
    }

    username = tempUsername;
    
    console.log("Betöltött felhasználónév:", username);
    
    if (!username || username === 'null' || username === 'undefined' || username.trim() === '') {
        showMessage("Kérjük, először indítsa el a kvízt a kezdőlapon (hiányzó felhasználónév).", true);
        setTimeout(() => window.location.href = '/', 3000);
        return;
    }

    username = username.trim();
    
    console.log("Feldolgozott felhasználónév:", username);

    const success = await registerUserAndStartQuiz();
    
    if (success) {
        await initializeQuiz();
    }
};

// Initialization
async function initializeQuiz() {
    
}