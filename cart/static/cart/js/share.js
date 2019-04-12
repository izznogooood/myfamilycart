// Simple bootstrap spinner
const spinner = `
                <div class="spinner-border" role="status">
                <span class="sr-only">Loading...</span>
                </div>`;

// Inserting text between the fields of the Django Form. ( OR )
const legend = document.createElement("legend");
legend.innerHTML = "OR";
legend.classList.add("mt-4", "text-muted", "display-4");
document.querySelector("#id_username").parentElement.append(legend);

// Start spinner while waiting for Django (todo: add async mail method)
document.querySelector("#submit").addEventListener("click", function() {
    this.innerHTML = spinner;
    document.share.submit();
});
