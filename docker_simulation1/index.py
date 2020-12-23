from flask import Flask
from ca_simulation1 import simulation_1day
import datetime

app = Flask(__name__)

@app.route('/simulation', methods=['GET'])
def main():
    
    today = datetime.date.today()
    start_date = str(today)
    start_date = '2020-12-17'
    date = start_date
    
    simulation_1day(date)
    return "The simulation is executed successfully, Please Check in the ca_simulationdb"
    
@app.route('/test', methods=['GET'])
def test():
    return "Hello World!!!!!!!!!!!"
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)