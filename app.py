import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template
import os

# Imprimir la lista de archivos en el directorio
print(os.listdir("C:\\Users\\18498\\Desktop\\PruebasPy\\MineriaDeDatos\\VisualisaciónDeDatos"))
# Paso 1: Cargar el dataset adjunto
df = pd.read_csv("C:\\Users\\18498\\Desktop\\PruebasPy\\MineriaDeDatos\\VisualisaciónDeDatos\\netflix-titles.csv")

# Paso 2: Visualización de los 10 directores con más películas/series en Netflix
top_directors = df['director'].value_counts().head(10)
plt.figure(figsize=(16, 6))
sns.barplot(x=top_directors.values, y=top_directors.index)
plt.xlabel('Número de Películas/Series')
plt.ylabel('Director')
plt.title('Top 10 Directores con más Películas/Series en Netflix')
# Guardar la gráfica como imagen
plt.savefig('static/top_directors_plot.png')
plt.close()

# Paso 3: Visualización comparativa de la cantidad de series vs cantidad de películas
types_count = df['type'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(types_count, labels=types_count.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Porcentaje de Películas y Series en Netflix')
# Guardar la gráfica como imagen
plt.savefig('static/types_count_plot.png')
plt.close()

# Paso 4: Visualización comparativa de las 5 clasificaciones con más títulos de series/películas
top_categories = df['listed_in'].value_counts().head(5)
plt.figure(figsize=(30, 10))
sns.barplot(x=top_categories.values, y=top_categories.index)
plt.xlabel('Número de Títulos')
plt.ylabel('Categoría')
plt.title('Top 5 Categorías con más Títulos en Netflix')
# Guardar la gráfica como imagen
plt.savefig('static/top_categories_plot.png')
plt.close()

# Paso 5: Crear un dashboard con Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/directors')
def directors():
    return render_template('directors.html', plot1='top_directors_plot.png')

@app.route('/types')
def types():
    return render_template('types.html', plot2='types_count_plot.png')

@app.route('/categories')
def categories():
    return render_template('categories.html', plot3='top_categories_plot.png')

if __name__ == '__main__':
    app.run(debug=True)
