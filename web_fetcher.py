import requests
from bs4 import BeautifulSoup
import json

def fetch_web_data(source_file,output_file):
    with open(source_file,"r") as f:
        urls=f.read().splitlines()
    extracted_data=[]
    headers={
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)"
    }
    for url in urls:
        try:
            response=requests.get(url,headers=headers,timeout=10)
            response.raise_for_status()

            soup=BeautifulSoup(response.text,"html.parser")
            title=soup.title.string if soup.title else "No Title"

            paragraph=""
            skip_keywords = ["javascript", "enable", "notice", "cookies"]

            for p in soup.find_all("p"):
                text = p.get_text().strip()
                if len(text) < 80:
                    continue
                lower_text = text.lower()
                if any(word in lower_text for word in skip_keywords):
                    continue
                paragraph = text
                break
            extracted_data.append({
                "url": url,
                "title":title,
                "content": paragraph
            })
        except Exception as e:
            extracted_data.append({
                "url":url,
                "error" :str(e)
            })
    with open (output_file,"w",encoding="utf-8") as f:
        json.dump(extracted_data,f,indent=4)
    return extracted_data

            

            
                    

