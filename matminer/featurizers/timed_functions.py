
def timed_featurization(df, base_feat, feats_nofit=[], feats_fit=[] ):
    ''' Featurizers are separated in those that need fit and those that can be applied directly '''
    from matminer.featurizers.base import TimeTable
    Timetables=[]
    T=TimeTable()
    for feats in feats_nofit+feats_fit:
        if isinstance(feat,feats_fit):
            feat.fit(df[base_feat])
        (df_ofm,T) = feat.featurize_dataframe(df, base_feat,timetable=T)
        Timetables.append(T)
        T=TimeTable() # reset T
    Timetables=pd.concat(Timetables)
    Timetables=Timetables.groupby(Timetables.index).sum()
    return Timetables

