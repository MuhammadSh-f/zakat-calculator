from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_zakat(wealth, debts, gold_price_per_gram):
    # Calculate Nisab
    nisab = 85 * gold_price_per_gram
    net_wealth = wealth - debts
    
    if net_wealth >= nisab:
        zakat = net_wealth * 0.025
        return zakat, nisab, True
    else:
        return 0, nisab, False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get data from the form
    wealth = float(request.form['wealth'])
    debts = float(request.form['debts'])
    gold_price_per_gram = float(request.form['gold_price_per_gram'])

    # Calculate Zakat
    zakat, nisab, eligible = calculate_zakat(wealth, debts, gold_price_per_gram)
    return render_template('result.html', zakat=zakat, nisab=nisab, eligible=eligible)

if __name__ == '__main__':
    app.run(debug=True)
