import csv
import folium
import leafmap
from datetime import date, datetime, timedelta
from turtle import width
import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import numpy as np
import openpyxl
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
import streamlit.components.v1 as components
st. set_page_config(layout="wide")
def main():
	col1, col2, col3,col4 = st.columns(4)
	with col1:
		st.write('')
	
	with col3:
		st.write('')
	
	
	
	
	with col4:


		st.write('')

	st.sidebar.image(
			"https://media-exp1.licdn.com/dms/image/C560BAQFp2xGac-EGmQ/company-logo_200_200/0/1644310391217?e=1659571200&v=beta&t=YV5Lgvs_H4rOoQ-bWjmI1k1jZcgJZxR8ZIcV0urw0vc",
			width=70, # Manually Adjust the width of the image as per requirement
			)
	
    # Add Reports name here 
	menu = ["Home","Fleet Planning","Mercury Order Recommendation Reports" , "Trucks & Drivers on Stale Report","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		with col2:
			st.image(
			"https://dctinc.com/wp-content/themes/dct/images/home/about-us.svg",
			width=750, # Manually Adjust the width of the image as per requirement
			)
		html_temp = """
		<div style="background-color:#025246 ;padding:10px">
		<h2 style="color:white;text-align:center;">Hoptek Automated Reports System </h2>
		</div>
		"""
		st.markdown(html_temp, unsafe_allow_html=True)
		#st.subheader("Home")
		"""
		
		"""
	if choice == "Fleet Planning":
		#m = leafmap.Map()
		
		#create map object
		#different tiles (map styles) can be used, like 'Stamen Toner', 'Stamen Terrain', ...
		m = folium.Map(location= [39.0997,-94.5786], zoom_start=4.3)
		#create city markers and add them to map object
		df = pd.read_csv('location12.csv')
		df_1 = df.drop(['CLIENT_ID','CITY','STATE','ADDRESS_1','ZIPCODE','LOCATION_TYPE','ONSITEBREAKFLAG','TIME_ZONE','INS_TMSTMP'], axis=1)
		for _, rows in df_1.iterrows():
			folium.Marker(
				location=[rows['LATITUDE'],rows['LONGITUDE']],popup= rows['NAME'],icon=folium.Icon(color='darkblue', icon_color='white', icon= "loading", prefix='fa')
			).add_to(m)
		df_2 = pd.read_csv('TruckLocation.csv')
		df_3 = df_2.dropna().reset_index(drop=True)
		#df_3 = df_2.drop([ 'LAST_SAT_DATE','CITY', 'STATE','ZIPCODE', 'LAST_SAT_ZONE', 'INS_TMSTMP'], axis=1)
		for _, rows1 in df_3.iterrows():
			folium.Marker(
				location=[rows1['LATITUDE'],rows1['LONGITUDE']],popup= rows1['UNIT_ID'],icon=folium.Icon(color='darkpurple', icon_color='white', icon= "truck", prefix='fa')
			).add_to(m)	
		#folium.Marker(location=[47.606209, -122.332069],popup='Seattle',icon=folium.Icon(color='purple', icon= "truck", prefix='fa')).add_to(m)
						#l1 = (df_1.loc[i,'LATITUDE'].tolist()).astype(float)
				#l2 = (df_1.loc[i,'LONGITUDE'].tolist()).astype(float)
				#l3 = df_1.loc[i,'NAME']

		#create superhero icons from images
		#iconSpiderman = folium.features.CustomIcon('./images/spiderman.png', icon_size=(100,100))
		#iconHulk = folium.features.CustomIcon('./images/hulk.png', icon_size=(100,100))
		#iconWolverine = folium.features.CustomIcon('C:\Users\savin.hooda\Desktop\coding\e41bc4be3d9cc8fcda26.png', icon_size=(100,100))

		#create superhero popup descriptions
		#popupSpiderman = "<strong>Spiderman</strong><br>Realname: Peter Parker<br>City of birth: Forest Hills, Queens, New York, USA"
		#popupHulk = "<strong>Hulk</strong><br>Realname: Bruce Banner<br>City of birth: Dayton, Ohio, USA"
		#SpopupWolverine = "<strong>Wolverine</strong><br>Realname: James Howlett (Logan)<br>City of birth: Cold Lake, Alberta, Canada"

		#create superhero markers and add them to map object
		#folium.Marker([40.743720, -73.822030], tooltip="Spiderman", popup=popupSpiderman, icon=iconSpiderman).add_to(m)
		#folium.Marker([39.760979, -84.192200], tooltip="Hulk", popup=popupHulk, icon=iconHulk).add_to(m)
		#folium.Marker([54.464180, -110.182259], tooltip="Wolverine").add_to(m)

		#generate map and save as local file
		source_code= m.save('index.html')
		HtmlFile = open("index.html", 'r', encoding='utf-8')
		source_code = HtmlFile.read()
		col1, col2, col3,col4 = st.columns(4)
		with col1:
			st.write('')
	
		with col3:
			st.write('')
	

		with col4:
			
			print(source_code)		
		components.html(source_code , height = 650 , width= 1190 )
		#m.to_streamlit()
	if choice == "Mercury Order Recommendation Reports":
		html_temp = """
		<div style="background-color:#025246 ;padding:10px">
		<h2 style="color:white;text-align:center;">Mercury Order Recommendation Reports </h2>
		</div>
		"""
		st.markdown(html_temp, unsafe_allow_html=True)
		#st.subheader("Home")
		"""
		
		"""
		data_file_1 = st.file_uploader("Upload First Run Order_Id File",type=['xlsx'])
		data_file_2 = st.file_uploader("Upload Second Run Order_Id File",type=['xlsx'])
		if st.button("Get Reports"):
			if data_file_1 is not None:
				df = pd.read_excel(data_file_1)
				df_1 = df.drop(['AssetInHopDP',
						'DriverInHopDP', 'DriverBEInHopDP', 'AssestInManualDP',
						'DriverInManualDP', 'DriverBEInManualDP', 'status', 'includeInSchedule',
						'priority', 'criticality', 'revMilesOnOrder', 'orLoc', 'orWindowOpen',
						'orWindowClose', 'orType', 'dsLoc', 'dsWindowOpen', 'dsWindowClose',
						'dsType', 'daysToPickup', 'WOLegORInboundLevel1',
						'WOLegORInboundLevel2', 'WOLegORInboundLevel3', 'WOLegDSOutboundLevel1',
						'WOLegDSOutboundLevel2', 'WOLegDSOutboundLevel3',
						'WOLegORInboundFromCLLevel1', 'WOLegORInboundFromCLLevel2',
						'WOLegORInboundFromCLLevel3', 'TotalTPCount', 'TPDistribution',
						'TPAssessment', 'Description', 'driverId', 'driverName', 'driverBE',
						'orderBE'], axis=1)
				df_2 = df_1[(df_1['assignedBy']== 'Mercury') & (df_1['orderType'] == 'SOLO')]
				df_3 = pd.read_excel(data_file_2)
				df_4 = df_3.drop(['AssetInHopDP',
						'DriverInHopDP', 'DriverBEInHopDP', 'AssestInManualDP',
						'DriverInManualDP', 'DriverBEInManualDP', 'status', 'includeInSchedule',
						'priority', 'criticality', 'revMilesOnOrder', 'orLoc', 'orWindowOpen',
						'orWindowClose', 'orType', 'dsLoc', 'dsWindowOpen', 'dsWindowClose',
						'dsType', 'daysToPickup', 'WOLegORInboundLevel1',
						'WOLegORInboundLevel2', 'WOLegORInboundLevel3', 'WOLegDSOutboundLevel1',
						'WOLegDSOutboundLevel2', 'WOLegDSOutboundLevel3',
						'WOLegORInboundFromCLLevel1', 'WOLegORInboundFromCLLevel2',
						'WOLegORInboundFromCLLevel3', 'TotalTPCount', 'TPDistribution',
						'TPAssessment', 'Description', 'driverId', 'driverName', 'driverBE',
						'orderBE'], axis=1)      
				filt = (df_4['assignedBy'] == 'Manual') & (df_4['orderType'] == 'SOLO') 
				df_5 = df_4.loc[filt]
				#df_5['orderId'].astype(int64)
				df_6 = pd.merge(df_2,df_5 ,on='orderId')
				df_7 = df_6.orderId.values.tolist()
				df_6 = df_5.merge(df_2, on=['orderId','AssetInDP', 'DriverInDP', 'DriverBEInDP'], how = 'inner')
				def get_reports() :
					st.write("Mercury recommendation", '=', len(df_2)) 
					st.write("Manual order count", '=', df_5.shape[0])
					st.write( 'OrderId Matched From Mercury Recommendation count' , '=' , len(df_7) )
					st.write('OrderId Matched From Mercury Recommendation' , '=', str(df_7))
					st.write('Number of Accepted Recommendation', '=' , df_6.shape[0])
					st.write('Number of Rejected Recommendation', '=' ,df_5.shape[0] - df_6.shape[0] )
					st.write('Percentage of Accepted Recommendation', '=' , round((df_6.shape[0]) / df_5.shape[0] *100),'%')
				st.write(get_reports())
	if choice == "Trucks & Drivers on Stale Report":
		#st.subheader("Home")
		html_temp = """
		<div style="background-color:#025246 ;padding:10px">
		<h2 style="color:white;text-align:center;"> Trucks & Drivers on Stale Report </h2>
		</div>
		"""
		st.markdown(html_temp, unsafe_allow_html=True)
#st.subheader("Home")
		"""
		
		"""
		data_file_1 = st.file_uploader("Trucks & Drivers on Stale Report File",type=['csv'])
		time_1 = st.text_input("Enter current schedule date and time in format MM-DD-2022 HH:00:00 ")
		if st.button("Get Reports"):
			if data_file_1 is not None:
				df = pd.read_csv(data_file_1)
				df_1 = df.drop([ 'dispatcher', 
						'gapBetweenTruckandDriverLastUpdate', 'recentlyUpdatedTruckDriver',
						'truckCurrentLat', 'truckCurrentLong', 'truckCurrentCity', 'hOSClocks',
						'recaps'], axis=1)
				df_2 = df_1.drop([ 'truckId', 'truckLastUpdated'], axis=1)
				df_2['Current_Schedule_Time'] = (time_1)
				df_2['driverStatusInitiated'] = pd.to_datetime(df_2['driverStatusInitiated'].astype(str))
				df_2['Current_Schedule_Time'] = pd.to_datetime(df_2['Current_Schedule_Time'].astype(str))
				df_2['Driver_Stale_Time'] = df_2['Current_Schedule_Time']-df_2['driverStatusInitiated']
				df_2['Driver_Stale_Time'] = df_2['Driver_Stale_Time']/np.timedelta64(1,'h')
				filt = (df_2['Driver_Stale_Time'] > 10)
				df_3 = df_2.loc[filt]
				df_3['Remarks'] = 'Only Driver  Status not updated >10 hours'
				Count1 = (df_3['Remarks'].count())
				filt = (df_3['hOSStatus'] == 'OffDuty')
				df_4 = df_3.loc[filt]
				Count2 = (df_4['hOSStatus'].count())
				filt = (df_3['hOSStatus'] == 'SleeperBerth')
				df_5 = df_3.loc[filt]
				Count3 = (df_5['hOSStatus'].count())
				filt = (df_3['hOSStatus'] == 'OnDuty')
				df_6 = df_3.loc[filt]
				Count4 = (df_6['hOSStatus'].count())
				filt = (df_3['hOSStatus'] == 'Driving')
				df_7 = df_3.loc[filt]
				Count5 = (df_7['hOSStatus'].count())
				st.title("Drivers More Than 10 Hours Stale :-")
				st.title(Count1)
				st.write(df_3)
				st.title("Driver HOS STATUS OffDuty -")
				st.title(Count2)
				st.write(df_4)
				st.title("Driver HOS STATUS SleeperBerth:-")
				st.title(Count3)
				st.write(df_5)
				st.title("Driver HOS STATUS OnDuty:-")
				st.title(Count4)
				st.write(df_6)
				st.title("Driver HOS STATUS Driving:-")
				st.title(Count5)
				st.write(df_7)
				df_11 = df_1.drop([ 'driverName','hOSStatus', 'driverStatusInitiated'], axis=1)
				df_11['Current_Schedule_Time'] = df_2['Current_Schedule_Time']
				df_11['Current_Schedule_Time'] = pd.to_datetime(df_11['Current_Schedule_Time'].astype(str))
				df_11['truckLastUpdated'] = pd.to_datetime(df_11['truckLastUpdated'].astype(str))
				df_11['Truck_Stale_Time'] = df_11['Current_Schedule_Time'] - df_11['truckLastUpdated']
				df_11['Truck_Stale_Time'] = df_11['Truck_Stale_Time']/np.timedelta64(1,'h')
				filt = (df_11['Truck_Stale_Time'] > 10)
				df_12 = df_11.loc[filt]
				df_12['Remarks'] = 'Asset Status not updated >10 hours'
				Count11 = (df_12['Remarks'].count())
				st.title("Assets More Than 10 Hours Stale :-")
				st.title(Count11)
				st.write(df_12)
				df_12.to_excel("reports.xlsx", sheet_name='Truck & Driver Stale Update')
				st.download_button(label= 'Download Reports',data= "reports.xlsx",mime= 'xlsx')

	if choice == "About":
		with col2:
				st.image(
				"https://dctinc.com/wp-content/themes/dct/images/home/about-us.svg",
				width=550, # Manually Adjust the width of the image as per requirement
				)
		st.subheader("About")
		st.info("Built By :  SAVIN HOODA ")
		st.info("Automated Reports Genration System For Hoptek")
		st.text("Digital Convergence Technologies (DCT Inc))")
		st.subheader('')
if __name__ == '__main__':
	main()