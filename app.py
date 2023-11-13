from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "mWm5SVTZlmYO03nr1RHi76NbORYOY64Z"

products = {
    "001": {
        "name": "Double-sided coat with buttons",
        "price": 119.00,
        "description": "Double-sided design. Short design. Lapel-collar V-neck collar. Long sleeve. Two front pockets. Front button closure.",
        "image": "http://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57087709_09_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "women"
    },
    "002": {
        "name": "Slim fit stretch cotton shirt",
        "price": 49.00,
        "description": "Performance Collection. Slim fit. Slightly elastic cotton fabric. Classic collar. Long sleeve with buttoned cuffs. Front button closure. Rounded hem. Easy iron. Comfort Stretch: Stretch fabric for added comfort. Performance is a selection of garments made of technical fibers that will keep you intact, and most of all, comfy all day long, whatever you do, wherever you go. Our performance selection includes a wide range of advanced features as bi-stretch, quick-dry, easy-iron, thermoregulator, breathable or water-repellent fabrics arranged in four general categories: Thermoregulator, Functional, Easy-care and Comfort.",
        "image": "https://img.fruugo.com/product/8/23/617162238_max.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "003": {
        "name": "Shearling denim bomber jacket",
        "price": 149.00,
        "description": "Denim style cotton fabric. Bomber design. Oversize design. Shirt-style collar. Faux shearling collar. Removable fur collar. Long sleeve. Two patch pockets on the front. Button fastening on the front section. Hem with elastic band. Inner lining.",
        "image": "https://outdazl.com/cdn/shop/files/free-people-ariel-cozy-denim-bomber-jacket-outdazl-1.png?v=1693476813",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "women"
    },
    "004": {
        "name": "Printed long sleeve t-shirt",
        "price": 39.00,
        "description": "Straight design. Print. Rounded neck. Long sleeve.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57027731_69_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "kids"
    },
    "005": {
        "name": "Handmade recycled wool coat",
        "price": 199.00,
        "description": "Recycled wool mix fabric. Regular fit. Lapel-collar. Inside flap in checkered pattern. Front button closure. Long sleeve. Back-slit hem. Partial lining.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57047705_92_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "006": {
        "name": "Leather jacket with worn effect",
        "price": 239.00,
        "description": "100% nappa leather. Straight design. Shirt-style collar. Front snap button closure. Two patch pockets with flaps on the chest. Two front pockets.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57095947_30_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "007": {
        "name": "Regular-fit kids jeans",
        "price": 19.00,
        "description": "Regular fit. Regular fit. Medium waist. Five pockets. Zip and one button fastening. Back to school.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57002520_TN_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "kids"
    },
    "008": {
        "name": "Regular fit check cotton kids shirt",
        "price": 19.00,
        "description": "Straight design. Shirt-style collar. Front closure. Long sleeve. Button up.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57037721_05_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "kids"
    },
    "009": {
        "name": "Knot printed skirt",
        "price": 46.00,
        "description": "Flowy fabric. Midi design. Printed design. Back closure. Side slit. Knot detail. Office looks.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57097725_52_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "women"
    },
    "010": {
        "name": "Embroidered detail cotton sweatshirt",
        "price": 46.00,
        "description": "Cotton-blend fabric. Slim fit. Embroidered drawing on the chest. Rounded neck. Long sleeve with elastic cuffs. Straight hem.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57077748_02_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "011": {
        "name": "Printed long dress",
        "price": 29.00,
        "description": "100% recycled polyester. Flowy fabric. Midi design. Evasé design. Printed design. Rounded neck. Long sleeve with elastic cuffs. Puffed sleeves. Plus Size Available.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57057734_99_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "women"
    },
    "012": {
        "name": "Velveteen suit trousers",
        "price": 29.00,
        "description": "Velveton fabric. Long design. Flare design. Medium waist. Two side pockets. Two patch pockets on the back. Zip and hook fastening. Inner lining. Co-ord.",
        "image": "https://www.pngkey.com/png/full/219-2192359_h-frost-green-bow-01-mens-shirt-in.png",
        "sizes": ["4", "6", "8", "10", "12", "14", "16", "18"],
        "stock": 100,
        "gender": "women"
    },
    "013": {
        "name": "Cotton jogger-style kids trousers",
        "price": 19.00,
        "description": "Jogger design. Elastic band. Long design. Medium. Brushed fabric.",
        "image": "http://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57086725_56_B.jpg",
        "sizes": ["6y", "7y", "8y", "9y", "10y", "11y", "12y", "13-14y"],
        "stock": 100,
        "gender": "kids"
    },
    "014": {
        "name": "100% cashmere knitted polo shirt",
        "price": 149.00,
        "description": "Polo shirt made of 100% cashmere wool from the island of Mongolia. As a result, the fabric is soft to the touch, lightweight and a very good thermal insulator, fine knit fabric, straight design, v-neck polo collar without closure, long sleeve, straight hem, ribbed finishes on the collar",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57057898_06_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "015": {
        "name": "Check wool-blend overshirt",
        "price": 59.00,
        "description": "Regular fit. Standard design.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57037711_08_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "016": {
        "name": "Oversize knit sweater",
        "price": 49.00,
        "description": "Medium knit. Long design. Oversize design. Rounded neck. Long sleeve. Cable knit finish. Co-ord.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57044412_05_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "women"
    },
    "017": {
        "name": "Long Snoopy kids pyjama",
        "price": 23.00,
        "description": "T-shirt and pyjama trousers pack. Snoopy design. Long design. Printed message. Elastic waist. Rounded neck. Long sleeve. Licenses.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57059090_02_B.jpg",
        "sizes": ["5-6y", "7-8y", "9-10y", "11-12y", "13-14y"],
        "stock": 100,
        "gender": "kids"
    },
    "018": {
        "name": "Cotton pyjama shorts pack",
        "price": 29.00,
        "description": "T-shirt and pyjama trousers pack. 100% cotton fabric. Includes a bag to store. T-shirt. Rounded neck. 100% cotton shorts. Elastic waist with adjustable drawstring. Two side pockets. With this cotton garment you support our investment in the mission of Better Cotton. This fabric is a mass balance that replaces or blends Better Cotton with conventional cotton, so it may not contain Better Cotton. Partner farmers receive ongoing support and training.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T4/fotos/S20/47065959_01_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "019": {
        "name": "Printed cotton kids sweatshirt",
        "price": 19.00,
        "description": "Brushed fabric. Cotton fabric. Print. Straight design. Hood. Long sleeve. Unclosed.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57065993_02_B.jpg",
        "sizes": ["5-6y", "7-8y", "9-10y", "11-12y", "13-14y"],
        "stock": 100,
        "gender": "kids"
    },
    "020": {
        "name": "Fitted suit jacket",
        "price": 49.00,
        "description": "Straight design. Tailored design. Lapel-collar V-neck collar. Lapel with notch. Long sleeve. Structured shoulders. Two welt pockets on the front. Dart detail. Back slit. Inner lining. Co-ord. Blazer style. Plus Size Available. Party and events collection. College. Office looks.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57040365_69_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "women"
    },
    "021": {
        "name": "Crewneck lurex ",
        "price": 46.00,
        "description": "Fine knit fabric. Cable knit fabric. Lurex fabric. Straight design. Rounded neck. Long sleeve. Openwork details. Co-ord. Party and events collection.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57007776_65_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "women"
    },
    "022": {
        "name": "Stretch fabric slim-fit printed suit trousers",
        "price": 59.00,
        "description": "Slim fit. Fabric made of recycled polyester, a durable, breathable, easy-care fiber that provides comfort in use. Comfort Stretch: Stretch fabric for added comfort. Prince of Wales check print. Medium waist. Detail of front and rear calipers. Concealed button, hook and zip fastening. Belt loops. Two side pockets. Coin pocket at hip height. Two welt pockets on the back. Slightly close-fitting, the Slim-Fit suit is a little closer to the body than the Regular Fit. Ideal for those who ask for a plus to the classic-cut suit, without marking a very fitted silhouette. The Slim-Fit suit comes in different models: double-breasted, linen, wool and classic. Combine it with a sweater or t-shirt if you want to give it a more casual look or with the classic shirt and tie for special occasions",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57040676_69_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "023": {
        "name": "Knitted turtleneck dress",
        "price": 69.00,
        "description": "Wool mix fabric, thick knitted fabric, straight design, long design, striped print, rolled neck, long sleeve, unclosed, plus Size Available.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57079101_95_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "women"
    },
    "024": {
        "name": "Braided wool-blend sweater",
        "price": 59.00,
        "description": "Fabric made of polyester and wool. Slim fit. Braided design. Rounded neck. Long sleeve with elastic cuffs. Straight hem. Ribbed finishes on the collar, sleeve and bottom. Plus Size Available. Party and events collection. College. Office looks.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57017724_02_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "025": {
        "name": "Printed long sleeve t-shirt",
        "price": 19.00,
        "description": "Straight design. Image printed on the front. Decorative pompoms. Rounded neck. Long sleeve.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57004027_02_B.jpg",
        "sizes": ["5-6y", "7-8y", "9-10y", "11-12y", "13-14y"],
        "stock": 100,
        "gender": "kids"
    },
    "026": {
        "name": "Wrapped satin dress",
        "price": 39.00,
        "description": "Flowy fabric. Short design. Crossover design. Evasé design. V-neck. Long sleeve with elastic cuffs. Ribbon on the waist with tie closure. Inner lining.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57097726_PL_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "women"
    },
    "027": {
        "name": "Leopard print sweater",
        "price": 26.00,
        "description": "Viscose fabric. Leopard print. Straight design. Fine knit fabric. Long sleeve. Rounded neck.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57034758_07_B.jpg",
        "sizes": ["5-6y", "7-8y", "9-10y", "11-12y", "13-14y"],
        "stock": 100,
        "gender": "kids"
    },
    "028": {
        "name": "Striped cotton long kids pyjama",
        "price": 23.00,
        "description": "Striped print, straight design, long design, rounded neck, long sleeve, cord fastening.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57078270_69_D0.jpg",
        "sizes": ["5-6y", "7-8y", "9-10y", "11-12y", "13-14y"],
        "stock": 100,
        "gender": "kids"
    },
    "029": {
        "name": "Fine modal-silk sweater",
        "price": 59.00,
        "description": "ESSENTIALS: Made to last. Regular fit. Modal and silk mix. Fine knit fabric. Flecked design. Rounded neck. Long sleeve. Straight hem. Ribbed finishes on the collar, sleeve and .",
        "image": "https://st.mngbcn.com/rcs/pics/static/T5/fotos/S20/57065956_30_B.jpg",
        "sizes": ["S", "M", "L", "XL"],
        "stock": 100,
        "gender": "men"
    },
    "030": {
        "name": "Cotton denim shorts",
        "price": 29.00,
        "description": "Fabric with cotton. Denim fabric. Straight design. Short design. Five pockets. Zip and one button fastening. With this cotton garment you support our investment in the mission of Better Cotton. This fabric is a mass balance that replaces or blends Better Cotton with conventional cotton, so it may not contain Better Cotton. Partner farmers receive ongoing support and training.",
        "image": "https://st.mngbcn.com/rcs/pics/static/T4/fotos/S20/47055941_TG_B.jpg",
        "sizes": ["6y", "7y", "8y", "9y", "10y", "11y", "12y", "13-14y"],
        "stock": 100,
        "gender": "kids"
    }
}

cart = {}

admin_username = "admin"
admin_password = "admin"

# Opening homepage
@app.route("/")
def home():
    return render_template("home.html")

#Display all products
@app.route("/store")
def store():
    return render_template("allProducts.html", products=products)

@app.route("/item/<sku>")
def item(sku):
    return render_template("item.html", product=products[sku], sku=sku)

@app.route("/add_to_cart/<sku>", methods=["POST"])
def add_to_cart(sku):
    chosen_size = request.form['size']
    if sku in products:
        if (sku in cart):
            cart[sku]["quantity"] += 1
        else:
            cart[sku] = {'name': products[sku]['name'], 'price': products[sku]['price'], 'image': products[sku]['image'], 'size': chosen_size, 'quantity': 1}
    products[sku]['stock'] -= 1
    return redirect(url_for("item", sku=sku))

# Displayng products by gender
@app.route("/products/<gender>")
def products_by_gender(gender):
    gendered_products = []
    for sku, item in products.items():
        if (item["gender"] == gender):
            gendered_products.append((sku, item))
    return render_template("products.html", gproducts=gendered_products, gender=gender)

# Displaying the cart
@app.route("/cart")
def view_cart():
    if not cart:
        cart_empty = True
    else:
        cart_empty = False
    return render_template("cart.html", cart_products=cart, cart_empty=cart_empty)

@app.route("/remove_from_cart/<sku>", methods=["POST"])
def remove_from_cart(sku):
    if sku in cart:
        products[sku]['stock'] += cart[sku]['quantity']
        del cart[sku]
    return redirect(url_for("view_cart"))

#Order items from cart
@app.route("/order", methods=["POST"])
def order():
    cart.clear()
    return redirect(url_for("success"))

# You can define a separate route for the success page
@app.route("/success")
def success():
    return render_template("success.html")


#Creating a login page
@app.route("/account")
def login():
    return render_template("login.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    username = request.form["username"]
    password = request.form["password"]

    if username == admin_username and password == admin_password:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

@app.route("/dashboard")
def dashboard():
    if 'username' in session:
        return render_template("admin.html", products=products)
    else:
        return redirect(url_for('login'))

@app.route('/add_product', methods=['POST'])
def add_product():
    if 'username' in session:
        sku = request.form['sku']
        name = request.form['name']
        price = float(request.form['price'])
        description = request.form['description']
        gender = request.form['gender']
        image = request.form['image']
        products[sku] = {'name': name, 'price': price, 'description': description, 'gender': gender, 'image': image}
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login.html'))

@app.route('/update_product/<sku>', methods=['POST'])
def update_product(sku):
    if 'username' in session:
        if sku in products:
            product = products[sku]
            product['price'] = float(request.form['price'])
            # You can update other attributes here if needed
            return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('index'))

#Delete item on the Admin page
@app.route('/delete_product/<sku>', methods=['POST'])
def delete_product(sku):
    if 'username' in session:
        if sku in products:
            del products[sku]
            return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True, port=8080)