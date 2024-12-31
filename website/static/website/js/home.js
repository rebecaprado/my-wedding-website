const weddingDate = new Date("April 18, 2025 19:00:00").getTime(); 

function countDown() {
    const now = new Date().getTime();
    const timeLeft = weddingDate - now;

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    let realDays;
    if (days < 10) {
        realDays = '0'+ days;
    } else {
        realDays = days;
    }

    document.getElementById('days').innerHTML = realDays;

    let realHours;
    if (hours < 10) {
        realHours = '0'+ hours;
    } else {
        realHours = hours;
    }

    document.getElementById('hours').innerHTML = realHours;

    let realMinutes;
    if (minutes < 10) {
        realMinutes = '0'+ minutes;
    } else {
        realMinutes = minutes;
    }

    document.getElementById('minutes').innerHTML = realMinutes;

    let realSeconds;
    if (seconds < 10) {
        realSeconds = '0'+ seconds;
    } else {
        realSeconds = seconds;
    }

    document.getElementById('seconds').innerHTML = realSeconds;

    if (timeLeft < 0) {
        document.querySelector('.countdown').innerHTML = "Chegou o momento tão esperado!";
        return;
    }
}

setInterval(countDown, 1000);