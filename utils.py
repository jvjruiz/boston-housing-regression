def pre_processing_pipeline(data):
    '''
    pre-processing pipeline for incoming data
    '''
    # removing these columns as they were deemed statistically insiginificant by linear regression analysis
    remove_columns = ['CRIM', 'INDUS', 'NOX', 'AGE', 'RAD']
    
    # drop the rows with null values from the dataset
    data = data.dropna()
    
    for column in remove_columns:
        if column in data.columns:
            data = data.drop(column, axis=1)
    
    return data