p = 1000
r = 7/100
tenth_year = p * (1 + r) ** 10 
thirtieth_year = p * (1 + r) ** 30
twentieth_year = p * (1 + r) ** 20

print(f"""
In 10 years >> {tenth_year:,.2f}
In 20 years >> {twentieth_year:,.2f}
In 30 years >> {thirtieth_year:,.2f}
""")


