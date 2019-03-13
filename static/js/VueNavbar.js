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
      const cart = document.querySelector('#cart-id');
      if (cart) {this.cart = true}
    },
});

