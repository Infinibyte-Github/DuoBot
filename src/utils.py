languages = {'English': 'en', 'Swedish': 'sv', 'Guarani': 'gn', 'Yiddish': 'yi', 'Navajo': 'nv', 'Finnish': 'fi', 'Swahili': 'sw', 'Zulu': 'zu', 'Spanish': 'es', 'Japanese': 'ja', 'Esperanto': 'eo', 'Portuguese': 'pt', 'Hindi': 'hi', 'Korean': 'ko', 'Italian': 'it', 'Vietnamese': 'vi', 'Indonesian': 'id', 'German': 'de', 'Norwegian (BokmÃ¥l)': 'no-BO', 'Polish': 'pl', 'Romanian': 'ro', 'Greek': 'el', 'Haitian Creole': 'ht', 'Czech': 'cs', 'Catalan': 'ca', 'Chinese': 'zh', 'Dutch': 'nl-NL', 'Latin': 'la', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Russian': 'ru', 'French': 'fr', 'Hungarian': 'hu', 'Danish': 'da', 'Arabic': 'ar', 'Hebrew': 'he', 'Chinese (Cantonese)': 'zh-HK', 'Hawaiian': 'hw', 'Irish': 'ga', 'Scottish Gaelic': 'gd', 'High Valyrian': 'hv', 'Welsh': 'cy', 'Klingon': 'tlh', 'Tagalog': 'tl', 'Bengali':'bn', 'Thai':'th'}
emojidict = {'en': 'ðºð¸', 'sv': 'ð¸ðª', 'gn': 'ðµð¾', 'yi': 'ð®ð±', 'nv': 'ðºð¸', 'fi': 'ð«ð®', 'sw': 'ð°ðª', 'zu': 'ð¿ð¦', 'es': 'ðªð¸', 'ja': 'ð¯ðµ', 'eo': '<:flag_eo:1045425989934645379>', 'pt': 'ðµð¹', 'hi': 'ð®ð³', 'ko': 'ð°ð·', 'it': 'ð®ð¹', 'vi': 'ð»ð³', 'id': 'ð®ð©', 'de': 'ð©ðª', 'no-BO': 'ð³ð´', 'pl': 'ðµð±', 'ro': 'ð·ð´', 'el': 'ð¬ð·', 'ht': 'ð­ð¹', 'cs': 'ð¨ð¿', 'ca': 'ðªð¸', 'zh': 'ð¨ð³', 'nl-NL': 'ð³ð±', 'la': 'ð»ð¦', 'tr': 'ð¹ð·', 'uk': 'ðºð¦', 'ru': 'ð·ðº', 'fr': 'ð«ð·', 'hu': 'ð­ðº', 'da': 'ð©ð°', 'ar': 'ð¸ð¦', 'he': 'ð®ð±', 'zh-HK': 'ð­ð°', 'hw': 'ðºð¸', 'ga': 'ð®ðª', 'gd': 'ð¬ð§', 'hv': 'ð»ð¦', 'cy': 'ð¬ð§', 'tlh': 'ð»ð¦', 'tl': 'ðµð­', 'bn': 'ð§ð©', 'th': 'ð¹ð­'}

def name_to_code(name):
    return languages[name]

def code_to_name(code):
    return list(languages.keys())[list(languages.values()).index(code)]

def emoji(code):
    return emojidict[code]  # I'm not sure if this is the right way to do it, but it works