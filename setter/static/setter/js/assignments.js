
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
