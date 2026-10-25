import pandas as pd
import numpy as np
import logging
import re
import os

os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/pipeline_audit.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    logging.info("Starting ETL Data Quality Pipeline...")
    df = pd.read_csv("data/dirty_raw_events.csv")
    df_clean = df.dropna(subset=['user_id']).copy()
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$'
    valid_email_mask = df_clean['email'].apply(lambda x: bool(re.match(email_regex, str(x))))
    df_clean = df_clean[valid_email_mask]
    valid_score_mask = (df_clean['engagement_score'] >= 0) & (df_clean['engagement_score'] <= 100)
    df_clean = df_clean[valid_score_mask]
    df_clean.to_csv("data/clean_events_warehouse.csv", index=False)
    print("ETL Audit Complete. Clean data saved.")

if __name__ == "__main__":
    run_pipeline()
