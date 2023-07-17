#creating a flask application.
import io
from flask import Flask, render_template, request, send_file,
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import seaborn as sns
matplotlib.use('Agg')

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/insight', methods=['GET', 'POST'])
def insight():
    cities = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', 'Nyeri', 'Meru', 'Kakamega']


    if request.method == 'POST':
        selected_city = request.form.get('city')
        # Perform accident data analysis for the selected city
        city_accidents = accident_data[accident_data['city'] == selected_city]


        # Generate bar chart for accident count by month
        plt.bar(city_accidents['month'], city_accidents['accident_count'])
        plt.xlabel('Month')
        plt.ylabel('Accident Count')
        plt.title('Monthly Accident Count in ' + selected_city)
        plt.savefig('static/bar_chart.png')
        plt.close()


        # Generate line chart for accident count by year
        plt.plot(city_accidents['year'], city_accidents['accident_count'])
        plt.xlabel('Year')
        plt.ylabel('Accident Count')
        plt.title('Yearly Accident Count in ' + selected_city)
        plt.savefig('static/line_chart.png')
        plt.close()


        # Generate pie chart for accident type distribution
        accident_type_counts = city_accidents['accident_type'].value_counts()
        plt.pie(accident_type_counts, labels=accident_type_counts.index, autopct='%1.1f%%')
        plt.title('Accident Type Distribution in ' + selected_city)
        plt.savefig('static/pie_chart.png')
        plt.close()
        # Generate data report
        data_report = city_accidents.to_string()

        return render_template('insight.html', cities=cities, selected_city=selected_city, data_report=data_report)


    return render_template('insight.html', cities=cities)

@app.route('/logout')
def logout():
    # Logout logic goes here
    return 'Logout Page'

@app.route('/signin')
def signin():
    # Sign in logic goes here
    return render_template('signin.html')

@app.route('/signup')
def signup():
    # Sign up logic goes here
    return render_template('signup.html')

@app.route('/download_report')
def download_report():
    data_report = request.args.get('data_report')
    bytes_io = io.BytesIO(data_report.encode())
    bytes_io.seek(0)
    return send_file(bytes_io, mimetype='text/csv', download_name='data_report.csv', as_attachment=True)

if __name__ == '__main__':
    # Create a dictionary with sample accident data
    # Create a dictionary with sample accident 
    data ={ 
        'city': ['Nairobi', 'Nairobi', 'Mombasa', 'Mombasa', 'Kisumu', 'Kisumu', 'Nakuru', 'Nakuru','Eldoret', 'Eldoret','Nyeri','Nyeri','Meru','Meru','Kakamega','Kakamega'], 
        'year': [2019, 2020, 2019, 2020, 2019, 2020, 2019, 2020,2023,2021,2022,2020,2020,2021,2019,2023], 
        'month': ['Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Feb','Jan', 'Feb','Jan', 'March','April','June','May','June'], 
        'accident_type': ['Collision', 'Pedestrian', 'Pedestrian', 'Pedestrian', 'Collision', 'Pedestrian', 'Pedestrian', 'Pedestrian','Collision', 'Pedestrian','Collision', 'Pedestrian','Collision', 'Pedestrian','Collision', 'Pedestrian'],
        'accident_count': [50, 60, 40, 45, 35, 30, 25, 20,70,35,46,70,50,45,80,50],
        }
    # Create a pandas DataFrame from the dictionary
    accident_data = pd.DataFrame(data)
    app.run(debug=True)