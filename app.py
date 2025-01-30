from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('inicial.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')  

@app.route('/eventos')
def eventos():
    return render_template('eventos.html') 

@app.route('/contato')
def contatos():
    return render_template('contatos.html')  

@app.route('/sou_novo')
def sou_novo():
    return render_template('sou_novo.html')

if __name__ == '__main__':
    app.run(debug=True)