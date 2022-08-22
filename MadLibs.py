md="MadLibs"
#przykłady konkatenacji w python
"welcome to" + md
"welcome to {}".format(md)
f"welcome to {md}"

przym = input("Przymiotnik (ona): ")
czasow = input("Czasownik: ")
celeb = input("Celebryta: ")

madlib = f"""Nauka pythona jest {przym}.
Uczę sie pythona ponieważ w przyszłości chcę {czasow} dużo kasy.
Moim idolem jest {celeb}."""

print(madlib)
