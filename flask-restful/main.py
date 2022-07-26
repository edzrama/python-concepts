from flask import Flask, render_template, request, make_response, jsonify, url_for, redirect, abort

app = Flask(__name__)

orders = {
    "order1": {
        "size": "small",
        "toppings": "cheese",
        "crust": "thin"
    },
    "order2": {
        "size": "medium",
        "toppings": "cheese",
        "crust": "thick"
    },
    "order3": {
        "size": "large",
        "toppings": "double cheese",
        "crust": "thin"
    },
}


@app.route('/')
def test():
    return render_template("index.html")


# no method argument is automatically considered as get
@app.route('/query')
def query():
    print(request.method)
    if request.args:
        req = request.args
        return " ".join(f"{k}:{v}<br>" for k, v in req.items())
    return "no query"


@app.route('/post', methods=['POST'])
def post():
    print(request.method)
    if request.form:
        name = request.form['name']
        last_name = request.form['lName']
        return f"name: {name}<br> lastname: {last_name}"
    return "no passed value(s)"


@app.route('/orders')
def get_orders():
    return make_response(jsonify(orders), 200)


@app.route('/test/<user>')
def test_redirect(user):
    if user == "admin":
        return redirect(url_for('admin'))
    abort(401)


@app.route('/admin')
def admin():
    return "<h1> This is the admin page</h1>"


@app.route('/order/<order_id>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def get_order(order_id):
    print(request.method)
    if request.method == "GET":
        if order_id in orders:
            return make_response(jsonify(orders[order_id]), 200)
        else:
            return make_response('"message": "order not found"', 404)
    if request.method == "POST":
        req = request.get_json()
        if order_id in orders:
            return make_response('"message": "order already exists"', 404)
        orders.update({order_id: req})
        return make_response(f'"message": "New Order {order_id} Added', 201)
    if request.method == "PUT":
        req = request.get_json()
        if order_id not in orders:
            return make_response('"message": "order not found"', 404)
        orders[order_id] = req
        return make_response(f'"message": "order {order_id} updated"', 201)
    if request.method == "PATCH":
        req = request.get_json()
        if order_id not in orders:
            return make_response('"message": "order not found"', 404)
        for key, val in req.items():
            orders[order_id][key] = val
        return make_response(f'"message": "order {order_id} patched"', 201)
    if request.method == "DELETE":
        if order_id not in orders:
            return make_response('"message": "order not found"', 404)
        del orders[order_id]
            # 204 explicitly mean no response body
        return make_response(f'"message": "order {order_id} deleted"', 200)


@app.errorhandler(404)
def server_error(error):
    return "<h1>Page not found</h1>"

if __name__ == "__main__":
    app.run(debug=True)
