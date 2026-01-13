import pandas as pd
import re

def is_valid_email(email):
    if pd.isna(email):
        return False
    email_pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

def clean_data(input_path, valid_output_path, invalid_output_path):
        df = pd.read_csv(input_path)
        valid_rows = []
        invalid_rows = []
        for index,row in df.iterrows():
             reasons=[]
             if pd.isna(row["name"]) or row["name"].strip() == "":
                  reasons.append("Missing name")

             if not is_valid_email(row["email"]):
                  reasons.append("Invalid email")
             try:
                  age=int(row["age"])
                  if age <18 or age>60:
                       reasons.append("Age out of range")
             except:            
                  reasons.append("Invalid age")
             try:
                  score=int(row["score"])
                  if score<0 or score>100:
                       reasons.append("Score out of range")
             except:
                  reasons.append("Invalid score")
             
             if len(reasons)==0:
                  if score>=80:
                       quality="High"
                
                  elif score>=50:
                       quality="Medium"
                  else:
                       quality="Low"
                  row["quality"]=quality
                  valid_rows.append(row)                  
             else:
                  row["rejection_reasons"]="; ".join(reasons)
                  invalid_rows.append(row)
             
             valid_df=pd.DataFrame(valid_rows)
             invalid_df=pd.DataFrame(invalid_rows)

             valid_df.to_csv(valid_output_path, index=False)
             invalid_df.to_csv(invalid_output_path, index=False)

        
        


