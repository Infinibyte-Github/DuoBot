languages = {'English': 'en', 'Swedish': 'sv', 'Guarani': 'gn', 'Yiddish': 'yi', 'Navajo': 'nv', 'Finnish': 'fi', 'Swahili': 'sw', 'Zulu': 'zu', 'Spanish': 'es', 'Japanese': 'ja', 'Esperanto': 'eo', 'Portuguese': 'pt', 'Hindi': 'hi', 'Korean': 'ko', 'Italian': 'it', 'Vietnamese': 'vi', 'Indonesian': 'id', 'German': 'de', 'Norwegian (Bokmål)': 'no-BO', 'Polish': 'pl', 'Romanian': 'ro', 'Greek': 'el', 'Haitian Creole': 'ht', 'Czech': 'cs', 'Catalan': 'ca', 'Chinese': 'zh', 'Dutch': 'nl-NL', 'Latin': 'la', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Russian': 'ru', 'French': 'fr', 'Hungarian': 'hu', 'Danish': 'da', 'Arabic': 'ar', 'Hebrew': 'he', 'Chinese (Cantonese)': 'zh-HK', 'Hawaiian': 'hw', 'Irish': 'ga', 'Scottish Gaelic': 'gd', 'High Valyrian': 'hv', 'Welsh': 'cy', 'Klingon': 'tlh', 'Tagalog': 'tl', 'Bengali':'bn', 'Thai':'th'}
emojidict = {'en': '🇺🇸', 'sv': '🇸🇪', 'gn': '🇵🇾', 'yi': '🇮🇱', 'nv': '🇺🇸', 'fi': '🇫🇮', 'sw': '🇰🇪', 'zu': '🇿🇦', 'es': '🇪🇸', 'ja': '🇯🇵', 'eo': '<:flag_eo:1045425989934645379>', 'pt': '🇵🇹', 'hi': '🇮🇳', 'ko': '🇰🇷', 'it': '🇮🇹', 'vi': '🇻🇳', 'id': '🇮🇩', 'de': '🇩🇪', 'no-BO': '🇳🇴', 'pl': '🇵🇱', 'ro': '🇷🇴', 'el': '🇬🇷', 'ht': '🇭🇹', 'cs': '🇨🇿', 'ca': '🇪🇸', 'zh': '🇨🇳', 'nl-NL': '🇳🇱', 'la': '🇻🇦', 'tr': '🇹🇷', 'uk': '🇺🇦', 'ru': '🇷🇺', 'fr': '🇫🇷', 'hu': '🇭🇺', 'da': '🇩🇰', 'ar': '🇸🇦', 'he': '🇮🇱', 'zh-HK': '🇭🇰', 'hw': '🇺🇸', 'ga': '🇮🇪', 'gd': '🇬🇧', 'hv': '🇻🇦', 'cy': '🇬🇧', 'tlh': '🇻🇦', 'tl': '🇵🇭', 'bn': '🇧🇩', 'th': '🇹🇭'}

def name_to_code(name):
    return languages[name]

def code_to_name(code):
    return list(languages.keys())[list(languages.values()).index(code)]

def emoji(code):
    return emojidict[code]  # I'm not sure if this is the right way to do it, but it works