
def volume_change(df1, df2):
    def vol_diff_calc(df1ColLen, df2ColLen):
        return str(float((df2ColLen - df1ColLen) / df1ColLen) * 100) + "%"
         
    if df1.shape[1] != df2.shape[1]:  
        print('Invalid Dataset Shapes')
        return
    
    numCols = df1.shape[1]

    res = {i : vol_diff_calc(len(df1.iloc[:, i]), len(df2.iloc[:, i])) for i in range(numCols)}
    return res