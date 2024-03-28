# Column names as specified
column_names = [
    "ID", "Age", "Gender", "Edu", "Country", "Ethn", "Neuro", "Extr", "Open",
    "Agree", "Consc", "Impul", "Sensat", "Alc", "Amphet", "Amyl", "Benzos",
    "Caff", "Can", "Choco", "Coke", "Crack", "Ecst", "Her", "Ket", "Leghighs",
    "LSD", "Meth", "Mush", "Nico", "Semeron", "VSA"
]

# Mapping from ordinal strings to numerical scale
ordinal_mapping = {
    'CL0': 0, 'CL1': 1, 'CL2': 2, 'CL3': 3, 'CL4': 4, 'CL5': 5, 'CL6': 6
}

# Columns containing ordinal data
ordinal_columns = [
    "Alc", "Amphet", "Amyl", "Benzos", "Caff", "Can", "Choco", "Coke", "Crack",
    "Ecst", "Her", "Ket", "Leghighs", "LSD", "Meth", "Mush", "Nico", "Semeron", "VSA"
]

feature_columns = ["Age", "Gender", "Edu", "Country", "Ethn", "Neuro", "Extr", "Open", "Agree", "Consc", "Impul", "Sensat"]

TARGET_DRUGS = ["Coke", "Her", "LSD", "Amphet", "Meth"]

def prepcessing_data(df):
    '''
    perform preprocessing
    '''

    # map ordinal to numerical
    for column in ordinal_columns:
        df[column] = df[column].map(ordinal_mapping)

    # remove overclaimers
    df = df[df['Semeron'] == 0]

    return df


def transform_target(df, target_drugs, threshold=2):
    df['target'] = df[target_drugs].gt(2).any(axis=1).astype(int)
    return df
