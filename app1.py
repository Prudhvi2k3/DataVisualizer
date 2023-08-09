from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)

# Load the Iris dataset
iris_data = pd.read_csv('D:\Problem Statement\iris.csv')

@app.route('/')
def index():
    # Create scatterplot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Sepal_Length', y='Sepal_Width', hue='Class', data=iris_data)
    plt.title('Sepal Length vs. Sepal Width')
    
    # Convert plot to image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    scatterplot_url = base64.b64encode(img.getvalue()).decode()

    # Create histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data=iris_data, x='Petal_Length', hue='Class', multiple='stack')
    plt.title('Petal Length Histogram')
    
    # Convert histogram to image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    histogram_url = base64.b64encode(img.getvalue()).decode()

    # Create pair plot
    plt.figure(figsize=(10, 6))
    sns.pairplot(iris_data, hue='Class')
    plt.title('Pair Plot')
    
    # Convert pair plot to image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    pairplot_url = base64.b64encode(img.getvalue()).decode()

    #Create box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=iris_data, x='Class', y='Petal_Length')
    plt.title('Petal Length Box Plot')

    # Convert pair plot to image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    boxplot_url = base64.b64encode(img.getvalue()).decode()

    # Create violin plot
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=iris_data, x='Class', y='Sepal_Width', inner='quartile')
    plt.title('Sepal Width Violin Plot')

    # Convert Violin plot to image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    violinplot_url = base64.b64encode(img.getvalue()).decode()

    # Create pie chart 
    plt.figure(figsize=(8, 8))
    species_counts = iris_data['Class'].value_counts()
    plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Species Distribution (Matplotlib)')

    # Convert Pie chart to image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    piechart_url = base64.b64encode(img.getvalue()).decode()

    # Render HTML template with plots and dataset overview
    dataset_overview = iris_data.head().to_html(index=False)
    # Render HTML template with plots
    return render_template('index.html', scatterplot_url=scatterplot_url,
                           histogram_url=histogram_url, 
                           pairplot_url=pairplot_url,
                           boxplot_url=boxplot_url,
                           violinplot_url=violinplot_url,
                           piechart_url=piechart_url,
                           dataset_overview=dataset_overview
                           )


if __name__ == '__main__':
    app.run(debug=True)
