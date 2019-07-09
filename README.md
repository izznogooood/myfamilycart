<!--
Todo: 
 * Does not work without JS: https://kryogenix.org/code/browser/everyonehasjs.html
 * Can add the same item to a list twice, does not update the quantity but instead just adds it again
-->

## MyFamilyCart
Protected by [Guardrails](https://www.guardrails.io/en).

![Models](doc/demo.png)


Live at: https://myfamily.unialt.no (Mobile First)
  
### About

MyFamilyCart came to life as our family needed a common
place to save and share our shopping lists. The App lets you create different
shopping carts (lists) where you can add and remove items.  

Key features:
 * Shopping lists
 * Share lists with other users
  
If you want to know more check out the [About Page](https://myfamily.unialt.no/about)

### Roadmap

The app is fulfilling it's purpose and we are using it daily. I've started integrating
django channels to make use of websockets.

This will make the app more responsive with more realtime features and allow for realtime
edits/actions on items and more. Please add issues if you have wishes.

Planned features:

* Inline editing of items
* Items can be "clickable" (links)
* Predictions will be cart related (Apple will not be suggested in IKEA cart)
* Todolist with recurring tasks
* *maybe: Full blown callender function*

### Contribute

This projects main platform / framework is [Django](https://www.djangoproject.com/) 
with quite a bit of plain JavaScript (ES6), [Nunjucks](https://mozilla.github.io/nunjucks/) templating
(need compiling) and a sprinkle of [Vue.js](https://vuejs.org/) along with
[Bootstrap 4](https://getbootstrap.com/) (themed).
  
If you are familiar with Django just clone the repo and have at it. `manage.py` has been 
altered to run `settings.dev` configuration with a SQLite database.  
  
Feel free to use this code for education / courses / tutorials and or what ever you want. 
If you see something wrong or se a better solution for anything I would appreciate if you 
create an issue so we (especially me) can evolve and benefit from your input.  
  
No issue is to small, I want your input/ideas.

**Functionality**

Utilizing Django to handle users / auth / login / backend tasks while JS onePage
apps take advantage of basic Django views as API endpoints.

**Very Basic Overview**

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

* /static/js/nunjucks/templates/ <-- Nunjucks (JS) templates

**Django Models / Database Tables**  
  
![Models](doc/models.png)
  


