from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home/index.html")


@app.route("/dashboard")
def dashboard():
    restaurant_data = {
        "orders_today": 24,
        "sales_today": 842.75,
        "menu_items": 18,
        "pending_orders": 5
    }

    recent_orders = []

    return render_template(
        "dashboard.html",
        data=restaurant_data,
        orders=recent_orders
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)