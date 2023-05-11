#This code will use find and string slicing to extract the number at the end of the text.

text = "X-DSPAM-Confidence:    0.8475"
one = text.find('0')
two = text.find('5')
final = text[one : two+1]
final2 = float(final)
print(final2)