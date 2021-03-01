import Queries
from flask import Flask, render_template, request

main_options = ['Stock Time Series', 'Fundamental Data']
stock_options = ['Intraday', 'Daily', 'Weekly', 'Monthly']
fundamental_options = ['Company Overview', 'Balance Sheet Annual', 'Cash Flow Annual', 'Income Statement Annual']

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pages=main_options)


@app.route('/submit', methods=['POST'])
def submit():
    if main_options == 'Stock Time Series':
        return render_template("stock.html", ts_options=stock_options)
    elif main_options == 'Fundamental Data':
        return render_template("fund.html", fd_options=fundamental_options)
    else:
        return render_template('index.html', message='Please enter required fields!', pages=main_options)


# @app.route('/submit', methods=['POST'])
# def submit():
#     # fd_options = request.form['fd_options']
#     return render_template("fund.html", fd_options=fundamental_options)

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         query = request.form['query']
#         st_options = request.form['st_options']
#         fd_options = request.form['fd_options']
#         if query == '' or st_options == '':
#             return render_template('index.html', message='Please enter required fields!')
#         #     return render_template('success.html')
#         return render_template('index.html', message='You have already submitted feedback!')


if __name__ == '__main__':
    app.run(debug=True)


