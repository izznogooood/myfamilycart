// Inserting text between the fields of the Django Form. ( OR )
const legend = document.createElement("legend");
legend.innerHTML = "OR";
legend.classList.add("mt-4", "text-muted", "display-4");
document.querySelector("#id_username").parentElement.append(legend);

// Start spinner while waiting for Django (async mail coming in Vue version)
document.querySelector("#submit").addEventListener("click", function () {
    this.innerHTML = nunjucks.render('spinner.njk');
    document.share.submit();
});
