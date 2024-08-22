from enum import Enum


languages = {
    "Afrikaans": "afr_Latn",
    "Amharic": "amh_Ethi",
    "Arabic (Modern Standard Arabic)": "arb_Arab",
    "Armenian": "hye_Armn",
    "Asturian": "ast_Latn",
    "Belarusian": "bel_Cyrl",
    "Bengali": "ben_Beng",
    "Bosnian": "bos_Latn",
    "Bulgarian": "bul_Cyrl",
    "Burmese": "mya_Mymr",
    "Catalan": "cat_Latn",
    "Cebuano": "ceb_Latn",
    "Chinese (Simplified)": "zho_Hans",
    "Croatian": "hrv_Latn",
    "Czech": "ces_Latn",
    "Danish": "dan_Latn",
    "Dutch": "nld_Latn",
    "English": "eng_Latn",
    "Estonian": "est_Latn",
    "Finnish": "fin_Latn",
    "French": "fra_Latn",
    "Friulian": "fuv_Latn",
    "Galician": "glg_Latn",
    "Ganda": "lug_Latn",
    "Georgian": "kat_Geor",
    "German": "deu_Latn",
    "Greek": "ell_Grek",
    "Gujarati": "guj_Gujr",
    "Hausa": "hau_Latn",
    "Hebrew": "heb_Hebr",
    "Hindi": "hin_Deva",
    "Hungarian": "hun_Latn",
    "Icelandic": "isl_Latn",
    "Igbo": "ibo_Latn",
    "Indonesian": "ind_Latn",
    "Persian": "prs_Arab",
    "Irish": "gle_Latn",
    "Italian": "ita_Latn",
    "Japanese": "jpn_Jpan",
    "Javanese": "jav_Latn",
    "Kannada": "kan_Knda",
    "Kashmiri (Arabic script)": "khk_Cyrl",
    "Kashmiri (Devanagari script)": "pbt_Arab",
    "Kazakh": "kaz_Cyrl",
    "Khmer": "khm_Khmr",
    "Korean": "kor_Hang",
    "Lao": "lao_Laoo",
    "Latvian (Standard)": "lvs_Latn",
    "Lingala": "lin_Latn",
    "Lithuanian": "lit_Latn",
    "Luxembourgish": "ltz_Latn",
    "Macedonian": "mkd_Cyrl",
    "Malayalam": "mal_Mlym",
    "Malaysian": "zsm_Latn",
    "Marathi": "mar_Deva",
    "Nepali": "npi_Deva",
    "Northern Sotho": "nso_Latn",
    "Norwegian (Nynorsk)": "nno_Latn",
    "Occitan": "oci_Latn",
    "Odia (Oriya)": "ory_Orya",
    "Polish": "pol_Latn",
    "Portuguese": "por_Latn",
    "Punjabi": "pan_Guru",
    "Romanian": "ron_Latn",
    "Russian": "rus_Cyrl",
    "Serbian": "srp_Cyrl",
    "Sinhala": "sin_Sinh",
    "Slovak": "slk_Latn",
    "Slovenian": "slv_Latn",
    "Somali": "som_Latn",
    "South Azerbaijani": "azj_Latn",
    "Spanish": "spa_Latn",
    "Swahili": "swh_Latn",
    "Swedish": "swe_Latn",
    "Tagalog": "tgl_Latn",
    "Tamil": "tam_Taml",
    "Thai": "tha_Thai",
    "Turkish": "tur_Latn",
    "Ukrainian": "ukr_Cyrl",
    "Urdu": "urd_Arab",
    "Uzbek": "uzn_Latn",
    "Vietnamese": "vie_Latn",
    "Welsh": "cym_Latn",
    "Wolof": "wol_Latn",
    "Xhosa": "xho_Latn",
    "Yoruba": "yor_Latn",
    "Zulu": "zul_Latn",
}


class LanguageDropdownOptions(str, Enum):
    option1 = "Afrikaans"
    option2 = "Amharic"
    option3 = "Arabic (Modern Standard Arabic)"
    option4 = "Armenian"
    option5 = "Asturian"
    option6 = "Belarusian"
    option7 = "Bengali"
    option8 = "Bosnian"
    option9 = "Bulgarian"
    option10 = "Burmese"
    option11 = "Catalan"
    option12 = "Cebuano"
    option13 = "Chinese (Simplified)"
    option14 = "Croatian"
    option15 = "Czech"
    option16 = "Danish"
    option17 = "Dutch"
    option18 = "English"
    option19 = "Estonian"
    option20 = "Finnish"
    option21 = "French"
    option22 = "Friulian"
    option23 = "Galician"
    option24 = "Ganda"
    option25 = "Georgian"
    option26 = "German"
    option27 = "Greek"
    option28 = "Gujarati"
    option29 = "Hausa"
    option30 = "Hebrew"
    option31 = "Hindi"
    option32 = "Hungarian"
    option33 = "Icelandic"
    option34 = "Igbo"
    option35 = "Indonesian"
    option36 = "Persian"
    option37 = "Irish"
    option38 = "Italian"
    option39 = "Japanese"
    option40 = "Javanese"
    option41 = "Kannada"
    option42 = "Kashmiri (Arabic script)"
    option43 = "Kashmiri (Devanagari script)"
    option44 = "Kazakh"
    option45 = "Khmer"
    option46 = "Korean"
    option47 = "Lao"
    option48 = "Latvian (Standard)"
    option49 = "Lingala"
    option50 = "Lithuanian"
    option51 = "Luxembourgish"
    option52 = "Macedonian"
    option53 = "Malayalam"
    option54 = "Malaysian"
    option55 = "Marathi"
    option56 = "Nepali"
    option57 = "Northern Sotho"
    option58 = "Norwegian (Nynorsk)"
    option59 = "Occitan"
    option60 = "Odia (Oriya)"
    option61 = "Polish"
    option62 = "Portuguese"
    option63 = "Punjabi"
    option64 = "Romanian"
    option65 = "Russian"
    option66 = "Serbian"
    option67 = "Sinhala"
    option68 = "Slovak"
    option69 = "Slovenian"
    option70 = "Somali"
    option71 = "South Azerbaijani"
    option72 = "Spanish"
    option73 = "Swahili"
    option74 = "Swedish"
    option75 = "Tagalog"
    option76 = "Tamil"
    option77 = "Thai"
    option78 = "Turkish"
    option79 = "Ukrainian"
    option80 = "Urdu"
    option81 = "Uzbek"
    option82 = "Vietnamese"
    option83 = "Welsh"
    option84 = "Wolof"
    option85 = "Xhosa"
    option86 = "Yoruba"
    option87 = "Zulu"
