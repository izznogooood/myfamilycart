const navBar = new Vue({

  el: '#nav',

  data() {
    return {
      display: false,
      cart: false
    }
  },

  methods: {
    toggleMenu() {
      this.display = !this.display;
    },
  },

  created() {
    // Looking for cart from hidden <p> passed in by Django
    const cart = document.querySelector('#cart-id');
    if (cart) {this.cart = true}
    },
});

