
function getCookie(name) {

    let cookie = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return cookie ? cookie[2] : null;
}

class Item {

    constructor(name, id = null, url = null) {
        this.name = name;
        this.id = id;
        this.url = url;
    }
}

class UI {

    static addItemToList(item) {
        const empty = document.querySelector('#empty');
        if (empty) empty.remove();

        const div = document.querySelector('#cart-list');
        const url = new URL(document.URL);

        const aButton = document.createElement('a');
        aButton.classList.add('btn', 'btn-primary', 'btn-block', 'mt-4', 'font-weight-bold');
        aButton.href = url.origin + item.url;
        aButton.innerHTML = item.name;

        div.appendChild(aButton);
    }
    
    static showAlert(msg, className) {
        const div = document.createElement('div');
        div.className = `alert alert-${className}`;
        div.appendChild(document.createTextNode(msg));

        const nav = document.querySelector('#nav');
        nav.append(div);

        setTimeout(() => document.querySelector('.alert').remove(), 3000)
    }

    static clearFields() {
        document.querySelector('#cart-name').value = '';
    }
}

class API {

    static createItem(item) {
        const data = new FormData();
        data.append('name', item.name);

        fetch('api/carts/create', {
            method: 'post',
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: data
        })
            .then(res => {return res.json()})
            .then(json => {
                UI.addItemToList(json);
                UI.showAlert('Cart added...', 'success');
                UI.clearFields();
            })
            .catch(err => {
                UI.showAlert(`Error: ${err}`, 'danger');
                console.log(err)
            });
    }
}

// Add Item
document.querySelector('#cart-form').addEventListener('submit', e => {
    e.preventDefault();

    const name = document.querySelector('#cart-name').value;

    if (!name) {
        UI.showAlert('Please enter an item...!', 'danger')
    }

    const item = new Item(name);

    API.createItem(item);
        
});




