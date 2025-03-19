def suma(a):
    return a+5

def division(a, b):
    c = a / b
    return c

def column_difference(df, col1, col2):
    return df[col1] - df[col2]

def column_sum(df, col1, col2):
    return df[col1] + df[col2]

def get_df_rename(connection, col1, col2):
    df = pd.read_sql("SELECT * FROM foo;", connection)
    df_o = df.rename(columns={col1: col2})
    return df_o

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()
