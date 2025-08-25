from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    my_list = ['apples', 'pears', 'bananas']
    return render_template('home.html', my_list = my_list)

# @app.route('/dynamic/<name>')
# def dynamic(name):
#     if name.endswith('y'):
#         new_name = name[:-1] + 'iful'
#     else:
#         new_name = name + 'y'
    
#     return render_template('home.html', content=new_name)




if __name__ == '__main__':
    app.run(debug=True)