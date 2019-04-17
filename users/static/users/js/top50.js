// Single word removal from Top50

const showAlert = (msg, className) => {
    const div = document.createElement("div");
    div.className = `alert alert-${className} text-center`;
    div.appendChild(document.createTextNode(msg));

    const nav = document.querySelector("#nav");
    nav.append(div);

    setTimeout(() => document.querySelector(".alert").remove(), 3000);
};

// Dataclass
class Item {
    constructor(id, element) {
        this.id = id;
        this.element /** @type {HTMLCanvasElement} */ = element;
    }

    removeElement() {
        this.element.remove();
    }
}

class API {
    static rmItem(item) {
        fetch(`./delete/${item.id}`)
          .then(res => res.json())
          .then(json => {
              if (json["success"] === "true") {
                  item.removeElement();
              } else {
                  showAlert(
                    "There was a problem removing your item!",
                    "danger"
                  );
              }
          })
          .catch(err => {
              console.log(err);
              showAlert(err, "danger");
          });
    }
}

// Deleting single words .
document.addEventListener("DOMContentLoaded", () => {
    const itemList /** @type {HTMLCanvasElement} */ = document.querySelector(
      "#item-list"
    );
    if (itemList) {
        itemList.addEventListener("click", e => {
            e.preventDefault();

            const target /** @type {HTMLCanvasElement} */ = e.target;

            if (target.classList.contains("delete")) {
                const itemID =
                  target.parentElement.previousElementSibling
                    .previousElementSibling.previousElementSibling
                    .innerHTML;
                const tableRowElement = target.parentElement.parentElement;

                const item = new Item(itemID, tableRowElement);

                API.rmItem(item);
            }
        });
    }
});
