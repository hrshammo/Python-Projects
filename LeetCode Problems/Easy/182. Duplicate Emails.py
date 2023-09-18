import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Group by the 'email' column and count occurrences
    email_counts = person['email'].value_counts()
    
    # Filter for emails with count greater than 1 (duplicates)
    duplicates = email_counts[email_counts > 1].index.tolist()
    
    # Create a new data frame with the duplicate emails
    result = pd.DataFrame({'Email': duplicates})
    
    return result
