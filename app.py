from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for handling Consult now
@app.route('/consult_now', methods=['POST'])
def consult_now():
    # Getting the form data from the user
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    phone = request.form['phone']

    # Saving data to Excel
    data = {'First Name': [firstname], 'Last Name': [lastname], 'Email': [email], 'Phone': [phone]}
    df = pd.DataFrame(data)
    try:
        existing_data = pd.read_excel('data.xlsx')
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        pass  # If file doesn't exist, ignore and create a new one
    df.to_excel('data.xlsx', index=False)
    
    return 'Your Response was saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
