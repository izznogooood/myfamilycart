// Remove Django messages after 3 sec
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const msg = document.querySelector('.django-message');
        if (msg) msg.remove();
    }, 3000);
});


