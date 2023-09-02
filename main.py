from gtts import gTTS
from googletrans import Translator


def chinese_to_english_speech(chinese_text):
    # Create a Translator object
    translator = Translator()

    # Detect the language of the input text (Chinese)
    detected_lang = translator.detect(chinese_text).lang

    # Translate Chinese text to English
    if detected_lang == 'zh-CN':
        english_text = translator.translate(
            chinese_text, src='zh-CN', dest='en').text
    else:
        # Handle cases where the input text is not in Chinese
        return "Input text is not in Chinese."

    # Convert the English text to speech
    tts = gTTS(text=english_text, lang='en')

    # Save the speech to a file or play it
    tts.save("english_speech.mp3")
    # Alternatively, you can play the speech directly:
    # tts.play()


# Take user input for Chinese text
chinese_text = input(
    "Enter the Chinese text you want to convert to English speech: ")
chinese_to_english_speech(chinese_text)
