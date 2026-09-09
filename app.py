from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    restaurant_data = {
        "orders_today": 24,
        "sales_today": 842.75,
        "menu_items": 18,
        "pending_orders": 5
    }

    recent_orders = [
        {"id": "#1042", "customer": "Maya Johnson", "total": 42.50, "status": "Preparing"},
        {"id": "#1041", "customer": "Andre Williams", "total": 28.00, "status": "Ready"},
        {"id": "#1040", "customer": "Tasha Brown", "total": 63.25, "status": "Completed"}
    ]

    return render_template(
        "dashboard.html",
        data=restaurant_data,
        orders=recent_orders
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)