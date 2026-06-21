from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy recipes stored in dictionary
recipes = {
    "maggi": "Boil water → add noodles → add tastemaker → cook 2 minutes.",
    "tea": "Boil water → add tea powder → add milk & sugar → strain & serve.",
    "coffee": "Boil milk → add coffee powder → add sugar & mix well.",
    "bread omelette": "Beat eggs → pour on pan → place bread → fold & serve.",
    "chicken biryani": "Wash rice & soak 15 mins → Fry spices & onions → Add ginger garlic paste → Add chicken & spices → Add curd & tomatoes → Add water → Add rice → Cook 15 mins on low flame."
}



@app.route("/", methods=["GET", "POST"])
def home():
    recipe_result = ""  # default (empty)
    
    if request.method == "POST":
        dish = request.form.get("dish", "").lower()
        recipe_result = recipes.get(dish, "❌ Recipe not found!")

    return render_template("index.html", recipe_result=recipe_result)

if __name__ == "__main__":
    app.run(debug=True)
