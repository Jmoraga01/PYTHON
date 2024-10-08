import pandas as pd

archivo="hotel_booking.csv"
df=pd.read_csv(archivo)
print(df)

#print(df.head(10))
#print(df.tail(10))

#reg=df["n_children"]==1

#reg = df[df["n_children"]==1]
#print(reg.head(10))

#reg2 = df[df["n_adults"]==3]
#print(reg2.head(10))

#reg3 = df[df["n_children"]==1] & df[df["n_adults"]==2]
#print(reg3.head())

#reg4 = df[df.groupby("year").size()]
#ordenac = reg.sort_values(ascending=False)