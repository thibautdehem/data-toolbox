import pandas as pd
import datetime
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler, StandardScaler

pd.set_option('display.width', 200)

def drop_multiple_col(col_names_list, df):
  # Drop multiple columns based on their column names

    df.drop(col_names_list, axis=1, inplace=True)
    return df

def check_missing_data(df):
    # check for any missing data in the df (display in descending order)
    return df.isnull().sum().sort_values(ascending=False)

def remove_col_str(df):
    # remove a portion of string in a dataframe column - col_1
    df['col_1'].replace('\n', '', regex=True, inplace=True)

    # remove all the characters after &# (including &#) for column - col_1
    df['col_1'].replace(' &#.*', '', regex=True, inplace=True)

def remove_col_white_space(df,col):
    # remove white space at the beginning of string
    df[col] = df[col].str.lstrip()

def convert_str_datetime(df):
    #Convert datetime(String) to datetime(format we want)
    df.insert(loc=2, column='timestamp', value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S.%f'))


def cyclical_features(df,col):
    # feature as sin(X_i) and cos(X_i) to stay within -1 and 1
    df = df.copy()
    df[f'{feature}_sin'] = np.sin(df[col].astype('int'))
    df[f'{feature}_cos'] = np.sin(df[col].astype('int'))
    df.drop(columns=[col], inplace=True)
    return df

def get_categorical_columns(df):
    # get all the categorical columns
    cols = df.columns
    num_cols = df._get_numeric_data().columns
    cat_cols = list(set(cols) - set(num_cols))
    #categories = df.dtypes == object
    return cat_cols

def preprocesing_categorical_features(df):
    ''' Returns a new DataFrame with dummified columns'''
    df = df.copy()
    return pd.get_dummies(df.apply(lambda col: col.astype('category')))

def get_numerical_columns(df):
    # get all the categorical columns
    cols = df.columns
    num_cols = df._get_numeric_data().columns
    return num_cols

def preprocessing_numerical_features(df):
    '''
    Returns a new DataFrame with
    - Missing values replaced by Column Mean
    - Features Standard Scaled
    - Original Features names kept in the DataFrame
    '''
    df = df.copy()
    # Replace "missing values" in X by column mean
    tmp = ColumnTransformer([], remainder=SimpleImputer(strategy="mean")).fit_transform(df)

    # keep feature names
    for (col_index, col_name) in enumerate(list(df.columns)):
        df[col_name] = tmp[:,col_index]

    # Scale feature
    ct = ColumnTransformer([], remainder=StandardScaler())
    tmp = ct.fit_transform(df)
    # keep feature names
    for (col_index, col_name) in enumerate(list(df.columns)):
        df[col_name] = tmp[:, col_index]
    return df


