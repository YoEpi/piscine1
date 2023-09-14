theString = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN"

lowercase = theString.lower()

count_garden = theString.lower().count("garden") + theString[:: -1].lower().count("garden")
count_cat = theString.lower().count("cat") + theString[:: -1].lower().count("cat")
count_mice = theString.lower().count("mice") + theString[:: -1].lower().count("mice")

total_count = count_cat + count_garden + count_mice

print(total_count)