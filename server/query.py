from transpiler import *
import nltk

fol = nl_to_fol(input("Enter natural lang>> "))
satisfiers = kb_fol_query(fol)
print("APP1>> " + ', '.join(satisfiers))