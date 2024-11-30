from django.utils.translation import gettext_lazy as _

CURRENCY_CHOICES = [
    ("DZD", _("Algerian Dinar")),
    ("AOA", _("Angolan Kwanza")),
    ("BWP", _("Botswana Pula")),
    ("BIF", _("Burundi Franc")),
    ("CVE", _("Cape Verde Escudo")),
    ("XAF", _("Central African CFA Franc")),
    ("KMF", _("Comorian Franc")),
    ("CDF", _("Congolese Franc")),
    ("DJF", _("Djiboutian Franc")),
    ("EGP", _("Egyptian Pound")),
    ("ERN", _("Eritrean Nakfa")),
    ("SZL", _("Eswatini Lilangeni")),
    ("ETB", _("Ethiopian Birr")),
    ("GMD", _("Gambian Dalasi")),
    ("GHS", _("Ghanaian Cedi")),
    ("GNF", _("Guinean Franc")),
    ("KES", _("Kenyan Shilling")),
    ("LSL", _("Lesotho Loti")),
    ("LRD", _("Liberian Dollar")),
    ("LYD", _("Libyan Dinar")),
    ("MGA", _("Malagasy Ariary")),
    ("MWK", _("Malawian Kwacha")),
    ("MRU", _("Mauritanian Ouguiya")),
    ("MUR", _("Mauritian Rupee")),
    ("MAD", _("Moroccan Dirham")),
    ("MZN", _("Mozambican Metical")),
    ("NAD", _("Namibian Dollar")),
    ("NGN", _("Nigerian Naira")),
    ("RWF", _("Rwandan Franc")),
    ("STN", _("São Tomé and Príncipe Dobra")),
    ("SCR", _("Seychellois Rupee")),
    ("SLL", _("Sierra Leonean Leone")),
    ("SOS", _("Somali Shilling")),
    ("ZAR", _("South African Rand")),
    ("SSP", _("South Sudanese Pound")),
    ("SDG", _("Sudanese Pound")),
    ("TZS", _("Tanzanian Shilling")),
    ("TND", _("Tunisian Dinar")),
    ("UGX", _("Ugandan Shilling")),
    ("XOF", _("West African CFA Franc")),
    ("ZMW", _("Zambian Kwacha")),
    ("ZWL", _("Zimbabwean Dollar")),
    ("ARS", _("Argentine Peso")),
    ("BSD", _("Bahamian Dollar")),
    ("BBD", _("Barbadian Dollar")),
    ("BZD", _("Belize Dollar")),
    ("BMD", _("Bermudian Dollar")),
    ("BOB", _("Bolivian Boliviano")),
    ("BRL", _("Brazilian Real")),
    ("CAD", _("Canadian Dollar")),
    ("CLP", _("Chilean Peso")),
    ("COP", _("Colombian Peso")),
    ("CRC", _("Costa Rican Colón")),
    ("CUP", _("Cuban Peso")),
    ("DOP", _("Dominican Peso")),
    ("XCD", _("Eastern Caribbean Dollar")),
    ("USD", _("Ecuadorian Dollar")),
    ("USD", _("El Salvador Dollar")),
    ("FKP", _("Falkland Islands Pound")),
    ("GTQ", _("Guatemalan Quetzal")),
    ("GYD", _("Guyanaese Dollar")),
    ("HTG", _("Haitian Gourde")),
    ("HNL", _("Honduran Lempira")),
    ("JMD", _("Jamaican Dollar")),
    ("MXN", _("Mexican Peso")),
    ("NIO", _("Nicaraguan Córdoba")),
    ("PAB", _("Panamanian Balboa")),
    ("PYG", _("Paraguayan Guaraní")),
    ("PEN", _("Peruvian Sol")),
    ("SRD", _("Surinamese Dollar")),
    ("TTD", _("Trinidad and Tobago Dollar")),
    ("USD", _("United States Dollar")),
    ("UYU", _("Uruguayan Peso")),
    ("VES", _("Venezuelan Bolívar")),
    ("AFN", _("Afghan Afghani")),
    ("AMD", _("Armenian Dram")),
    ("AZN", _("Azerbaijani Manat")),
    ("BHD", _("Bahraini Dinar")),
    ("BDT", _("Bangladeshi Taka")),
    ("BTN", _("Bhutanese Ngultrum")),
    ("BND", _("Brunei Dollar")),
    ("KHR", _("Cambodian Riel")),
    ("CNY", _("Chinese Yuan")),
    ("GEL", _("Georgian Lari")),
    ("HKD", _("Hong Kong Dollar")),
    ("INR", _("Indian Rupee")),
    ("IDR", _("Indonesian Rupiah")),
    ("IRR", _("Iranian Rial")),
    ("IQD", _("Iraqi Dinar")),
    ("ILS", _("Israeli New Shekel")),
    ("JPY", _("Japanese Yen")),
    ("JOD", _("Jordanian Dinar")),
    ("KZT", _("Kazakhstani Tenge")),
    ("KWD", _("Kuwaiti Dinar")),
    ("KGS", _("Kyrgyzstani Som")),
    ("LAK", _("Lao Kip")),
    ("LBP", _("Lebanese Pound")),
    ("MYR", _("Malaysian Ringgit")),
    ("MVR", _("Maldivian Rufiyaa")),
    ("MNT", _("Mongolian Tögrög")),
    ("MMK", _("Myanmar Kyat")),
    ("NPR", _("Nepalese Rupee")),
    ("OMR", _("Omani Rial")),
    ("PKR", _("Pakistani Rupee")),
    ("PHP", _("Philippine Peso")),
    ("QAR", _("Qatari Riyal")),
    ("SAR", _("Saudi Riyal")),
    ("SGD", _("Singapore Dollar")),
    ("KRW", _("South Korean Won")),
    ("LKR", _("Sri Lankan Rupee")),
    ("SYP", _("Syrian Pound")),
    ("TJS", _("Tajikistani Somoni")),
    ("THB", _("Thai Baht")),
    ("TMT", _("Turkmenistan Manat")),
    ("AED", _("United Arab Emirates Dirham")),
    ("UZS", _("Uzbekistani Som")),
    ("VND", _("Vietnamese Đồng")),
    ("YER", _("Yemeni Rial")),
    ("ALL", _("Albanian Lek")),
    ("EUR", _("Andorran Euro")),
    ("BYN", _("Belarusian Ruble")),
    ("BAM", _("Bosnia and Herzegovina Convertible Mark")),
    ("BGN", _("Bulgarian Lev")),
    ("HRK", _("Croatian Kuna")),
    ("CZK", _("Czech Koruna")),
    ("DKK", _("Danish Krone")),
    ("EUR", _("Euro")),
    ("HUF", _("Hungarian Forint")),
    ("ISK", _("Icelandic Króna")),
    ("MKD", _("Macedonian Denar")),
    ("MDL", _("Moldovan Leu")),
    ("EUR", _("Montenegrin Euro")),
    ("NOK", _("Norwegian Krone")),
    ("PLN", _("Polish Złoty")),
    ("RON", _("Romanian Leu")),
    ("RUB", _("Russian Ruble")),
    ("RSD", _("Serbian Dinar")),
    ("CHF", _("Swiss Franc")),
    ("TRY", _("Turkish Lira")),
    ("UAH", _("Ukrainian Hryvnia")),
    ("GBP", _("United Kingdom Pound")),
    ("AUD", _("Australian Dollar")),
    ("FJD", _("Fijian Dollar")),
    ("AUD", _("Kiribati Dollar")),
    ("NZD", _("New Zealand Dollar")),
    ("PGK", _("Papua New Guinean Kina")),
    ("WST", _("Samoan Tālā")),
    ("SBD", _("Solomon Islands Dollar")),
    ("TOP", _("Tongan Paʻanga")),
    ("AUD", _("Tuvaluan Dollar")),
    ("VUV", _("Vanuatu Vatu")),
]