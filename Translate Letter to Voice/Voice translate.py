import gtts as gt
import playsound as sound

tts = gt.gTTS(
    'rabi shrestha '
)
tts.save('voice.mp3')
sound.playsound('voice.mp3')
