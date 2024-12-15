from app.main import app
#from app.tests.chart_plot import create_plot

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    #create_plot()