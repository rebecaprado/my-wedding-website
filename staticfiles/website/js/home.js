const weddingDate = new Date("April 18, 2025 19:00:00").getTime();

function countDown() {
    const now = new Date().getTime();
    const timeLeft = weddingDate - now;

    if (timeLeft < 0) {
        document.querySelector('.countdown').innerHTML = "Chegou o momento tão esperado!";
        return;
    }

    const formatNumber = (num) => (num < 10 ? `0${num}` : num);

    const days = formatNumber(Math.floor(timeLeft / (1000 * 60 * 60 * 24)));
    const hours = formatNumber(Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)));
    const minutes = formatNumber(Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60)));
    const seconds = formatNumber(Math.floor((timeLeft % (1000 * 60)) / 1000));

    document.getElementById('days').innerHTML = days;
    document.getElementById('hours').innerHTML = hours;
    document.getElementById('minutes').innerHTML = minutes;
    document.getElementById('seconds').innerHTML = seconds;
}

setInterval(countDown, 1000);

document.addEventListener('DOMContentLoaded', function () {
    const eventDays0 = document.getElementById('id_days_present_0');
    const eventDays1 = document.getElementById('id_days_present_1');
    const confirmation = document.getElementById('id_confirmation');
    const form = document.getElementById("rsvp-form");
    const successMessage = document.getElementById("rsvp-message-1");

    const toggleDays = (isDisabled) => {
        eventDays0.disabled = isDisabled;
        eventDays1.disabled = isDisabled;
        if (isDisabled) {
            eventDays0.checked = false;
            eventDays1.checked = false;
            eventDays0.required = false;
            eventDays1.required = false;
            eventDays0.setCustomValidity("");
            eventDays1.setCustomValidity("");
        }
    };

    confirmation.onchange = function () {
        toggleDays(this.value === 'no');
    };

    [eventDays0, eventDays1].forEach((input) => {
        input.onchange = function () {
            if (eventDays0.checked || eventDays1.checked) {
                eventDays0.setCustomValidity("");
                eventDays1.setCustomValidity("");
            }
        };
    });

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch(form.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                successMessage.innerText = data.message;
                successMessage.style.display = "block";
                successMessage.style.opacity = "1";
                successMessage.style.visibility = "visible";

                form.reset();

                setTimeout(() => {
                    window.location.hash = "#schedule";
                    window.location.reload();
                }, 3000);
            } else {
                alert("Erro ao enviar: " + JSON.stringify(data.errors));
            }
        })
        .catch(error => console.error("Erro:", error));
    });

    function hideSuccessMessage() {
        if (successMessage && successMessage.style.display === "block") {
            setTimeout(() => {
                successMessage.style.transition = "opacity 0.5s ease";
                successMessage.style.opacity = "0";
                setTimeout(() => {
                    successMessage.style.display = "none";
                }, 500);
            }, 5000);
        }
    }

    hideSuccessMessage();
});