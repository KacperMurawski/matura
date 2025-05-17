from flask import Flask, render_template
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # Generowanie danych
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    # Tworzenie animowanego wykresu
    fig = go.Figure()

    for i in range(len(x)):
        fig.add_trace(go.Scatter(x=x[:i+1], y=y[:i+1], mode='lines+markers', name='sin(x)'))

    fig.update_layout(title='Animowany wykres funkcji sinus', xaxis_title='x', yaxis_title='sin(x)')
    fig.write_html('templates/sine_wave.html')

    return render_template('sine_wave.html')

if __name__ == '__main__':
    app.run(debug=True)
