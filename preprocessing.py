import pandas as pd

def feature_transactional_Price (cleanedData , lostRevenue):
    cleanedData['TransactionalPrice'] = cleanedData.UnitPrice * cleanedData.Quantity
    lostRevenue['TransactionalPrice'] = (lostRevenue.UnitPrice * lostRevenue.Quantity)
    return (cleanedData , lostRevenue)

def feature_weekday_month(cleanedData , lostRevenue):

    cleanedData['Month'] = cleanedData.InvoiceDate.dt.month
    cleanedData['WeekDay'] = cleanedData.InvoiceDate.dt.weekday
    lostRevenue['Month'] = lostRevenue.InvoiceDate.dt.month
    lostRevenue['WeekDay'] = lostRevenue.InvoiceDate.dt.weekday

    return (cleanedData, lostRevenue)
