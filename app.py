from flask import Flask, request, render_template
from flask_cors import cross_origin
#import sklearn
import pickle
#import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # C
        C = float(request.form["C"])
        C_sc = (C - 0.17)/0.06
        

        # Si
        Si = float(request.form["Si"])
        Si_sc = (Si - 0.31)/0.09
        
        
        # Mn
        Mn = float(request.form["Mn"])
        Mn_sc = (Mn - 0.81)/0.34
        

        # P
        P = float(request.form["P"])
        P_sc = (P - 0.01)/0.01
        

        # S
        S = float(request.form["S"])
        S_sc = (S - 0.01)/0.003
        

        # Ni
        Ni = float(request.form["Ni"])
        Ni_sc = (Ni - 0.14)/0.17
        

        # Cr
        Cr = float(request.form["Cr"])
        Cr_sc = (Cr - 0.43)/0.46
        
        # Mo
        Mo = float(request.form["Mo"])
        Mo_sc = (Mo - 0.44)/0.39
        
        # Cu
        Cu = float(request.form["Cu"])
        Cu_sc = (Cu - 0.08)/0.06
        
        # V
        V = float(request.form["V"])
        V_sc = (V - 0.06)/0.1
        
        # Al
        Al = float(request.form["Al"])
        Al_sc = (Al - 0.01)/0.01
        
        # N
        N = float(request.form["N"])
        N_sc = (N - 0.01)/0.003
        
        # Ceq
        Ceq = float(request.form["Ceq"])
        Ceq_sc = (Ceq - 0.09)/0.17
        
        # NbTa
        NbTa_sc = 0
        
        # Temperature (°C)
        Temp = float(request.form["Temp"])
        Temp_sc = (Temp - 352)/190
       
   
        
        prediction=model.predict([[
            C_sc,
            Si_sc,
            Mn_sc,
            P_sc,
            S_sc,
            Ni_sc,
            Cr_sc,
            Mo_sc,
            Cu_sc,
            V_sc,
            Al_sc,
            N_sc,
            Ceq_sc,
            NbTa_sc,
            Temp_sc,
            
        ]])
        proof_strength = round((prediction[0]*132)+328,2)
        tensile_strength = round((prediction[1]*240)+496,2)
        elongation = round((prediction[2]*8.8)+26.8,2)
        reduction_area=round((prediction[3]*12.4)+70.2,2)
        
        return render_template('home.html',prediction_text="0.2% Proof Stress is {1}MPa \n Tensile Strength is {2} MPa \n Elongation is {3}% \n Reduction in Area is {4}%".format(proof_strength, tensile_strength, elongation, reduction_area))



    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
