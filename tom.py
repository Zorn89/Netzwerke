from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome Mamazon"


@app.route("/item/<product_id>", methods=["GET"])
def get_item(product_id):
    color = request.args.get("color")  # /item/2?color=black
    size = request.args.get("size")  # /item/2?size=M
    # /item/2?color=black&size=M
    return f"Welcome Mamazon's item {product_id} with the color {color} an with the size {size}"


@app.route("/brand", methods=["GET"])
def get_mamazon_default_brand_page():
    # Should return a welcome to brand page text
    return "Welcome to brand page"


@app.route("/brand/<brand_id>", methods=["GET"])
def get_brand_by_id(brand_id):
    # Should return  welcome to specific brand page text
    # E.g. Welcome to Hilfigher (dynamisch)
    # Should be able to filter by brand type and should display the filter on the screen

    brand_type = request.args.get("type")
    # E.g. Welcome to Hilfigher and the type is t-shirts
    # Should be able to filter by condition of the article and should display the condition on the screen
    # --> Goals E.g. Welcome to Hilfigher and the type is t-shirts and the condition is used
    condition = request.args.get("condition")
    return (
        f"My Brand id is:{brand_id}, type: {brand_type} and the condition: {condition}"
    )


if __name__ == "__main__":
    app.run(debug=True, port=6060)