
def timed_featurization(df, base_feat, feats_nofit=[], feats_fit=[] ):
    ''' Featurizers are separated in those that need fit and those that can be applied directly '''
    from matminer.featurizers.base import TimeTable
    import pandas as pd
    import pickle
    Timetables=[]
    T=TimeTable()
    for feat in feats_nofit+feats_fit:
        print(feat)
        if isinstance(feat,tuple(x.__class__ for x in feats_fit)):
            feat.fit(df[base_feat])
        (df_ofm,T) = feat.featurize_dataframe(df, base_feat,timetable=T,ignore_errors=True)
        Timetables.append(T)
        T=TimeTable() # reset T
        with open("partial_Timetable.pkl","wb") as file:
            pickle.dump(T, file)

    Timetables=pd.concat(Timetables)
    Timetables=Timetables.groupby(Timetables.index).sum()
    return Timetables

