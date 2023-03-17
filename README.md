# Rest API with python
This is a simple **hello world** rest api written in python.
<br>
In the Ubuntu terminal, follow the steps below to run and test the API:
<br>
<br>
## Step 1
`user:/$ sudo apt-get update`
<br>
<br>
## Step 2
`user:/$ sudo apt-get install -y python3 python3-pip`
<br>
<br>
## Step 3
`user:/$ pip install fastapi uvicorn[standard]`
<br>
<br>
## Step 4
Download the `app.py` file and paste it in the folder of your choice.
<br>
<br>
After that, run the following statement:
<br>
`user:/$ uvicorn your_folder_with_file.app:app --host 0.0.0.0 --reload`
<br>
<br>
## Step 5
Open the browser and type the url: `http://localhost:8000` and press enter.
<br>
You will see the result below:
<br>
`{"message":"Hello World!"}`
<br>
<br>
## Step 6
On the browser type the follow url: `http://localhost:8000?name=Your name` and press enter.
<br>
You will see the result below:
<br>
`{"message":"Hello Your name!"}`
