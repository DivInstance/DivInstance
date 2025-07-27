from datetime import datetime

def calculate_uptime(start_date):
    start = datetime(2003, 11, 3)
    end = datetime.now()
    delta = end - start
    
    years = delta.days // 365
    remaining_days = delta.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    
    return f"{years} years, {months} months, {days} days"

# Usage
if __name__ == "__main__":
    uptime = calculate_uptime(datetime(2003, 11, 3))
    print(f"Uptime: {uptime}")
    with open("uptime.md", "w") as f:
        f.write(f"Uptime: {uptime}")
