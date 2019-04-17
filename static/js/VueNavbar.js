const navBar = new Vue({
    el: '#nav',
    data() {
        return {
            display: false,
            cart: false,
        }
    },
    methods: {
        toggleMenu() {
            this.display = !this.display;
        },
    },
    created() {
        // Looking for cart id and shared status from hidden <p> passed in by Django
        const cart = document.querySelector('#cart-id');
        const shared = document.querySelector('#shared');

        if (cart && !shared) {
            this.cart = true
        }
    },
});

