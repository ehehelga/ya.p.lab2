import os
import requests
import typer
from clint.textui import progress

def main(url: str):
   file_name = os.path.basename(url)
   with open(file_name, "wb") as f:
      response = requests.get(url, stream=True)
      total_length = int(response.headers.get('content-length'))
      for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
        if chunk:
            f.write(chunk)
            f.flush()
      print("\nDone!")

if __name__ == "__main__":
   typer.run(main)