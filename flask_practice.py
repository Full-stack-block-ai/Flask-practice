from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template('home.html')

# @app.route('/signup/')
# def signup():
#     return render_template('signup.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    upper = False
    lower = False
    end_in_num = False

    if any(char.isupper() for char in username):
        upper = True
    if any(char.islower() for char in username):
        lower = True
    if username[-1].isdigit():
        end_in_num = True

    report = upper and lower and end_in_num

    return render_template('report.html', username=username, upper=upper, lower=lower,end_in_num=end_in_num, report=report)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



# @app.route('/dynamic/<name>')
# def dynamic(name):
#     if name.endswith('y'):
#         new_name = name[:-1] + 'iful'
#     else:
#         new_name = name + 'y'
    
#     return render_template('home.html', content=new_name)




if __name__ == '__main__':
    app.run(debug=False)