from flask import Flask
app = Flask(__name__)
books=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
@app.route("/api/books")
def index():
    return {"data" : books}
if __name__ == '__main__':
    app.run(debug=True)
