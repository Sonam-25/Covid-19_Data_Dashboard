import src.extract as extract
import src.app as app
import logging

def main():
    # First, run data extraction
    extract.extract_data()
    
    # Then, start the Flask application
    app.app.run(debug=True)

logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    main()
