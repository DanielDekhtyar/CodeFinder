from openai import OpenAI
from dotenv import load_dotenv
import datetime
import os


# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)


def list_and_delete_file():
    while True:
        response = client.files.list(purpose="fine-tune")
        files = list(response.data)
        if len(files) == 0:
            print("No files found.")
            return
        for i, file in enumerate(files, start=1):
            created_date = datetime.datetime.utcfromtimestamp(file.created_at).strftime(
                "%Y-%m-%d"
            )
            print(f"[{i}] {file.filename} [{file.id}], Created: {created_date}")
        choice = input(
            "Enter a file number to delete, or any other input to return to menu: "
        )
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(files):
            return
        selected_file = files[int(choice) - 1]
        client.files.delete(selected_file.id)
        print(f"File deleted: {selected_file.filename}")


list_and_delete_file()
