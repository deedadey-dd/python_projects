from flask import Flask, render_template, request
import requests
import smtplib
import os

sender_email = os.environ.get('SENDER_EMAIL')
sender_pass = os.environ.get('SENDER_PASS')
email_host = os.environ.get('EMAIL_HOST')
email_port = os.environ.get('EMAIL_PORT')

print(sender_email)
print(sender_pass)
print(email_host)
print(email_port)

app = Flask(__name__)


def send_email(receiver_email, the_message):
    with smtplib.SMTP(host=email_host, port=email_port) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_pass)
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=the_message)
        print('email sent')


blog_url = 'https://api.npoint.io/e38e8ad24640b232fb38'
blog_posts = requests.get(blog_url).json()


@app.route('/')
def home():

    return render_template('index.html', posts=blog_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    title = ''
    subtitle = ''
    body = ''
    for blog in blog_posts:
        if blog['id'] == post_id:
            title = blog['title']
            subtitle = blog['subtitle']
            body = blog['body']

    return render_template('post.html', title=title, subtitle=subtitle, body=body)


@app.route('/form-entry', methods=['POST', 'GET'])
def receive_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        message_to_send = f"Subject: CONTACTED!!!\n\nName: {name}\nemail: {email}\nPhone No.: {phone}\n\nMessage:\n{message}"
        send_email('deedadey@gmail.com', message_to_send)
        print(message_to_send)

        return render_template('form-entry.html')


if __name__ == "__main__":
    app.run(debug=True)
