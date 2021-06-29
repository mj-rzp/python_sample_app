import razorpay
import json

from flask import Flask, render_template, request

app = Flask(__name__,static_folder = "static", static_url_path='')
razorpay_client = razorpay.Client(auth=("rzp_test_FwyKemzlKf9Wi6","3FZLH15XNZY5SMwlGZNfy6LV"))

@app.route('/')
def app_create():
    return render_template('app.html')

@app.route('/pay', methods=['POST'])
def pay():
    global payment, name
    name = request.form.get('username')
    email = request.form.get('useremail')
    contact = request.form.get('usercontact')
    order_amount = 500
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'   
    payment = razorpay_client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt)
    
    return render_template('pay.html',payment = payment)
if __name__ == '__main__':
    app.run()
