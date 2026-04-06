from flask import Flask, render_template, request, redirect
from datetime import datetime
import tracker

app = Flask(__name__)

@app.route('/')
def home():
    total = tracker.get_total_expense()
    balance = tracker.get_initial_balance()
    remaining = tracker.get_remaining_balance()

    return render_template('index.html',
                           total=total,
                           balance=balance,
                           remaining=remaining)

@app.route('/set_balance', methods=['POST'])
def set_balance():
    try:
        amount = float(request.form['balance'])
        tracker.set_initial_balance(amount)
    except:
        pass
    return redirect('/')

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':

        use_time = request.form.get('use_time')

        if use_time == 'y':
            timestamp = datetime.now().strftime("%H:%M %d-%m-%Y")
        else:
            date = request.form.get('date')
            time = request.form.get('time')
            try:
                timestamp = datetime.strptime(time + " " + date, "%H:%M %d-%m-%Y").strftime("%H:%M %d-%m-%Y")
            except:
                return "❌ Invalid date/time format"

        category = request.form.get('category')

        try:
            amount = float(request.form.get('amount'))
        except:
            return "❌ Invald amount"

        note = request.form.get('note')

        success = tracker.add_expense(timestamp, category, amount, note)

        if not success:
            return "❌ Not enough balance"

        return redirect('/')

    return render_template('add expense.html')

@app.route('/expenses')
def view_expenses():
    expenses = tracker.get_expenses()
    return render_template('view expense.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)