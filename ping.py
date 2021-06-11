# pip install speedtest-cli
# pip install python-cfonts
import speedtest as st
from cfonts import render

# Title
title = render('Speed Test', colors=['red', 'white'], align='center')
print(title)

# Code
try:
    speed = st.Speedtest()

    print('Server Listening...')
    speed.get_servers()

    print('Choosing Server...')
    bestServer = speed.get_best_server()

    print(f"\nServer Location: {bestServer['country']}/{bestServer['name']}")

    print('Download Test...')
    downloadResult = speed.download()

    print('Upload Test...')
    uploadResult = speed.upload()

    print('Ping Test...\n')
    pingResult = speed.results.ping

    print(f"Download Result: {downloadResult / 1024 /1024:.2f} Mbps")
    print(f"Upload Result: {uploadResult / 1024 /1024:.2f} Mbps")
    print(f"Ping Result: {pingResult:.2f} ms")

    input('')

except:
    print("Check your internet connection and try again")
    input('')
