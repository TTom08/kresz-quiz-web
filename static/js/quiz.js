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
    try {
        const response = await fetch('/api/quiz/questions');
        if (!response.ok) {
            throw new Error('Hiba a kérdések betöltésekor.');
        }
        questions = await response.json();
        
        if (questions.length === 0) {
            showMessage("A kvíz nem indul el: nincs betöltött kérdés.", true);
            return;
        }

        if (quizArea) quizArea.style.display = 'block';
        loadQuestion();
    } catch (error) {
        console.error('Hiba:', error);
        showMessage(`Hiba történt a kvíz betöltésekor: ${error.message}`, true);
    }
}

// Loading questions
function loadQuestion() {
    if (currentQuestionIndex >= questions.length) {
        endQuiz();
        return;
    }

    const currentQuestion = questions[currentQuestionIndex];
    questionText.textContent = `${currentQuestionIndex + 1}. ${currentQuestion.text}`;
    answersContainer.innerHTML = '';
    feedbackElement.textContent = '';
    nextButton.style.display = 'none';

    currentQuestion.answers.forEach(answer => {
        const button = document.createElement('button');
        button.textContent = answer.text;
        button.classList.add('answer-button');
        button.addEventListener('click', () => handleAnswer(button, answer));
        answersContainer.appendChild(button);
    });
}

// Handling the answer given by the player
function handleAnswer(clickedButton, answer) {
    Array.from(answersContainer.children).forEach(button => {
        button.disabled = true;
    });

    const isCorrect = answer.is_correct;

    if (isCorrect) {
        clickedButton.classList.add('correct');
        score++;
        feedbackElement.textContent = 'Helyes.';
    } else {
        clickedButton.classList.add('incorrect');
        feedbackElement.textContent = 'Helytelen.';
        
        const correctAnswerButton = Array.from(answersContainer.children).find(btn => 
            questions[currentQuestionIndex].answers.find(a => a.is_correct)?.text === btn.textContent
        );
        if (correctAnswerButton) {
            correctAnswerButton.classList.add('correct');
        }
    }

    nextButton.style.display = 'block';
    nextButton.onclick = nextQuestion;
}

function nextQuestion() {
    currentQuestionIndex++;
    loadQuestion();
}

// Timer
function startTimer(duration) {
    let time = duration;
    timeLeftElement.textContent = time;
    timeLeftElement.classList.remove('time-warning');
    timerInterval = setInterval(() => {
        time--;
        timeLeftElement.textContent = time;
        if (time <= 10) {
            timeLeftElement.classList.add('time-warning');
        }
        if (time <= 0) {
            clearInterval(timerInterval);
            forceNextQuestionDueToTimeout();
        }
    }, 1000);
}

// If timer ends, skip to next question
function forceNextQuestionDueToTimeout() {
    Array.from(answersContainer.children).forEach(button => {
        button.disabled = true;
    });

    feedbackElement.textContent = 'Lejárt az idő. Helytelen.';

    const correctAnswerButton = Array.from(answersContainer.children).find(btn => 
        questions[currentQuestionIndex].answers.find(a => a.is_correct)?.text === btn.textContent
    );
    if (correctAnswerButton) {
        correctAnswerButton.classList.add('correct');
    }

    nextButton.style.display = 'block';
    nextButton.onclick = nextQuestion;
}

// Quiz end
async function endQuiz() {
    clearInterval(timerInterval);

    try {
        const response = await fetch('/api/quiz/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: username, score: score })
        });

        const data = await response.json();
        if (response.ok || response.status === 201) {
            finalScoreElement.textContent = score;
            if (quizArea) quizArea.style.display = 'none';
            if (resultScreen) resultScreen.style.display = 'block';
        } else {
            showMessage(`Hiba a pontszám elküldésében: ${data.error || 'Ismeretlen hiba'}`, true);
        }
    } catch (error) {
        console.error("Hiba a pontszám küldésekor:", error);
        showMessage("Hálózati hiba a pontszám küldésekor.", true);
    }
}