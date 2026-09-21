import pandas as pd
import sqlite3

product_prices=pd.Series(
    [2999,15999,52999,4999,1999],
    index=["Wireless Earbuds","Smartphone","Laptop","Smartwatch","Bluetooth Speaker"]
)
print(product_prices)
print(product_prices.mean())
print(product_prices.sum())
print(product_prices.max())
print(product_prices.min())
print(product_prices.head())
print(product_prices.tail())

def func(x):
    return x*2

print(product_prices.apply(func))
print(product_prices.map(func))
print(product_prices.sort_values())
print(product_prices.sort_index())
print(product_prices.value_counts())

data={
    "Product":["Wireless Earbuds","Smartphone","Laptop","Smartwatch","Bluetooth Speaker"],
    "Brand":["SoundMax","TechNova","ByteCore","TimeTrack","EchoBoom"],
    "Price":[2999,15999,52999,4999,1999],
    "Stock":[50,30,20,40,60]
}

df=pd.DataFrame(data)
print(df)

connection=sqlite3.connect("inventory.db")
df.to_sql("inventory",connection,if_exists="replace",index=False)
df_sql=pd.read_sql("SELECT * FROM inventory",connection)
print(df_sql)
connection.close()

print(df["Product"])
print(df[["Product","Price"]])

filtered_df=df[df["Price"]>10000]
print(filtered_df)

print(df.loc[1,"Product"])
print(df.iloc[1,2])

print(df.dropna())
print(df.fillna(0))
print(df.select_dtypes(include="number").interpolate())

df["Price"]=df["Price"].astype(float)

print(df.info())
print(df.describe())

df.rename(columns={"Product":"Product Name"},inplace=True)
print(df)

df.drop(columns=["Stock"],inplace=True)
print(df)

data2={
    "Product":["Wireless Earbuds","Smartphone","Laptop","Smartwatch","Bluetooth Speaker"],
    "Brand":["SoundMax","TechNova","ByteCore","TimeTrack","EchoBoom"],
    "Price":[2999,15999,52999,4999,1999],
    "Stock":[50,30,20,40,60]
}

df=pd.DataFrame(data2)

grouped=df.groupby("Brand")["Price"].mean()
print(grouped)

print(df.groupby("Brand").agg({"Price":["mean","max","min"]}))

print(df.sort_values(by="Price",ascending=False))

df["Rank"]=df["Price"].rank(ascending=False)
print(df)

df1=df.head(3)
df2=df.tail(2)

df_combined=pd.concat([df1,df2],axis=0)
print(df_combined)

df_combined=pd.concat(
    [df1.reset_index(drop=True),df2.reset_index(drop=True)],
    axis=1
)
print(df_combined)

df3=pd.DataFrame({
    "Product":["Wireless Earbuds","Smartphone","Laptop"],
    "Category":["Audio","Mobile","Computer"]
})

df4=pd.DataFrame({
    "Product":["Wireless Earbuds","Smartphone","Laptop"],
    "Discount":[10,15,20]
})

df_merged=pd.merge(df3,df4,on="Product",how="inner")
print(df_merged)

pivot_df=df.pivot_table(
    values="Price",
    index="Brand",
    columns="Stock",
    aggfunc="mean"
)
print(pivot_df)

cross_tab=pd.crosstab(df["Brand"],df["Stock"])
print(cross_tab)

time_data={
    "Purchase Date":["2026-01-15","2026-01-20","2026-02-10","2026-02-15","2026-03-05"],
    "Price":[2999,15999,52999,4999,1999]
}

time_df=pd.DataFrame(time_data)

time_df["Purchase Date"]=pd.to_datetime(time_df["Purchase Date"])
time_df.set_index("Purchase Date",inplace=True)

print(time_df)
print(time_df.resample("M").mean())

df["Price"].plot(kind="bar",title="Product Prices")
df.plot(x="Product",y="Price",kind="scatter",title="Product Price Distribution")