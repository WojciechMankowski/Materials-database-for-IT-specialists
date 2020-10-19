from flask import Flask, request, render_template
from Commands_Box.urls import Adding_to_database, Enter_the_categories, Enter_your_links
app = Flask(__name__)

@app.route('/')
def Home_page():
    list = Enter_the_categories()
    return render_template("index.html", list=list)

@app.route('/add', methods=['POST', 'GET'])
def Add_urls():
    list = Enter_the_categories()
    if request.method == 'POST':
        category = request.form['category']
        category2 = request.form['category2']
        url = request.form['url']
        print(type(category))
        # ca = category.lenght
        # ca2 = category2.lenght
        # ur = url.lenght
        # if ca != 0 and ca2 != 0 and ur != 0:
        #     print(ca)
        Adding_to_database(category, category2, url)
        return  render_template("Add.html", category=category2, list=list)
    return render_template("Add.html", list=list)

@app.route("/Kategorie", methods=['POST', 'GET'])
def See_categories():
    list = Enter_the_categories()
    if request.method == "POST":
        req = request.form
        category = req["items"]
        categors = Enter_your_links(category)
        return render_template("See.html", list=list,categors=categors )
    return render_template("See.html", list=list)

app.run(debug=True)
