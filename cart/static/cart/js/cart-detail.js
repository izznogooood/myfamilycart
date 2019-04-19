// Get coockie value (Django csrftoken)
const getCookie = name => {
    let cookie = document.cookie.match("(^|;) ?" + name + "=([^;]*)(;|$)");
    return cookie ? cookie[2] : null;
};

// Dataclass
class Item {
    constructor(quantity, name) {
        this.quantity = quantity;
        this.name = name;
    }
}

class UI {
    static addItemToList(item) {
        if (document.querySelector("#empty")) {
            document.querySelector("#empty").remove();
            document.querySelector("table").innerHTML = nunjucks.render('views/todo-table.njk');
        }

        const tbody = document.querySelector("#item-list");
        const row = document.createElement("tr");
        row.innerHTML = nunjucks.render('views/todo.njk', {quantity: item.quantity, name: item.name});
        tbody.insertBefore(row, tbody.firstChild);
    }

    static deleteItem(el) {
        el.parentElement.parentElement.remove();
        const itemList = document.querySelector("#item-list");
        if (itemList && itemList.childElementCount === 0) {
            document.querySelector("thead").remove();
            document.querySelector("tbody").remove();

            const empty = document.createElement("p");
            empty.id = "empty";
            empty.classList.add("empty-state", "text-center");
            empty.innerHTML = "Your cart is empty...";
            document.querySelector("table").appendChild(empty);
        }
    }

    static showAlert(msg, className) {
        const div = document.createElement("div");
        div.className = `alert alert-${className}`;
        div.appendChild(document.createTextNode(msg));

        const nav = document.querySelector("#nav");
        nav.append(div);

        setTimeout(() => document.querySelector(".alert").remove(), 3000);
    }

    static clearFields() {
        document.querySelector("#quantity").value = "";
        document.querySelector("#name").value = "";
    }
}

class API {
    static createItem(item) {
        // Getting cart number from hidden <p> passed in by Django
        const cartNumber = document.querySelector("#cart-id").innerHTML;

        const data = new FormData();
        data.append("quantity", item.quantity);
        data.append("name", item.name);
        data.append("cart", cartNumber);

        fetch("../api/items/create", {
            method: "post",
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: data
        })
          .then(res => {
              return res.json();
          })
          .then(json => {
              UI.addItemToList(json);
              UI.clearFields();
              buttonEventListener();
          })
          .catch(err => {
              UI.showAlert(`Error: ${err}`, "danger");
              console.log(err);
          });
    }

    static delItem(item) {
        const cartNumber = document.querySelector("#cart-id").innerHTML;

        const data = new FormData();
        data.append("quantity", item.quantity);
        data.append("name", item.name);
        data.append("cart", cartNumber);

        fetch("../api/items/delete", {
            method: "post",
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: data
        }).catch(err => {
            UI.showAlert(`Error: ${err}`, "danger");
            console.log(err);
        });
    }
}

// Add item
document.querySelector("#cart-form").addEventListener("submit", e => {
    e.preventDefault();

    let quantity = document.querySelector("#quantity").value || 1;
    const name = document.querySelector("#name").value;

    if (!name) {
        UI.showAlert("Please enter an item...!", "danger");
    } else if (quantity <= 0) {
        UI.showAlert('You can not add negative values to list.', 'danger')
    } else {
        const item = new Item(quantity, name);
        API.createItem(item);
    }
});

// Remove item
const buttonEventListener = () => {
    document.querySelector("#item-list").addEventListener("click", e => {
        e.preventDefault();
        if (e.target.classList.contains("delete")) {
            let item = {
                quantity:
                e.target.parentElement.previousElementSibling
                  .previousElementSibling.innerHTML,
                name: e.target.parentElement.previousElementSibling.innerHTML
            };

            UI.deleteItem(e.target);
            API.delItem(item);
        }
    });
};

// Eventlistener (Remove item)
if (document.querySelector("#item-list")) {
    buttonEventListener();
}
