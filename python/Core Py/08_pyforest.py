# What is Pyforest?
# Pyforest is a Python library that allows you to import popular data science libraries lazily. This means that you can use these libraries without having to import them explicitly at the beginning of your code. Pyforest will automatically import the libraries when you first use them.


# To use Pyforest, you can simply install it using pip:
# pip install pyforest

# Once you have Pyforest installed, you can start using it in your code. For example, if you want to use the pandas library, you can simply use it without importing it:

active_imports() #this function will show you the libraries that have been imported lazily
df=pd.read_csv("https://winterolympicsmedals.com/medals.csv") #pandas is a popular data science library for data manipulation and analysis
print(df.head())
