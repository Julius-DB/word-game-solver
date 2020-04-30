import enchant
d_EN = enchant.Dict("en_US")
d_DK = enchant.Dict("da")
d_DE = enchant.Dict("de_DE")
d_FR = enchant.Dict("fr_FR")
d_ES = enchant.Dict("es_ES")
# Visit https://pyenchant.github.io/pyenchant/index.html for more information
print(enchant.list_languages()) # Gives a list of built-in dictionaries.


word = "Fødselsdag"
print(d_EN.check(word))
print(d_DK.check(word))
