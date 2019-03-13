
document.addEventListener('DOMContentLoaded', () => {

  // Remove Django messages after 3 sec
  setTimeout(() => {
      const msg = document.querySelector('.django-message');
      if (msg) msg.remove();
  }, 3000);

});


