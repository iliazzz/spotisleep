import os
print("Input time pefore spotify is killed below (in minutes):")
time = int(input())

timeSec = str(time*60)

os.system("timeout /t " + timeSec + " & taskkill /im Spotify.exe /f")