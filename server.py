from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = 'coding dojo is awesome'

def incrementar(counter = 1):
    if 'clickCounter' in session:
        session['clickCounter'] = int(session['clickCounter']) + counter
    else:
        session['clickCounter'] = 1

@app.route( '/', methods=['GET'] )
def count():
    if 'refreshCounter' in session:
        session['refreshCounter'] = int(session['refreshCounter']) + 1
    else:
        session['refreshCounter'] = 1

    if not 'clickCounter' in session:
        session['clickCounter'] = 0

    return render_template( "show.html", refreshCounter = session['refreshCounter'], clickCounter = session['clickCounter'])

@app.route( '/count2', methods=['GET'] )
def count2():
    incrementar(2)
    return redirect('/')

@app.route( '/destroy_session', methods=['GET'] )
def destroy():
    session.pop('clickCounter')
    return redirect('/')

@app.route( '/sensei', methods=['POST'] )
def sensei():
    incrementarSensei = int(request.form['inputContador'])
    incrementar(incrementarSensei)
    return redirect('/')

if __name__ == "__main__":
    app.run( debug = True )