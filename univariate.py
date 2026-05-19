class univariate:
    def quanqual(dataset):
        qual=[]
        quan=[]
        for ColumnName in dataset.columns:
            #print(ColumnName)
            if(dataset[ColumnName].dtypes=='O'):
                quan.append(ColumnName)
            else:
                qual.append(ColumnName)
        return qual,quan
        