from flask import Flask , jsonify , request

app = Flask(__name__)

data = [{
    "Contact": 9987644456,
    "Name":u"Raju",
    "id": 1,
    "done": False
},
{
    "Contact": 9876543222,
    "Name":u"Rahul",
    "id": 2,
    "done": False

}]

@app.route("/")

def hello():
    return("Hello !!")

@app.route("/add-data",methods = ["POST"])

def add_task():

    if not request.json:

        return jsonify({
            "status":"Error !!",
            "message":"Please provide the data !!"
        } , 400)

    contact = {
        "id": data[-1]['id'] + 1,
        "Name": request.json['Name'],
        "Contact": request.json.get('Contact',""),
        "done": False
    }

    data.append(contact)
    return jsonify({
        "status":"Success",
        "message":"Task added successfuly"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data":data,
    })

if (__name__ == "__main__"):
    app.run(debug = True)
