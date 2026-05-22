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
    def Frequency_Table(ColumnName,dataset):
        Frequency_Table=pd.DataFrame(columns=['Unique_Values','Frequency','Relative_Frequency','Cumsum'])
        Frequency_Table['Unique_Values']=dataset[ColumnName].value_counts().index
        Frequency_Table['Frequency']=dataset[ColumnName].value_counts().values
        Frequency_Table['Relative_Frequency']=(Frequency_Table['Frequency']/103)
        Frequency_Table['Cumsum']=Frequency_Table['Relative_Frequency'].cumsum()
        return Frequency_Table
    def univariate(quan,dataset):
        Descriptive=pd.DataFrame(index=['Mean','Median','Mode','Q1:25%','Q2:50%','Q3:75%','99','Q4:100%','IQR','1.5rule','less','high','min','max'],columns=quan)
        for ColumnName in quan:
            Descriptive[ColumnName]['Mean']=dataset[ColumnName].mean()
            Descriptive[ColumnName]['Median']=dataset[ColumnName].median()
            Descriptive[ColumnName]['Mode']=dataset[ColumnName].mode()[0]
            Descriptive[ColumnName]['Q1:25%']=dataset.describe()[ColumnName]["25%"]
            Descriptive[ColumnName]['Q2:50%']=dataset.describe()[ColumnName]["50%"]
            Descriptive[ColumnName]['Q3:75%']=dataset.describe()[ColumnName]["75%"]
            Descriptive[ColumnName]['99']=np.percentile(dataset[ColumnName],40)
            Descriptive[ColumnName]['Q4:100%']=dataset.describe()[ColumnName]["max"]
            Descriptive[ColumnName]['IQR']=Descriptive[ColumnName]['Q3:75%']-Descriptive[ColumnName]['Q1:25%']
            Descriptive[ColumnName]['1.5rule']=1.5*Descriptive[ColumnName]['IQR']
            Descriptive[ColumnName]['less']=Descriptive[ColumnName]['Q1:25%']-Descriptive[ColumnName]['1.5rule']
            Descriptive[ColumnName]['high']=Descriptive[ColumnName]['Q3:75%']+Descriptive[ColumnName]['1.5rule']
            Descriptive[ColumnName]['min']=dataset[ColumnName].min()
            Descriptive[ColumnName]['max']=dataset[ColumnName].max()
        return Descriptive
    def outlier(less,high):
        less=[]
        high=[]
        for ColumnName in quan:
            if(Descriptive[ColumnName]['max']>Descriptive[ColumnName]['high']):
                high.append(ColumnName)
            if(Descriptive[ColumnName]['min']<Descriptive[ColumnName]['less']):
                less.append(ColumnName)
        return less,high
    def replace_outlier(less,high):
        for ColumnName in less:
            dataset[ColumnName][dataset[ColumnName]<Descriptive[ColumnName]['less']]=Descriptive[ColumnName]['less']
        for ColumnName in high:
            dataset[ColumnName][dataset[ColumnName]>Descriptive[ColumnName]['high']]=Descriptive[ColumnName]['high']
        return less,high
        
                        