from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_etl():
    # Step 1: Extract data
    raw_data = extract_data()
    
    # Step 2: Transform data
    processed_data = transform_data(raw_data)
    
    # Step 3: Load data
    load_data(processed_data)

if __name__ == "__main__":
    run_etl()