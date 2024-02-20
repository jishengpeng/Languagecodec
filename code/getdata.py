# 下载common voice

from datasets import load_dataset


print(0)

# ['ab', 'af', 'am', 'ar', 'as', 'ast', 'az', 'ba', 'bas', 'be', 'bg', 'bn', 'br', 'ca', 'ckb', 'cnh', 'cs', 'cv', 'cy', 'da', 'de', 'dv', 'dyu', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy-NL', 'ga-IE', 'gl', 'gn', 'ha', 'he', 'hi', 'hsb', 'hu', 'hy-AM', 'ia', 'id', 'ig', 'is', 'it', 'ja', 'ka', 'kab', 'kk', 'kmr', 'ko', 'ky', 'lg', 'lij', 'lo', 'lt', 'ltg', 'lv', 'mdf', 'mhr', 'mk', 'ml', 'mn', 'mr', 'mrj', 'mt', 'myv', 'nan-tw', 'ne-NP', 'nhi', 'nl', 'nn-NO', 'oc', 'or', 'os', 'pa-IN', 'pl', 'ps', 'pt', 'quy', 'rm-sursilv', 'rm-vallader', 'ro', 'ru', 'rw', 'sah', 'sat', 'sc', 'sk', 'skr', 'sl', 'sq', 'sr', 'sv-SE', 'sw', 'ta', 'te', 'th', 'ti', 'tig', 'tk', 'tok', 'tr', 'tt', 'tw', 'ug', 'uk', 'ur', 'uz', 'vi', 'vot', 'yi', 'yo', 'yue', 'zgh', 'zh-CN', 'zh-HK', 'zh-TW']

ds=load_dataset("mozilla-foundation/common_voice_16_1","hu")

# https://huggingface.co/datasets/reach-vb/common_voice_16_1/resolve/main/audio/af/train/af_train_0.tar