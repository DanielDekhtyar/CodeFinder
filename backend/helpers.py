"""
Here are just helper functions to be used in other functions in the backend
"""

from datetime import datetime, timedelta


def format_date(date):
    # Convert the date string to a datetime object
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    
    # Get today's date and time
    now = datetime.utcnow()
    
    # Calculate the difference between now and the given date
    delta = now - date
    
    # If the difference is less than a minute
    if delta < timedelta(minutes=1):
        return 'less than a minute ago'
    # If the difference is less than an hour
    elif delta < timedelta(hours=1):
        return f'{delta.seconds // 60} minutes ago'
    # If the difference is less than 24 hours
    elif delta < timedelta(days=1):
        return f'{delta.seconds // 3600} hours ago'
    # If the date is today
    elif delta.days == 0:
        return 'today'
    # If the date is yesterday
    elif delta.days == 1:
        return 'yesterday'
    # If the date is within the past 7 days
    elif 1 < delta.days <= 7:
        return f'{delta.days} days ago'
    # Otherwise, format the date as 'on day of month year'
    else:
        return f'on {date.day} of {date.strftime("%B")} {date.year}'
