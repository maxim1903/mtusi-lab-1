from flask import Flask, render_template, request

app = Flask(__name__)
posts=[]

@app.route('/')
@app.route('/index', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        posts.append({"message": request.form.get("text")})
    return render_template("index.html", posts=posts )

app.run ()