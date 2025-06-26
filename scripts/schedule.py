from scripts.first_batch_10years import get_data_historical
from scripts.schedule_data_update import get_next_day 

def main():
    get_data_historical() ## get data from 2015 to 2025 until 2 days ago, execute this only once
    ## 
    get_next_day() ## get data from 2 days ago, execute this every day after the first run
    

if __name__ == "__main__":
    main()