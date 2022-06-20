# Python Tkinter QRcode reader
read and extract information from QR codes!

![qr-code-gen](https://user-images.githubusercontent.com/68698872/174504949-4468b979-dba2-44f2-9ae2-7d7634ccf188.png)

1. Clone this repo into a project folder and create a virtual environment
```
cd project-folder/
git clone https://github.com/westoleaboat/qr-codeReader.git
cd qr-codeReader
sudo python3 -m venv env_name
```
2. Install dependencies 
```
source env_name/bin/activate
pip install opencv-python Pillow
```
3. Open an image containing the QR code you want to examine and run main.py (you may need sudo privileges)
```
sudo python3 main.py
```
4. The program will start running and an indication will appear on top of your screen.
5. Click the top-left and bottom-right corners of the QRcode you want to examine, as shown below.
![qr-coordinates](https://user-images.githubusercontent.com/68698872/174506040-beb410ce-fc2e-4d53-bf69-208920cb2294.png)

6. If successful, the GUI will appear and show the encoded data inside the QRcode.
