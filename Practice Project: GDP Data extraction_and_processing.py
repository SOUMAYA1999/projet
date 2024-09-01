URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
tables=pd.read_html(URL)
df=tables[3]
#df.head()
# Replace the column headers with column numbers
df.columns = range(df.shape[1])
#df.head()

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df=df[[0,2]]
df.columns=["Name of country","Value of GDP quoted by IMF"]

#df.head()

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df=df.iloc[1:11,:]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns=['Country','GDP (Million USD)']
df.to_csv("Country and GDP (Million USD).csv")
df.head(10)

# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df["GDP (Million USD)"]=df["GDP (Million USD)"].astype(int)

# Convert the GDP value in Million USD to Billion USD

df["GDP (Billion USD)"]=df["GDP (Million USD)"]*0.001
df.head()
