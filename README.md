# Warning
This site will reset March 14 @ 23:59 CET  
After the reboot the site will be permanent.


#### MyFamilyCart

Live at: https://myfamily.unialt.no  
  
Better instructions / readme will follow shortly.




#### Contribution

Clone the repo and have at it, manage.py has been altered to run settings.dev
configuration with a SQLite database.  
  
Feel free to use this code for education / courses / tutorials and or what ever you want. 
If you see something wrong or se a better solution for anything I would appreciate if you 
create an issue so we (especially me) can evolve and benefit from your input.  
  
No issue is to small, I want your input/ideas.


**Functionality**

Utilizing Django to handle users / auth / login while using "normal" views as JS endpoints. 

**Basic Overview**

* /templates/base.html
  * FontAwsome
  * Bootstrap 4 <-- Theme / JS
  * /static/js/VueNavbar.js <-- Vue component
  * /static/js/global.js <-- Global JS functions
  
 * /cart/templates/cart/cart-list.html
   * Carts overview
   * /cart/static/cart/js/cart-list.js <-- One page app
  
* /cart/templates/cart/cart-detail.html
   * Cart Items
   * /cart/static/cart/js/cart-detail.js <-- One page app
   
* /users <-- User functionality
  
