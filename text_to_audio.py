
#coded by ostronics, Qxchan
#contact us at https://www.disotronics.com , on TELEGRAM @ https://t.me/Qxchan
#visit our groupo on telegram @ hackerbdv https://t.me/hackerbdv

import os
#pip install gtts
try:
	from gtts import gTTS
except ImportError:
	os.system('pip install gtts')
	os.system('pip install pygobject')
	from gtts import gTTS

#pip install playsound
try:
	from playsound import playsound
except ImportError:
	os.system('pip install playsound')
	from playsound import playsound
try:
    audio = 'speech.mp3'
    language = 'en'
    sp = gTTS(text = input("Enter the text in which you want to convert to audio file!: \n\t"), lang = language,slow=False)

    sp.save(audio)
    playsound(audio)
except Exception as e:
    print(e, "\n\t\r\nplay the file speech.mp3\n")
