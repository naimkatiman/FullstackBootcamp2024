from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        salutation = request.form['salutation']
        name = request.form['name'].strip()
        message = request.form['message'].strip()

        # Validation
        if not name:
            flash('Name is required.', 'error')
        elif len(name) < 2 or len(name) > 50:
            flash('Name must be between 2 and 50 characters long.', 'error')
        elif not message:
            flash('Message is required.', 'error')
        elif len(message) < 10 or len(message) > 300:
            flash('Message must be between 10 and 300 characters long.', 'error')
        else:
            # Confirmation page
            return render_template('confirmation.html', name=name, message=message, salutation=salutation)

    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
