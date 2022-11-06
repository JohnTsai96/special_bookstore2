import streamlit as st
import requests
def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' 
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def app():
    bookstoreList = getAllBookstore()
    countyOption = getCountyOption(bookstoreList)
    st.header('特色書店小地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('選一下縣市', countyOption)
    specificBookstore = getSpecificBookstore(bookstoreList,county)
    num = len(specificBookstore)
    st.write(f"總共有{num}間書店")

def getCountyOption(items):
    optionList = []
    for item in items:
        name = item["cityName"][0:3]
        if name not in optionList:
            optionList.append(name)

    return optionList
def getSpecificBookstore(items,county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county not in name : continue
        for district in district:
            if district not in name:continue
            specificBookstoreList.append(name)
    return specificBookstoreList

def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write(item["intro"]) 
        expander.subheader('Address')
        expander.write(item["address"]) 
        expander.subheader('Open Time')
        expander.write(item["openTime"]) 
        expander.subheader('Email')
        expander.write(item["email"]) 
        expanderList.append(expander) 
    return expanderList    


if __name__ == '__main__':
    app()
