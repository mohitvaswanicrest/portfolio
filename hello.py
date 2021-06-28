from flask import Flask,render_template,url_for,request
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def main():
  return render_template('index.html')

@app.route('/<string:page_name>')
def main2(page_name):
  return render_template(page_name)



@app.route("/<username>/<int:post_id>")
def hello(username=None,post_id=None):
  return "Hello " +username+" has posted a new post which has id: %d" %post_id

@app.route("/blog")
def blog():
  return "this is mohit's blog"

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_data_to_csv(data)
        return render_template('thanks.html')
      except:
        return 'did not save to database'  
    else:
      return "Something Went Wrong"

def write_data(data):
  with open('database.txt',mode='a') as database:
    email = data["email"]
    subject =data["subject"]
    message =data["message"]
    file=database.write(f'\n{email},{subject},{message}')

def write_data_to_csv(data):
  with open('database.csv',mode='a',newline='') as database2:
    email = data["email"]
    subject =data["subject"]
    message =data["message"]
    csv_writer= csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])
