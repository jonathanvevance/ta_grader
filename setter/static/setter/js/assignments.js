
// Styling (Discord-like) for rename buttons
const renameButtons = document.getElementsByClassName("rename-button-js");

for (let i = 0; i < renameButtons.length; ++i) {
    renameButtons[i].addEventListener("mouseover", function () {
        let renameIcon = renameButtons[i].getElementsByClassName("rename-icon-js")[0]
        if (!(renameIcon.classList.contains("max-white-hover"))) {
            let titleElement = renameButtons[i].parentElement.getElementsByClassName("assignment-title-js")[0]
            titleElement.classList.add("mid-white")
        }
    })

    renameButtons[i].addEventListener("mouseout", function () {
        let renameIcon = renameButtons[i].getElementsByClassName("rename-icon-js")[0]
        if (!(renameIcon.classList.contains("max-white-hover"))) {
            let titleElement = renameButtons[i].parentElement.getElementsByClassName("assignment-title-js")[0]
            titleElement.classList.remove("mid-white")
        }
    })
}

// Countdown timer for undo
const undoAssgDiv = document.getElementById("undo-assg-div");
const undoAssgCloseButton = document.getElementById("undo-assg-close-button");
const undoAssgProgressbar = document.getElementById("undo-assg-progressbar");
const undoAssgProgressDiv = document.getElementById("undo-assg-progress-div");

// https://stackoverflow.com/a/50846458
ProgressCountdown(undoAssgProgressbar).then(value => function () {

    setTimeout(function () {
        undoAssgDiv.style.display = "none"
        undoAssgProgressDiv.style.display = "none"
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