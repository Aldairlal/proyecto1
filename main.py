from flask import Flask, render_template

app = Flask(_name_)

# Ruta para la página principal
@app.route('/')
def tienda():
    return render_template('tienda.html')

if _name_ == '_main_':
    app.run(debug=True)