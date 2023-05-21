# =[Modules dan Packages]========================
import numpy as np
from flask import Flask, render_template, request, jsonify
# from flask_ngrok import run_with_ngrok  #Karena engga make ngrok diapus aja
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor
from sklearn.model_selection import train_test_split
from joblib import load

# =[Variabel Global]=============================

app = Flask(__name__, static_url_path='/static')
model_AB = None

# =[Routing]=====================================


# [Routing untuk Halaman Utama atau Home]
@app.route("/")
def beranda():
  return render_template('index.html')


# [Routing untuk API]
@app.route(
  "/api/prediksi", methods=['POST']
)  ##file api/prediksi liat dimana mat?## api prediksi itu path route nya pal bukan file
def apiPrediksi():
  # float_feature = [float(x) for x in request.form.values()]
  # feature = [np.array(float_feature)]
  # prediksi = model_AB.prediksi(feature)
  # return render_template("test.html", prediksi_text="{}".format(prediksi))

  # Nilai default untuk variabel input atau features (X) ke model
  input_Lokasi = 'Depok'
  input_Tipe = 'Tipe 70'
  input_KT = '2'
  input_KM = '1'
  input_Listrik = '2200'

  # POST data dari API
  if request.method == 'POST':
    # Set nilai untuk variabel input atau features (X) berdasarkan input dari pengguna
    # $("#range_sepal_length").val();

    input_Lokasi = str(request.form.get('lokasi'))
    input_Tipe = str(request.form.get('tipe_rumah'))
    input_KT = str(request.form.get('kamar_tidur'))
    input_KM = str(request.form.get('kamar_mandi'))
    input_Listrik = str(request.form.get('tipe_listrik'))

    print(f'test : {input_KT}')

    if input_Lokasi == "Lokasi":
      input_Lokasi = "Jakarta Pusat"
    if input_Tipe == "tipe_rumah":
      input_Tipe = "Tipe 36"
    if input_KT == "KT":
      input_KT = "1"
    if input_KM == "KM":
      input_KM = "1"
    if input_Listrik == "tipe_listrik":
      input_Listrik = "1300"

    # Membuat dataframe pandas
    df = pd.DataFrame(
      data={
        "Lokasi": [input_Lokasi],
        "Tipe": [input_Tipe],
        "KT": [input_KT],
        "KM": [input_KM],
        "Listrik": [input_Listrik],
      })

    # Encoder lokasi
    df['Lokasi'] = df['Lokasi'].map({
      'Jakarta Pusat': 0,
      'Jakarta Timur': 1,
      'Jakarta Selatan': 2,
      'Jakarta Barat': 3,
      'Jakarta Utara': 4,
      'Kota Bogor': 5,
      'Kabupaten Bogor': 6,
      'Depok': 7,
      'Tangerang': 8,
      'Kota Bekasi': 9,
      'Kabupaten Bekasi': 10
    })

    # Encoder tipe rumah
    df['Tipe'] = df['Tipe'].map({
      'Tipe 21': 0,
      'Tipe 36': 1,
      'Tipe 45': 2,
      'Tipe 54': 3,
      'Tipe 60': 4,
      'Tipe 70': 5,
      'Tipe 90': 6,
      'Tipe 120': 7,
      'Tipe 140': 8
    })

    # Encoder listrik
    df['Listrik'] = df['Listrik'].map({'900': 0, '1300': 1, '2200': 2})

    print(df)
    print(df[0:1])

    #Menampilkan Prediksi model adaboost
    hasil_prediksi = model_AB.predict(df[0:1])[0]

    print(hasil_prediksi)

    hasil_prediksi_conv = f"Rp. {hasil_prediksi:,.0f}"

    # Return hasil prediksi dengan format JSON
    return jsonify({"prediksi": hasil_prediksi_conv})


# =[Main]========================================

if __name__ == '__main__':
  # Load model yang telah ditraining
  model_AB = load('prediksi_harga_rumah.model')

  # Run Flask di Google Colab menggunakan ngrok
  # run_with_ngrok(
  #   app
  # )  # <-- Ngrok susah kalo di replit ganti jadi harus run ga pake ngrok terus host nya diganti "0.0.0.0"

  app.run(host="0.0.0.0", port=4000, debug=True)  # <-- Harusnya gini
  # app.run()
