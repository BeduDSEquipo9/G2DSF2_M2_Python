# Import Libraries
import pandas as pd

# READ CSV
df = pd.read_csv('MergedData.csv')
# Explore Dataset
print('shape:', df.shape)
print("describe", df.describe())
print("head", df.head(10))
print("Info", df.info)
print("columnas", df.columns)
lista_columnas = len(df.columns)
print("Numero de columnas:", lista_columnas)
"""
Listed Columns:
[10 rows x 54 columns]
columnas Index(['Unnamed: 0', 'zpid', 'id', 'lotId', 'imgSrc', 'hasImage', 'statusType',
       'statusText', 'detailUrl', 'latLong', 'units', 'variableData',
       'badgeInfo', 'buildingName', 'isBuilding', 'address', 'addressStreet',
       'addressState', 'addressCity', 'addressZipcode', 'providerListingId',
       'canSaveBuilding', 'has3DModel', 'isFeaturedListing', 'isSaved', 'list',
       'relaxed', 'streetViewMetadataURL', 'streetViewURL', 'area',
       'availabilityDate', 'baths', 'beds', 'countryCurrency',
       'hasAdditionalAttributions', 'hasVideo', 'hdpData', 'isHomeRec',
       'isUndisclosedAddress', 'isUserClaimingOwner', 'isUserConfirmedClaim',
       'isZillowOwned', 'pgapt', 'price', 'sgapt',
       'shouldShowZestimateAsPrice', 'unformattedPrice', 'zestimate',
       'brokerName', 'hasOpenHouse', 'openHouseDescription',
       'openHouseEndDate', 'openHouseStartDate', 'carouselPhotos'],  dtype='object')
Numero de columnas: 54
Describe columns:
"""
# REMOVE UNUSED COLUMNS FROM 54 kept X columns
df_dropped = df.drop(columns=['zpid', 'imgSrc', 'hasImage', 'statusType',
                              'statusText', 'detailUrl', 'latLong', 'variableData',
                              'badgeInfo', 'buildingName', 'isBuilding', 'address', 'addressStreet',
                              'providerListingId',
                              'canSaveBuilding', 'has3DModel', 'isFeaturedListing', 'isSaved', 'list',
                              'relaxed', 'streetViewMetadataURL', 'streetViewURL', 'area',
                              'availabilityDate', 'countryCurrency',
                              'hasAdditionalAttributions', 'hasVideo', 'hdpData', 'isHomeRec',
                              'isUndisclosedAddress', 'isUserClaimingOwner', 'isUserConfirmedClaim',
                              'isZillowOwned', 'pgapt', 'sgapt',
                              'shouldShowZestimateAsPrice', 'zestimate',
                              'brokerName', 'hasOpenHouse', 'openHouseDescription',
                              'openHouseEndDate', 'openHouseStartDate', 'carouselPhotos'])

print('shape:', df_dropped.shape)
print("describe", df_dropped.describe())
print("head", df_dropped.head(10))
print("Info:", df_dropped.info)
print("columnas", df_dropped.columns)
lista_columnas = len(df_dropped.columns)
print("Numero de columnas:", lista_columnas)
"""
Listed Columns:
[10 rows x 11 columns]
columnas Index(['Unnamed: 0', 'id', 'lotId', 'units', 'addressState', 'addressCity',
       'addressZipcode', 'baths', 'beds', 'price', 'unformattedPrice'],
      dtype='object')
Numero de columnas: 11
Describe columns: and why we kept them
"""
# df_dropped.to_csv('Data1_RemoveColumns.csv')
# CHECK MISSING DATA
missing_data = df_dropped.isna().sum()
print("IsNa's:", missing_data)
df_R1 = df_dropped
df_R1['units'] = df_R1['units'].str.split('}, {')
df_R1 = df_R1.explode('units').reset_index(drop=True)
cols = list(df_R1.columns)
cols.append(cols.pop(cols.index('id')))
df_R1 = df_R1[cols]

# print('='*80+'\n')
df_R1.to_csv('Data1_SplittingUnitInRows.csv')
# d=df_R1["units"].str.replace(r'[\x7B\x7D\x5B\x5D]', '')
#df_R1[['units_price2','units_beds2']] = df_R1['units'].str.split("\+", expand=True)
#df_R1.to_csv('Data2_SplittingUnitInColumns.csv')

df_R1["units"]=df_R1["units"].str.replace(r'[\x7B\x7D\x5B\x5D\+ \x27price\x27\x3A]', '')
df_R1.to_csv('Data2_RemovingbadCharsFromUnit.csv')

df_R1['unformattedPrice']=(df_R1['units'].str.split(',bds', expand=True))[0]
df_R1['beds']=(df_R1['units'].str.split(',bds', expand=True))[1]
df_R1["price"]=df_R1["price"].str.replace(r'\D', '')

df_R1['price']=pd.to_numeric(df_R1['price'])

df_R1.to_csv('Data3_SplitcolumnsfromUnit.csv')

def double_to_money(value):

    return f'${value}'

#df_R1['price']=df_R1['price'].map(double_to_money)

df_R1['baths'] = df_R1['baths'].fillna('Unknown')
df_R1['unformattedPrice'] = df_R1['unformattedPrice'].fillna(df_R1['price'])
df_R1['unformattedPrice']=df_R1['unformattedPrice'].str.replace(r'[\x24\x2C]', '')
df_R1['unformattedPrice'] = pd.to_numeric(df_R1['unformattedPrice'])

df_R1['lotId'] = df_R1['lotId'].fillna(df_R1['id'])
df_R1=df_R1.drop(columns=['Unnamed: 0', 'units','price','id'])
df_R1=df_R1.reset_index(drop=True)
column_name_mapping={
    'lotId':'LotId',
    'addressState':'State',
    'addressCity':'City',
    'addressZipcode':'Zipcode',
    'baths':'Baths',
    'beds':'Beds',
    'unformattedPrice':'Price'
}


df_R1 = df_R1.rename(columns=column_name_mapping)
df_R1.to_csv('Data4_SplitcolumnsfromUnit.csv')

print('shape:', df_R1.shape)
print("describe", df_R1.describe())
print("head", df_R1.head(10))
print("Info:", df_R1.info)
print("columnas", df_R1.columns)
lista_columnas = len(df_R1.columns)
print("Numero de columnas:", lista_columnas)
missing_data = df_R1.isna().sum()
print("IsNa's:", missing_data)
print("Tamaño:",df_R1.groupby('State').size())
print("Cuenta Valores1: ",df_R1.groupby('State')['City'].value_counts())
print("Cuenta Valores2: ",df_R1.groupby(['State','City'])['Zipcode'].value_counts())
#print("Moda 1: " ,df_R1.groupby('State')['City'].agg(pd.Series.mode))
print("Moda 2: " , df_R1.groupby('State')['City','Zipcode'].agg(pd.Series.mode))
print("Moda 3: " , df_R1.groupby('State')['City','Price'].agg(pd.Series.mode))
print(df_R1.groupby('State')['Price'].agg(['mean', 'median', 'std']))
print(df_R1.groupby(['State','City'])['Price'].agg(['mean', 'median', 'std']))
