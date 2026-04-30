# ZenPlus Shop Integration Guide

This document outlines the exact steps to integrate the standalone `index.html` shop page into the main ZenPlus Flask project. 

## 1. File Placement

The main project uses a typical Flask structure (`app.py`, `templates/`, `static/`).

1. **Move the HTML File**: 
   Rename `index.html` to `shop.html` and place it inside the `templates/` folder of the main project.
   ```
   zenplus/
   ├── templates/
   │   └── shop.html   <-- Place it here
   ```

2. **Move the Assets**: 
   Move the entire `assets/` folder (containing the product images) into the `static/` folder of the main project.
   ```
   zenplus/
   ├── static/
   │   └── assets/     <-- Place images here
   ```

## 2. Setting Up the Route in Flask (`app.py`)

Open `app.py` in the main project and add a new route for the shop. You can place this near your other routes (e.g., after the `/diet` route).

```python
@app.route("/shop")
@login_required
def shop():
    """Display the ZenPlus Shopping Page"""
    return render_template("shop.html")
```

## 3. Updating Links and Asset Paths

### In `templates/shop.html`

Flask uses `url_for()` to safely generate URLs for static files. While standard relative paths (`assets/image.png`) might work depending on the URL structure, the robust Flask way is to update them.

Find the `productData` object in the script tag at the bottom of `shop.html`.
Update the `image` paths from:
```javascript
image: 'assets/l-carnitine.png'
```
to use Flask static paths:
```javascript
image: '{{ url_for("static", filename="assets/l-carnitine.png") }}'
```

*Note: Since the script is inside `shop.html`, Jinja templating (`{{ url_for(...) }}`) will process correctly when Flask renders the template.*

### In `templates/layout.html`

To make the shop accessible from the main navigation bar, open `layout.html` and add a link to the `nav-pills` list.

```html
<!-- Inside <ul class="nav nav-pills"> -->
<li class="nav-item"><a href="{{ url_for('shop') }}" class="nav-link">Shop</a></li>
```

## 4. Preserving the Cart (Shared State)

Currently, the `cart` array in the shop resets if you navigate away. To give it a real e-commerce feel across the ZenPlus site, use `localStorage`.

**In `shop.html`, update the cart logic:**

1. **When the shop loads, retrieve the cart:**
Replace `let cart = [];` with:
```javascript
let cart = JSON.parse(localStorage.getItem('zenplus_cart')) || [];
```

2. **When adding/updating items, save to localStorage:**
```javascript
function saveCart() {
    localStorage.setItem('zenpulse_cart', JSON.stringify(cart));
}
```
*Make sure to call `saveCart()` at the end of `addToCart()`, `updateQuantity()`, and `clearCart()`.*

## 5. Connecting Main Site Goals to the Shop

If a user selects "Muscle Gain" on another page, you can pass this goal via a query parameter when linking to the shop:

```html
<a href="{{ url_for('shop', goal='Muscle Gain') }}">Go to Shop for Muscle Gain</a>
```

Then, in `shop.html`, read the parameter on load:
```javascript
const urlParams = new URLSearchParams(window.location.search);
const goalParam = urlParams.get('goal');

if (goalParam) {
    setGoal(goalParam);
} else {
    setGoal('Weight Loss'); // Default
}
```

## 6. Presentation Highlights

When demonstrating the shop, emphasize:
- **Clean Theme Integration**: The shop UI matches the main site's Bootstrap aesthetic (white cards, blue primary buttons, light gradients).
- **Client-Side Rendering**: Products load instantly without a backend delay.
- **Cart Persistence**: Adding items and navigating away won't lose the cart if `localStorage` is implemented.
