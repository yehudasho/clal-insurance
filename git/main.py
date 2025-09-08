from flask import Flask, render_template
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    year = now.year
    month = now.month
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    return render_template('calendar.html', year=year, month=month_name, calendar=cal)

if __name__ == '__main__':
    app.run(debug=True)
