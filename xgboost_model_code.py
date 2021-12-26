# -*- coding: utf-8 -*-
"""XGBoost_Caroline

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fdsOQuZKzoYm_dke7crBL1uRgMjnBVi3
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import log_loss, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/BU MSBA /Cobras-Humana May Case Competition/CleanData2.csv")

df.head()

train_dataSet=df[[
"covid_vaccination",
'cons_hxwearbl',
'cons_rxadhs',
'cons_rxadhm',
'cons_rxmaint',
'cons_stlnindx',
'cons_estinv30_rc',
'cons_hxmioc',
'est_age',
'rx_days_since_last_script_0to3m_b4',
'rx_days_since_last_script_6to9m_b4',
'rx_maint_pmpm_ct_9to12m_b4',
'rx_generic_pmpm_ct_0to3m_b4',
'rx_hum_16_pmpm_ct',
'cons_lwcm07',
'atlas_pct_fmrkt_wic16',
'pdc_lip',
'rx_nonbh_mbr_resp_pmpm_cost_6to9m_b4',
'rx_nonbh_mbr_resp_pmpm_cost',
'atlas_pct_loclfarm12',
'rwjf_mv_deaths_rate',
'atlas_convspth14',
'rwjf_uninsured_child_pct',
'rwjf_uninsured_adults_pct',
'rwjf_uninsured_pct',
'credit_hh_nonmtgcredit_60dpd',
'credit_num_nonmtgcredit_60dpd',
'credit_hh_1stmtgcredit',
'credit_hh_bankcard_severederog',
'credit_bal_nonmtgcredit_60dpd',
'credit_hh_bankcardcredit_60dpd',
'credit_bal_mtgcredit_new',
'atlas_hiamenity',
'atlas_farm_to_school13',
'atlas_hipov_1115',
'atlas_low_employment_2015_update',
'cms_orig_reas_entitle_cd',
'atlas_type_2015_update',
'cons_ltmedicr',
'rx_gpi2_33_pmpm_ct_0to3m_b4',
'rx_gpi2_72_pmpm_ct_6to9m_b4',
'hum_region_CALIFORNIA/NEVADA',
'hum_region_CENTRAL',
'hum_region_CENTRAL WEST',
'hum_region_EAST',
'hum_region_EAST CENTRAL',
'hum_region_FLORIDA',
'hum_region_GREAT LAKES/CENTRAL NORTH',
'hum_region_GULF STATES',
'hum_region_INTERMOUNTAIN',
'hum_region_MID-ATLANTIC/NORTH CAROLINA',
'hum_region_MID-SOUTH',
'hum_region_NORTHEAST',
'hum_region_PACIFIC',
'hum_region_PR',
'hum_region_SOUTHEAST',
'hum_region_TEXAS']]



train_dataSet_2=df[['covid_vaccination',
'hum_region_CALIFORNIA/NEVADA',
'hum_region_CENTRAL',
'hum_region_CENTRAL WEST',
'hum_region_EAST',
'hum_region_EAST CENTRAL',
'hum_region_FLORIDA',
'hum_region_GREAT LAKES/CENTRAL NORTH',
'hum_region_GULF STATES',
'hum_region_INTERMOUNTAIN',
'hum_region_MID-ATLANTIC/NORTH CAROLINA',
'hum_region_MID-SOUTH',
'hum_region_NORTHEAST',
'hum_region_PACIFIC',
'hum_region_PR',
'hum_region_SOUTHEAST',
'hum_region_TEXAS','cons_hxwearbl',
'cons_rxadhs',
'cons_rxadhm',
'cons_rxmaint',
'cons_stlnindx',
'cons_estinv30_rc',
'cons_hxmioc',
'est_age',
'rx_days_since_last_script_0to3m_b4',
'rx_days_since_last_script_6to9m_b4',
'rx_maint_pmpm_ct_9to12m_b4',
'rx_generic_pmpm_ct_0to3m_b4',
'rx_hum_16_pmpm_ct',
'cons_lwcm07',
'atlas_pct_fmrkt_wic16',
'pdc_lip',
'rx_nonbh_mbr_resp_pmpm_cost_6to9m_b4',
'rx_nonbh_mbr_resp_pmpm_cost',
'atlas_pct_loclfarm12',
'rwjf_mv_deaths_rate',
'atlas_convspth14',
'rwjf_uninsured_child_pct',
'rwjf_uninsured_adults_pct',
'rwjf_uninsured_pct',
'credit_hh_nonmtgcredit_60dpd',
'credit_num_nonmtgcredit_60dpd',
'credit_hh_1stmtgcredit',
'credit_hh_bankcard_severederog',
'credit_bal_nonmtgcredit_60dpd',
'credit_hh_bankcardcredit_60dpd',
'credit_bal_mtgcredit_new',
'atlas_hiamenity',
'atlas_farm_to_school13',
'atlas_hipov_1115',
'atlas_low_employment_2015_update',
'cms_orig_reas_entitle_cd',
'atlas_type_2015_update',
'cons_ltmedicr',
'rx_gpi2_33_pmpm_ct_0to3m_b4',
'rx_gpi2_72_pmpm_ct_6to9m_b4']]

import pandas as pd

# Use 3 decimal places in output display
#pd.set_option("display.precision", 3)

# Don't wrap repr(DataFrame) across additional lines
pd.set_option("display.expand_frame_repr", False)

# Set max rows displayed in output to 25
pd.set_option("display.max_rows",170)

# We can plot a histogram of training hours
plt.figure(figsize=[12,8])
sns.histplot(data=df, x="est_age", hue="covid_vaccination", palette="rocket")
plt.title("Histogram of Training Hours")

df.groupby(["est_age","covid_vaccination"])["covid_vaccination"].count()

new_cols = train_dataSet.columns[~train_dataSet.columns.isin(train_dataSet_2.columns)]

new_cols

train_dataSet.info()

train_dataSet["rx_gpi2_33_pmpm_ct_0to3m_b4"].unique()

y = train_dataSet["covid_vaccination"]
y.shape

y

x = train_dataSet.drop("covid_vaccination", axis=1)

x.shape

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
# 
# from xgboost import XGBClassifier
# #xgb = XGBClassifier(nthread=4, seed=0)
# # 'subsamples': 0.23, 'scale_pos_weight': 6, 'n_estimators': 130, 'max_depth': 7, 'learning_rate': 0.1, 'colsample_bytrees': 0.8, 'colsample_bylevel': 0.1, 'min_child_weight': 1,
# #xgb = XGBClassifier(subsample= 0.7, scale_pos_weight= 6, reg_lambda= 0.0001, reg_alpha= 1e-12, n_estimators= 200, min_child_weight= 5, max_depth= 3, learning_rate= 0.1, gamma=0.9, colsample_bytree= 0.7)
# xgb = XGBClassifier(subsamples= 0.23, scale_pos_weight= 6, n_estimators=130, max_depth= 7, learning_rate= 0.1, colsample_bytrees=0.8, colsample_bylevel= 0.1) #, min_child_weight= 1) #,min_split_loss= 17.09, reg_lambda= 0.0001,reg_alpha= 1e-09,gamma=1.0)
# #xgb = XGBClassifier(learning_rate=0.62, max_depth= 96, subsample= 0.58, min_split_loss= 17.09, min_child_weight= 41.09, colsample_bytree= 0.95, colsample_bylevel= 0.97, colsample_bynode= 0.69, reg_lambda= 6.49, reg_alpha= 1.21)
# #{'subsample': 0.4, 'scale_pos_weight': 3, 'reg_lambda': 0.0001, 'reg_alpha': 1e-09, 'n_estimators': 100, 'min_child_weight': 1, 'max_depth': 2, 'learning_rate': 0.1, 'gamma': 1.0, 'colsample_bytree': 0.8}
# xgb.fit(X_train, y_train,eval_set=[(X_train,y_train),(X_test,y_test)],
#           verbose=20,eval_metric='auc')
# 
# from sklearn.metrics import roc_auc_score
# y_pred_xgb = xgb.predict_proba(X_test)[:, 1]
# print(roc_auc_score(y_test, y_pred_xgb))
# 
# from sklearn.metrics import classification_report
# y_estimate_xgb = xgb.predict(X_test)
# print(classification_report(y_test, y_estimate_xgb))

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
# 
# from xgboost import XGBClassifier
# #xgb = XGBClassifier(nthread=4, seed=0)
# # 'subsamples': 0.23, 'scale_pos_weight': 6, 'n_estimators': 130, 'max_depth': 7, 'learning_rate': 0.1, 'colsample_bytrees': 0.8, 'colsample_bylevel': 0.1, 'min_child_weight': 1,
# #xgb = XGBClassifier(subsample= 0.7, scale_pos_weight= 6, reg_lambda= 0.0001, reg_alpha= 1e-12, n_estimators= 200, min_child_weight= 5, max_depth= 3, learning_rate= 0.1, gamma=0.9, colsample_bytree= 0.7)
# xgb = XGBClassifier(subsamples= 0.23, scale_pos_weight= 6, n_estimators=130, max_depth= 7, learning_rate= 0.1, colsample_bytrees=0.8, colsample_bylevel= 0.1,min_child_weight= 5) #, min_child_weight= 1) #,min_split_loss= 17.09, reg_lambda= 0.0001,reg_alpha= 1e-09,gamma=1.0)
# #xgb = XGBClassifier(learning_rate=0.62, max_depth= 96, subsample= 0.58, min_split_loss= 17.09, min_child_weight= 41.09, colsample_bytree= 0.95, colsample_bylevel= 0.97, colsample_bynode= 0.69, reg_lambda= 6.49, reg_alpha= 1.21)
# #{'subsample': 0.4, 'scale_pos_weight': 3, 'reg_lambda': 0.0001, 'reg_alpha': 1e-09, 'n_estimators': 100, 'min_child_weight': 1, 'max_depth': 2, 'learning_rate': 0.1, 'gamma': 1.0, 'colsample_bytree': 0.8}
# xgb.fit(X_train, y_train,eval_set=[(X_train,y_train),(X_test,y_test)],
#           verbose=20,eval_metric='rmse')
# 
# from sklearn.metrics import roc_auc_score
# y_pred_xgb = xgb.predict_proba(X_test)[:, 1]
# print(roc_auc_score(y_test, y_pred_xgb))
# 
# from sklearn.metrics import classification_report
# y_estimate_xgb = xgb.predict(X_test)
# print(classification_report(y_test, y_estimate_xgb))

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
# 
# from xgboost import XGBClassifier
# #xgb = XGBClassifier(nthread=4, seed=0)
# # 'subsamples': 0.23, 'scale_pos_weight': 6, 'n_estimators': 130, 'max_depth': 7, 'learning_rate': 0.1, 'colsample_bytrees': 0.8, 'colsample_bylevel': 0.1, 'min_child_weight': 1,
# #xgb = XGBClassifier(subsample= 0.7, scale_pos_weight= 6, reg_lambda= 0.0001, reg_alpha= 1e-12, n_estimators= 200, min_child_weight= 5, max_depth= 3, learning_rate= 0.1, gamma=0.9, colsample_bytree= 0.7)
# xgb = XGBClassifier(subsamples= 0.23, scale_pos_weight= 6, n_estimators=130, max_depth= 7, learning_rate= 0.1, colsample_bytrees=0.8, colsample_bylevel= 0.1,min_child_weight= 5) #, min_child_weight= 1) #,min_split_loss= 17.09, reg_lambda= 0.0001,reg_alpha= 1e-09,gamma=1.0)
# #xgb = XGBClassifier(learning_rate=0.62, max_depth= 96, subsample= 0.58, min_split_loss= 17.09, min_child_weight= 41.09, colsample_bytree= 0.95, colsample_bylevel= 0.97, colsample_bynode= 0.69, reg_lambda= 6.49, reg_alpha= 1.21)
# #{'subsample': 0.4, 'scale_pos_weight': 3, 'reg_lambda': 0.0001, 'reg_alpha': 1e-09, 'n_estimators': 100, 'min_child_weight': 1, 'max_depth': 2, 'learning_rate': 0.1, 'gamma': 1.0, 'colsample_bytree': 0.8}
# xgb.fit(X_train, y_train,eval_set=[(X_train,y_train),(X_test,y_test)],
#           verbose=20,eval_metric='rmse')
# 
# from sklearn.metrics import roc_auc_score
# y_pred_xgb = xgb.predict_proba(X_test)[:, 1]
# print(roc_auc_score(y_test, y_pred_xgb))
# 
# from sklearn.metrics import classification_report
# y_estimate_xgb = xgb.predict(X_test)
# print(classification_report(y_test, y_estimate_xgb))

xgb = XGBClassifier(nthread=4, seed=0)

|from sklearn import metrics
auc = metrics.roc_auc_score(y_test, y_pred_xgb)
print(auc)
false_positive_rate, true_positive_rate, thresolds = metrics.roc_curve(y_test, y_pred_xgb)
print(false_positive_rate,true_positive_rate)
plt.figure(figsize=(10, 8), dpi=100)
plt.axis('scaled')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.title("AUC & ROC Curve")
plt.plot(false_positive_rate, true_positive_rate, 'g')
plt.fill_between(false_positive_rate, true_positive_rate, facecolor='lightgreen', alpha=0.7)
plt.text(0.95, 0.05, 'AUC = %0.4f' % auc, ha='right', fontsize=12, weight='bold', color='blue')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()

from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred, pos_label=1)
roc_auc = auc(fpr, tpr) 

plt.figure(figsize=(10, 10))
plt.plot(fpr, tpr, 'b',label='AUC = %0.2f'% roc_auc)
plt.legend(loc='lower right', fontsize=15)
plt.plot([0, 1], [0, 1], color='black', linestyle='--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.tick_params(labelsize=13)
plt.xlabel('False Positive Rate', fontsize=15) 
plt.ylabel('True Positive Rate', fontsize=15)  
plt.savefig('roc.png')

feature_importance = pd.DataFrame({'feature':x.columns, 'importance':xgb.feature_importances_}).sort_values('importance',ascending=False).reset_index().drop(columns='index')
fig, ax = plt.subplots()
fig.set_size_inches(8.27,15)
plt.title('Feature Importance Plot')
sns.barplot(x='importance',y='feature',ax=ax,data=feature_importance)

feature_importance = pd.DataFrame({'feature':x.columns, 'importance':xgb.feature_importances_}).sort_values('importance',ascending=False).reset_index().drop(columns='index')
fig, ax = plt.subplots()
fig.set_size_inches(8.27,15)
plt.title('Feature Importance Plot')
sns.barplot(x='importance',y='feature',ax=ax,data=feature_importance)

holdout = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/BU MSBA /Cobras-Humana May Case Competition/holdout09.csv')

holdout.head()

holdout.shape

y_holdout = xgb.predict_proba(holdout.drop('ID',axis=1))
print(y_holdout[:,1])

pred = y_holdout[:,1]

holdout["SCORE"] = pred
holdout["RANK"] = holdout["SCORE"].rank(ascending=False).astype('int64')
holdout.sort_values("SCORE",inplace=True, ascending=False)
holdout[["ID","SCORE","RANK"]].to_csv('/content/drive/MyDrive/Colab Notebooks/BU MSBA /Cobras-Humana May Case Competition/Aaron_Wen_20211008.csv')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(x, y)
# 
# from sklearn.model_selection import RandomizedSearchCV
# from xgboost import XGBClassifier
# xgb = XGBClassifier(nthread=1, objective='binary:logistic', seed=0) 
# parameters = {'n_estimators':range(80,201,10), 
#               'min_child_weight': range(1,7,1),
#               'max_depth': range(1,9,1),
#               'colsample_bytree': [i / 10.0 for i in range(2, 11)],
#               'gamma': [i / 10.0 for i in range(3, 11)],
#               'subsample': [i / 10.0 for i in range(1, 11)], 
#               'reg_alpha': [1e-14,1e-13,1e-12,1e-11,1e-10,1e-9,1e-8], 
#               'reg_lambda': [1e-05,0.0001,0.001,0.010,1,1,10,100],
#               'learning_rate': [0.01,0.05,0.1,0.5,1],
#               'scale_pos_weight': [1, 3, 6]}
# # Instantiate the RandomizedSearchCV object: searcher_xgb
# searcher_xgb = RandomizedSearchCV(xgb, parameters, scoring="roc_auc", n_jobs=4, random_state=0)
# # Fit it to the data
# searcher_xgb.fit(X_train, y_train)
# 
# # Print the tuned parameters and score
# print("Best CV params", searcher_xgb.best_params_)
# print("Best score: ", searcher_xgb.best_score_)

, test_size=0.4, random_state=0

import numpy as np

# Commented out IPython magic to ensure Python compatibility.
# %%time
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(x, y)
# 
# from sklearn.model_selection import RandomizedSearchCV
# from xgboost import XGBClassifier
# xgb = XGBClassifier(nthread=1, objective='binary:logistic', seed=0) 
# parameters = {'n_estimators':range(80,201,10), 
#               'max_depth': range(1,9,1),
#               'colsample_bytrees': np.linspace(0.1, 1.0, 10),
#               'colsample_bylevel': np.linspace(0.1, 1.0, 10),
#               'subsamples': np.linspace(0.01, 1.0, 10),
#               'learning_rate': [0.01,0.05,0.1,0.5,1],
#               'scale_pos_weight': [1, 3, 6]}
# # Instantiate the RandomizedSearchCV object: searcher_xgb
# searcher_xgb = RandomizedSearchCV(xgb, parameters, scoring="roc_auc", n_jobs=4, random_state=0)
# # Fit it to the data
# searcher_xgb.fit(X_train, y_train)
# 
# # Print the tuned parameters and score
# print("Best CV params", searcher_xgb.best_params_)
# print("Best score: ", searcher_xgb.best_score_)

from sklearn.metrics import roc_auc_score
y_pred_xgb = searcher_xgb.best_estimator_.predict_proba(X_test)[:, 1]
print('auc score: ', roc_auc_score(y_test, y_pred_xgb))

from sklearn.metrics import classification_report
y_estimate_xgb = searcher_xgb.best_estimator_.predict(X_test)
print(classification_report(y_test, y_estimate_xgb))



holdout = pd.read_csv('/content/drive/MyDrive/BU MSBA /Cobras-Humana May Case Competition/keyfeatures.csv')

y_holdout = searcher_xgb.best_estimator_.predict_proba(holdout.drop("ID", axis=1))[:, 1]
print(y_holdout[:,1])