from django.shortcuts import *
import joblib
import numpy as np

model_path = r'C:\virtual enviroments\supply chain prediction\datascience\new_data2\predictions\supplymodel.pkl'
scaler_path = r'C:\virtual enviroments\supply chain prediction\datascience\new_data2\predictions\scaler.pkl'



model_ = joblib.load(model_path,'rb')
scaler = joblib.load(scaler_path,'rb')


data_ = {'Days for shipment (scheduled)': 0,
        'Late_delivery_risk': 0,
        'Latitude': 0,
        'Longitude': 0,
        'Order Item Discount': 0,
        'Order Item Discount Rate': 0,
        'Order Item Profit Ratio': 0,
        'Order Item Quantity': 0,
        'Sales': 0,
        'Customer Segment':0,
        'Market':0,
        'Type':0,
        'Department Name':0,
        'Category Name':0,}


# Create your views here.
def home2(request):
    global context
    if request.method=='POST':
        data_['Days for shipment (scheduled)'] = float(request.POST.get('DFSS'))
        data_['Late_delivery_risk'] = float(request.POST.get('LDRR'))
        data_['Latitude'] = float(request.POST.get('LTT'))
        data_['Longitude'] = float(request.POST.get('LGG'))
        data_['Order Item Discount Rate'] = float(request.POST.get('OIDRR'))
        data_['Order Item Profit Ratio'] = float(request.POST.get('OIPRR'))
        data_['Order Item Discount'] = float(request.POST.get('OIDD'))
        data_['Order Item Quantity'] = float(request.POST.get('OIQQ'))
        data_['Sales'] = float(request.POST.get('Saa'))

        CSS = [i*0 for i in range(3)]
        if request.POST.get('CSS')=='1':
            CSS[0] = 1
        elif request.POST.get('CSS')=='2':
            CSS[1] = 1
        else:
            pass
        data_['Customer Segment'] = CSS
        
        Mrr = [i*0 for i in range(4)]
        if request.POST.get('Mrr')=='1':
            Mrr[0] = 1
        elif request.POST.get('Mrr')=='2':
            Mrr[1] = 1
        elif request.POST.get('Mrr')=='3':
            Mrr[2] = 1
        elif request.POST.get('Mrr')=='4':
            Mrr[3] = 1
        else:
            pass
        data_['Market'] = Mrr

        Tyy = [i*0 for i in range(4)]
        if request.POST.get('Tyy')=='1':
            Tyy[0] = 1
        elif request.POST.get('Tyy')=='2':
            Tyy[1] = 1
        elif request.POST.get('Tyy')=='3':
            Tyy[2] = 1
        else:
            pass
        data_['Type'] = Tyy

        DNN = [i*0 for i in range(4)]
        if request.POST.get('DNN')=='1':
            DNN[0] = 1
        elif request.POST.get('DNN')=='2':
            DNN[1] = 1
        elif request.POST.get('DNN')=='3':
            DNN[2] = 1
        else:
            pass
        data_['Department Name'] = DNN


        CNN = [i*0 for i in range(29)]
        if request.POST.get('CNN')=='1':
            CNN[0] = 1
        elif request.POST.get('CNN')=='2':
            CNN[1] = 1
        elif request.POST.get('CNN')=='3':
            CNN[2] = 1
        elif request.POST.get('CNN')=='4':
            CNN[3] = 1
        elif request.POST.get('CNN')=='5':
            CNN[4] = 1
        elif request.POST.get('CNN')=='6':
            CNN[5] = 1
        elif request.POST.get('CNN')=='7':
            CNN[6] = 1
        elif request.POST.get('CNN')=='8':
            CNN[7] = 1
        elif request.POST.get('CNN')=='9':
            CNN[8] = 1
        elif request.POST.get('CNN')=='10':
            CNN[9] = 1
        elif request.POST.get('CNN')=='11':
            CNN[10] = 1
        elif request.POST.get('CNN')=='12':
            CNN[11] = 1
        elif request.POST.get('CNN')=='13':
            CNN[12] = 1
        elif request.POST.get('CNN')=='14':
            CNN[13] = 1
        elif request.POST.get('CNN')=='15':
            CNN[14] = 1
        elif request.POST.get('CNN')=='16':
            CNN[15] = 1
        elif request.POST.get('CNN')=='17':
            CNN[16] = 1
        elif request.POST.get('CNN')=='18':
            CNN[17] = 1
        elif request.POST.get('CNN')=='19':
            CNN[18] = 1
        elif request.POST.get('CNN')=='20':
            CNN[19] = 1
        elif request.POST.get('CNN')=='21':
            CNN[20] = 1
        elif request.POST.get('CNN')=='22':
            CNN[21] = 1
        elif request.POST.get('CNN')=='23':
            CNN[22] = 1
        elif request.POST.get('CNN')=='24':
            CNN[23] = 1
        elif request.POST.get('CNN')=='25':
            CNN[24] = 1
        elif request.POST.get('CNN')=='26':
            CNN[25] = 1
        elif request.POST.get('CNN')=='27':
            CNN[26] = 1
        elif request.POST.get('CNN')=='28':
            CNN[27] = 1
        else:
            pass
        data_['Category Name'] = CNN

        scaler.clip = False
        numerical_features = scaler.transform(np.array(list(data_.values())[:9]).reshape(1,-1))

        categorical_features = []
        for i in list(data_.values())[9:]:
            if type(i) is list:
                categorical_features.extend(i)
            else:
                categorical_features.append(i)
        
        features = np.concatenate((numerical_features,np.array(categorical_features).reshape(1,-1)),axis=1)
        predictions = model_.predict(features)
        
        context = predictions[0]
        return redirect('/index')
         
   

    return render(request,'new_data2/home.html')

def index(request):
    return render(request,'new_data2/index.html',{'context':context})

