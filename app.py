from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

# Datenbankverbindung
engine = create_engine(f"postgresql://{os.getenv('DBUSER')}:{os.getenv('DBPASS')}@localhost/{os.getenv('DBNAME')}")

@app.route('/')
def index():
    # Holen der Daten aus der Datenbank
    df_sub = pd.read_sql_query('''SELECT address_raw, rooms, area, price FROM apartment_table''', con=engine)
    rows = df_sub.head().to_dict(orient='records')

    # Plot erstellen
    fig = plt.figure(figsize=(7, 4))
    plt.hist(df_sub['price'], bins=20, color='#5DADE2', alpha=1.00, rwidth=0.95)
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title('Histogram of Apartment Prices')
    plt.grid(axis='y', alpha=0.75)

    # Plot als Bild umwandeln
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template("index.html", rows=rows, plot_url=f"data:image/png;base64,{plot_url}")

if __name__ == '__main__':
    app.run(debug=True)
