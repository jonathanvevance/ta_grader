// Close (default) alert messages after 3 sec
const closeMessageButtons = document.getElementsByClassName("mssg-close-button");  // Return an array
setTimeout(function () {
    for (let i = 0; i < closeMessageButtons.length; ++i) {
        closeMessageButtons[i].click()
    }
}, 3000);

// Countdown timer for undo
const undoAssgDiv = document.getElementById("undo-assg-div");
const undoAssgProgressbar = document.getElementById("undo-assg-progressbar");
const undoAssgProgressDiv = document.getElementById("undo-assg-progress-div");
const undoAssgCloseButton = document.getElementById("undo-assg-close-button");

undoAssgCloseButton.addEventListener('click', function () {
    this.style.display = "none"
    undoAssgDiv.style.display = "none"
    undoAssgProgressDiv.style.display = "none"
})

// https://stackoverflow.com/a/50846458
ProgressCountdown(undoAssgProgressbar).then(value => function () {

    setTimeout(function () {
        undoAssgDiv.style.display = "none"
        undoAssgProgressDiv.style.display = "none"
        undoAssgCloseButton.style.display = "none"
    }, 500); // HACK: delay to handle poor handling of small width %ages
}());

function ProgressCountdown(progressbar) {

    let progressPercent = 0
    return new Promise((resolve, reject) => {
        var countdownTimer = setInterval(() => {

            progressPercent += 1
            progressbar.style.width = progressPercent + '%'
            progressbar.setAttribute('aria-valuenow', progressPercent)

            if (progressPercent >= 100) {
                clearInterval(countdownTimer);
                resolve(true);
            }
        }, 50);
    });
}