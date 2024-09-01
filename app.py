from flask import Flask, render_template, request
import mysql.connector as mc
import joblib

model = joblib.load("./models/linear_model.lb")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        brand_name = int(request.form['brand_name'])
        Kms_Driven = int(request.form['Kms_Driven'])
        owner = int(request.form['owner'])
        age = int(request.form['age'])
        power = int(request.form['power'])
        
        brand_dict = {'Bajaj': 1, 'Royal Enfield': 2, 'Hero': 3, 'Honda': 4, 'Yamaha': 5, 'TVS': 6,
                      'KTM': 7, 'Suzuki': 8, 'Harley-Davidson': 9, 'Kawasaki': 10, 'Hyosung': 11,
                      'Mahindra': 12, 'Benelli': 13, 'Triumph': 14, 'Ducati': 15, 'BMW': 16}
        
        brand_dict2 = {value: key for key, value in brand_dict.items()}
        
        UNSEEN_DATA = [[Kms_Driven, owner, age, power, brand_name]]
        
        PREDICTION = model.predict(UNSEEN_DATA)[0][0]
        
        # MySQL INSERT statement using %s placeholders
        query_to_insert_ = """
        INSERT INTO Bike (owner, brand, kms_driven, power, age, predicted_price) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        # Connect to MySQL database
        conn = mc.connect(
            host='localhost',
            user='root',
            password='reetika',
            database='ml1',
            charset='utf8' 
        )
        cur = conn.cursor()
        
        data = (owner, brand_dict2[brand_name], Kms_Driven, power, age, int(round(PREDICTION, 2)))
        cur.execute(query_to_insert_, data)
        conn.commit()
        
        print("Your record has been stored in the database")
        cur.close()
        conn.close()
        
        return render_template('home.html', prediction_text=str(round(PREDICTION, 2)))

if __name__ == "__main__":
    app.run(debug=True)
