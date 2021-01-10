from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
	activelink = "menu-item-home current-menu-item page_item page-item-4 current_page_item"
	
	return render_template('index.html', activelink = activelink)

@app.route("/contact")
def contact():
    activelinkcontact = "menu-item-home current-menu-item page_item page-item-4 current_page_item"

    
    return render_template('contact.html', activelinkcontact = activelinkcontact)
    
@app.route("/search.html")
def search():

    return render_template('search.html')
    
@app.route("/blogs")
def blogpost():
	activelinkblog = "menu-item-home current-menu-item page_item page-item-4 current_page_item"
	
	return render_template('project.html', activelinkblog = activelinkblog)
    
@app.route("/about")
def about():
	activelinkabout = "menu-item-home current-menu-item page_item page-item-4 current_page_item"
	
	return render_template('about.html', activelinkabout = activelinkabout)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
    
app.run(debug=False)

    