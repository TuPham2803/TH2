from flask import Flask, render_template
import dao

app = Flask(__name__)


@app.route('/')
def index():
    cates = dao.load_categories()
    products=dao.load_product()

    return render_template('index.html', msg=cates,product=products)


if __name__ == "__main__":
    app.run(debug=True)
