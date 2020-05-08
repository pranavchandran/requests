import requests
import json

#  r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# https://api.covid19india.org/data.json
# r = requests.get('https://api.covid19india.org/data.json')
# print(r)
# print(r.text)

# print(r.json()['cases_time_series'][1])

# Just checking requests for api extraction

# ***************************************************************************
# r = requests.get('https://api.rootnet.in/covid19-in/contacts')
# print(r)
# data = json.loads(r.text)
# print(data)
# print(data.keys())
# print(data.values())


# print(data.values())owing is an important task so just practicing
# Details of that site API
# for d,y in data['data']['contacts']['primary'].items():
#     print(f'{d}     :   {y}')

# All states urgent contact numbers
# for d in data['data']['contacts']['regional']:
    # print(f'{d}Location     : Details {y}')
    # print(f'{d}')


# we can ue this type to show data in table.But i dont show here because am not using ANACONDA
# from pandas.io.json import json_normalize 
  
# df = json_normalize(json_parse['Student'], 
#                                'subject',  
#                     ['enrollment_no', 'name']) 
  
# df.sort_values(['code', 'grade', 'enrollment_no']).reset_index(drop=True) 


# You can search districtbase zones status =red,green,yel etc


r = requests.get('https://api.covid19india.org/zones.json')
print(r)
data = json.loads(r.text)
zones = []
for x in data['zones']:
    zones.append(x)
    # print("\t\tDistrict :{0}\t\tState :{1}\t\tZone :{2}".format (x['district'],x['state'], x['zone']))

# print(len(zones))
wanted=[]
for x in zones:

    ([lambda x,y,z: x+y+z,wanted.append((x['zone'],x['state'],x['district']))])

# One of the good format****************************************
st = 'Kerala'
res = [k for k in wanted if st in k]
# *************************************************************
# for x in res:
#     print(x)
# ************************************************************
print('The lists are:', *res, sep='\n')
# ************************************************************




        # if 'Andaman and Nicobar Islands' in wanted:
        #     print(x)
        # else:
        #     print('no')
# numbers = len(wanted)

# print(wanted,'\n')

# print(filtered)





