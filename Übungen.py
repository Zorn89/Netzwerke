from flask import Flask, request

app = Flask(__name__)





@app.route("/brand", methods=["GET"])
def get_brand_by_id():
    # Should return  welcome to specific brand page text
    # E.g. Welcome to Hilfigher (dynamisch)
    # Should be able to filter by brand type and should display the filter on the screen
    # E.g. Welcome to Hilfigher and the type is t-shirts
    # Should be able to filter by condition of the article and should display the condition on the screen
    # --> Goals E.g. Welcome to Hilfigher and the type is t-shirts and the condition is used
    # Get query parameters
    brand = request.args.get('brand', '')
    item_type = request.args.get('type', '')
    condition = request.args.get('condition', '')
    
    # Start the message
    message = f"Welcome to {brand.capitalize()}"
    
    # Add type if available
    if item_type:
        message += f" and the type is {item_type.lower()}"
    
    # Add condition if available
    if condition:
        message += f" and the condition is {condition.lower()}"
    
    # Return the final message
    return message
    


if __name__ == "__main__":
    app.run(debug=True, port=6060)


#/brand?brand=Hilfigher
#Response: Welcome to Hilfigher

#/brand?brand=Hilfigher&type=t-shirts
#Response: Welcome to Hilfigher and the type is t-shirts

#/brand?brand=Hilfigher&type=t-shirts&condition=used
#Response: Welcome to Hilfigher and the type is t-shirts and the condition is used