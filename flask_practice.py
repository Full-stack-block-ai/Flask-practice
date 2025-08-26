from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/thank_you/')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thank_you.html', first=first,last=last)



# @app.route('/dynamic/<name>')
# def dynamic(name):
#     if name.endswith('y'):
#         new_name = name[:-1] + 'iful'
#     else:
#         new_name = name + 'y'
    
#     return render_template('home.html', content=new_name)




if __name__ == '__main__':
    app.run(debug=True)