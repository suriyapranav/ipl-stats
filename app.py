from flask import Flask, escape, request, render_template,redirect, url_for
import os
import pandas as pd

app = Flask(__name__)

class data:

	pic1=''
	pic2=''


	bat=''
	bow=''

	runs=0
	frun=0
	srun=0
	f4=0
	f6=0
	s4=0
	s6=0
	wik=0
	fwik=0
	swik=0
	ball=0
	fball=0
	sball=0
	mat=0

	show=False

batsmen=['AM Nayar', 'Mustafizur Rahman', 'M Kaif', 'Z Khan', 'SK Warne', 'T Kohli', 'BA Bhatt', 'VVS Laxman', 'SN Thakur', 'CA Lynn', 'R Rampaul', 'NL McCullum', 'Sachin Baby', 'Abdur Razzak', 'Basil Thampi', 'SK Raina', 'JD Unadkat', 'GB Hogg', 'RJ Peterson', 'CV Varun', 'HH Pandya', 'SD Lad', 'MG Johnson', 'A Mukund', 'JA Morkel', 'VS Malik', 'LE Plunkett', 'MV Boucher', 'JE Taylor', 'C Madan', 'UBT Chand', 'JP Duminy', 'M Ashwin', 'RS Sodhi', 'Vishnu Vinod', 'J Arunkumar', 'RR Raje', 'Y Venugopal Rao', 'JDS Neesham', 'PJ Sangwan', 'A Singh', 'S Aravind', 'PA Patel', 'DJM Short', 'KC Sangakkara', 'HF Gurney', 'V Kohli', 'AD Nath', 'CJ Ferguson', 'RS Gavaskar', 'UT Yadav', 'V Pratap Singh', 'R Shukla', 'DM Bravo', 'S Sohal', 'SS Iyer', 'SO Hetmyer', 'AA Chavan', 'KS Williamson', 'F du Plessis', 'Joginder Sharma', 'P Kumar', 'DP Vijaykumar', 'S Dhawan', 'KP Appanna', 'SS Shaikh', 'M Rawat', 'KA Pollard', 'Shakib Al Hasan', 'T Taibu', 'SMSM Senanayake', 'MK Lomror', 'C Nanda', 'Anirudh Singh', 'DJ Thornely', 'T Henderson', 'BR Dunk', 'P Dogra', 'S Gopal', 'P Dubey', 'SP Narine', 'MJ Guptill', 'Abhishek Sharma', 'Parvez Rasool', 'R Bishnoi', 'A Zampa', 'RG More', 'M Kartik', 'BB Sran', 'D du Preez', 'DL Chahar', 'DB Ravi Teja', 'Sunny Singh', 'D Kalyankrishna', 'H Klaasen', 'VS Yeligati', 'BMAJ Mendis', 'KJ Abbott', 'K Goel', 'MD Mishra', 'S Badree', 'Avesh Khan', 'RD Chahar', 'KP Pietersen', 'Shahid Afridi', 'Harmeet Singh', 'Shoaib Malik', 'SB Styris', 'JL Denly', 'Shoaib Akhtar', 'Kuldeep Yadav', 'ML Hayden', 'Sohail Tanvir', 'AA Bilakhia', 'Imran Tahir', 'LH Ferguson', 'CA Pujara', 'L Balaji', 'LJ Wright', 'R Dhawan', 'VH Zol', 'T Natarajan', 'KH Pandya', 'S Sriram', 'VR Aaron', 'AB Dinda', 'I Udana', 'BA Stokes', 'Washington Sundar', 'I Malhotra', 'Rashid Khan', 'CR Brathwaite', 'WP Saha', 'Karanveer Singh', 'DR Shorey', 'DJ Hooda', 'Q de Kock', 'CK Langeveldt', 'KMA Paul', 'CR Woakes', 'KK Ahmed', 'LRPL Taylor', 'ER Dwivedi', 'LMP Simmons', 'MP Stoinis', 'Shoaib Ahmed', 'AM Rahane', 'RT Ponting', 'PC Valthaty', 'AC Voges', 'R Ashwin', 'M Prasidh Krishna', 'AB Barath', 'SB Joshi', 'DT Patil', 'Abdul Samad', 'S Narwal', 'MJ Lumb', 'P Sahu', 'A Symonds', 'RS Bopara', 'Shivam Sharma', 'I Sharma', 'FH Edwards', 'TD Paine', 'Mashrafe Mortaza', 'BJ Rohrer', 'PP Ojha', 'Ankit Soni', 'PR Shah', 'OA Shah', 'KD Karthik', 'SD Chitnis', 'CJ Anderson', 'AB McDonald', 'DE Bollinger', 'JDP Oram', 'Sandeep Sharma', 'MA Wood', 'A Chopra', 'C de Grandhomme', 'RD Gaikwad', 'DR Martyn', 'RA Tripathi', 'Mohammad Ashraful', 'Salman Butt', 'CJ McKay', 'SR Watson', 'RA Jadeja', 'K Rabada', 'AN Ghosh', 'SM Katich', 'AUK Pathan', 'P Chopra', 'PV Tambe', 'BJ Hodge', 'PSP Handscomb', 'A Mishra', 'Younis Khan', 'MEK Hussey', 'R McLaren', 'J Suchith', 'B Sumanth', 'DPMD Jayawardene', 'NJ Maddinson', 'DW Steyn', 'GJ Bailey', 'Misbah-ul-Haq', 'BJ Haddin', 'J Yadav', 'Yashpal Singh', 'V Sehwag', 'A Flintoff', 'SR Tendulkar', 'E Lewis', 'KAJ Roach', 'SS Tiwary', 'AA Noffke', 'TG Southee', 'P Ray Barman', 'Rasikh Salam', 'RR Rossouw', 'GD McGrath', 'MM Sharma', 'SK Trivedi', 'CA Ingram', 'P Awana', 'YBK Jaiswal', 'AA Jhunjhunwala', 'SW Billings', 'IS Sodhi', 'TU Deshpande', 'S Tyagi', 'TR Birt', 'MM Ali', 'B Kumar', 'MDKJ Perera', 'SJ Srivastava', 'Niraj Patel', 'X Thalaivan Sargunam', 'S Dube', 'MJ McClenaghan', 'MK Tiwary', 'JP Faulkner', 'Azhar Mahmood', 'MS Dhoni', 'Umar Gul', 'MS Wade', 'UA Birla', 'AD Hales', 'Bipul Sharma', 'MS Gony', 'DA Miller', 'PJ Cummins', 'AD Mascarenhas', 'AR Bawne', 'MR Marsh', 'AN Ahmed', 'Sunny Gupta', 'KL Nagarkoti', 'AD Russell', 'D Salunkhe', 'DAJ Bracewell', 'P Negi', 'CK Kapugedera', 'DS Kulkarni', 'A Nortje', 'TM Srivastava', 'TS Mills', 'SV Samson', 'RR Pant', 'SE Rutherford', 'PA Reddy', 'UT Khawaja', 'MN Samuels', 'FY Fazal', 'R Sathish', 'MA Starc', 'S Anirudha', 'SB Wagh', 'Harpreet Brar', 'KV Sharma', 'A Kumble', 'KB Arun Karthik', 'CRD Fernando', 'YA Abdulla', 'STR Binny', 'W Jaffer', 'SP Fleming', 'MN van Wyk', 'AG Paunikar', 'A Chandila', 'ND Doshi', 'Shivam Mavi', 'HV Patel', 'PD Collingwood', 'WA Mota', 'Swapnil Singh', 'Y Prithvi Raj', 'Y Nagar', 'Mandeep Singh', 'JR Philippe', 'KL Rahul', 'A Nehra', 'KM Jadhav', 'JEC Franklin', 'DJ Hussey', 'C Munro', 'KK Nair', 'SB Bangar', 'CM Gautam', 'RK Singh', 'AB de Villiers', 'RJ Quiney', 'GC Smith', 'RJ Harris', 'M Ntini', 'M Markande', 'LA Pomersbach', 'D Padikkal', 'G Gambhir', 'M Vohra', 'RR Sarwan', 'VY Mahesh', 'LA Carseldine', 'DR Smith', 'MJ Clarke', 'Mohammad Hafeez', 'B Chipli', 'RV Uthappa', 'MM Patel', 'Shahbaz Ahmed', 'MA Khote', 'GC Viljoen', 'Mohammed Siraj', 'RN ten Doeschate', 'RK Bhui', 'H Das', 'Yuvraj Singh', 'EJG Morgan', 'TK Curran', 'RG Sharma', 'JM Bairstow', 'ST Jayasuriya', 'NM Coulter-Nile', 'JR Hopes', 'DR Sams', 'DL Vettori', 'JM Kemp', 'AG Murtaza', 'L Ronchi', 'MC Henriques', 'SPD Smith', 'JC Archer', 'IK Pathan', 'JL Pattinson', 'AS Joseph', 'U Kaul', 'SE Bond', 'IR Jaggi', 'BB McCullum', 'SA Abbott', 'Ravi Bishnoi', 'DJ Harris', 'Ishan Kishan', 'WD Parnell', 'S Nadeem', 'SN Khan', 'BCJ Cutting', 'T Thushara', 'HH Gibbs', 'AP Tare', 'AJ Turner', 'BAW Mendis', 'YS Chahal', 'SA Yadav', 'A Dananjaya', 'TM Head', 'JPR Scantlebury-Searles', 'HM Amla', 'S Vidyut', 'NS Naik', 'JO Holder', 'LR Shukla', 'R Dravid', 'MA Agarwal', 'AS Yadav', 'MJ Santner', 'R Sharma', 'DP Nannes', 'T Banton', 'WPUJC Vaas', 'V Shankar', 'S Kaul', 'S Sreesanth', 'AP Dole', 'N Rana', 'AJ Tye', 'Arshdeep Singh', 'YK Pathan', 'KC Cariappa', 'BE Hendricks', 'DS Lehmann', 'KK Cooper', 'SS Cottrell', 'AL Menaria', 'N Jagadeesan', 'R Ninan', 'A Ashish Reddy', 'AC Thomas', 'B Lee', 'JJ Bumrah', 'KMDN Kulasekara', 'BB Samantray', 'KW Richardson', 'GR Napier', 'K Gowtham', 'VRV Singh', 'PK Garg', 'RP Singh', 'DJG Sammy', 'PP Shaw', 'L Ablish', 'PM Sarvesh Kumar', 'DJ Muthuswami', 'TM Dilshan', 'R Vinay Kumar', 'CH Gayle', 'SA Asnodkar', 'S Badrinath', 'Mohammad Asif', 'RV Gomez', 'JC Buttler', 'NLTC Perera', 'AP Majumdar', 'B Stanlake', 'A Uniyal', 'S Chanderpaul', 'AS Rajpoot', 'JJ van der Wath', 'DJ Bravo', 'AR Patel', 'SC Ganguly', 'Ankit Sharma', 'DNT Zoysa', 'LPC Silva', 'AF Milne', 'SM Harwood', 'AC Blizzard', 'AB Agarkar', 'CJ Jordan', 'GH Vihari', 'RE Levi', 'SE Marsh', 'SM Curran', 'RR Bhatkal', 'Mujeeb Ur Rahman', 'A Choudhary', 'J Syed Mohammad', 'MS Bisla', 'SP Goswami', 'CL White', 'R Tewatia', 'R Bhatia', 'M de Lange', 'Shubman Gill', 'M Vijay', 'TA Boult', 'MF Maharoof', 'NA Saini', 'SL Malinga', 'CH Morris', 'JJ Roy', 'S Kaushik', 'J Theron', 'Gurkeerat Singh', 'Harbhajan Singh', 'Anureet Singh', 'Mohammed Shami', 'IC Pandey', 'B Laughlin', 'YV Takawale', 'SP Jackson', 'MK Pandey', 'M Klinger', 'SW Tait', 'M Muralitharan', 'S Ladda', 'A Mithun', 'DB Das', 'MC Juneja', 'DH Yagnik', 'Mohammad Nabi', 'NV Ojha', 'DJ Jacobs', 'DA Warner', 'P Simran Singh', 'S Lamichhane', 'PP Chawla', 'Kamran Akmal', 'JD Ryder', 'K Upadhyay', 'SM Pollock', 'RR Powar', 'Jaskaran Singh', 'Kamran Khan', 'DT Christian', 'F Behardien', 'M Morkel', 'J Botha', 'GJ Maxwell', 'Kartik Tyagi', 'AS Raut', 'N Pooran', 'N Saini', 'M Manhas', 'AT Carey', 'AC Gilchrist', 'P Parameswaran', 'AD Mathews', 'B Akhil', 'Y Gnaneswara Rao', 'AJ Finch', 'NJ Rimmington', 'SB Jakati', 'R Parag', 'Harpreet Singh', 'RE van der Merwe', 'JH Kallis', 'TL Suman', 'D Wiese', 'S Rana', 'AT Rayudu', 'Pankaj Singh', 'S Randiv', 'LS Livingstone', 'Iqbal Abdulla']
bowlers=['AM Nayar', 'Mustafizur Rahman', 'Z Khan', 'SK Warne', 'BA Bhatt', 'SN Thakur', 'C Ganapathy', 'R Rampaul', 'NL McCullum', 'Sachin Baby', 'Abdur Razzak', 'Basil Thampi', 'SK Raina', 'JD Unadkat', 'GB Hogg', 'RJ Peterson', 'CV Varun', 'AS Roy', 'HH Pandya', 'MG Johnson', 'JA Morkel', 'VS Malik', 'LE Plunkett', 'JE Taylor', 'O Thomas', 'JP Duminy', 'M Ashwin', 'RR Raje', 'AA Kazi', 'JW Hastings', 'Y Venugopal Rao', 'SC Kuggeleijn', 'JDS Neesham', 'PJ Sangwan', 'A Singh', 'S Aravind', 'DJM Short', 'Gagandeep Singh', 'HF Gurney', 'V Kohli', 'K Santokie', 'RS Gavaskar', 'UT Yadav', 'V Pratap Singh', 'R Shukla', 'T Shamsi', 'AA Chavan', 'KS Williamson', 'Joginder Sharma', 'F du Plessis', 'P Kumar', 'DP Vijaykumar', 'S Dhawan', 'KP Appanna', 'KA Pollard', 'SS Mundhe', 'Shakib Al Hasan', 'SMSM Senanayake', 'C Nanda', 'MK Lomror', 'DJ Thornely', 'T Henderson', 'S Gopal', 'P Dubey', 'SP Narine', 'Abhishek Sharma', 'Parvez Rasool', 'A Zampa', 'RG More', 'M Kartik', 'MJ Henry', 'BB Sran', 'D du Preez', 'DL Chahar', 'DB Ravi Teja', 'D Kalyankrishna', 'Monu Kumar', 'VS Yeligati', 'BMAJ Mendis', 'KJ Abbott', 'K Goel', 'S Badree', 'Avesh Khan', 'KP Pietersen', 'RD Chahar', 'Shahid Afridi', 'Harmeet Singh', 'Shoaib Malik', 'SB Styris', 'Tejas Baroka', 'Shoaib Akhtar', 'Kuldeep Yadav', 'Sohail Tanvir', 'Imran Tahir', 'LH Ferguson', 'L Balaji', 'LJ Wright', 'R Dhawan', 'T Natarajan', 'KH Pandya', 'S Sriram', 'VR Aaron', 'K Khejroliya', 'AB Dinda', 'I Udana', 'BA Stokes', 'Washington Sundar', 'I Malhotra', 'Rashid Khan', 'CR Brathwaite', 'Karanveer Singh', 'DJ Hooda', 'CK Langeveldt', 'KMA Paul', 'RW Price', 'CR Woakes', 'KK Ahmed', 'LRPL Taylor', 'LMP Simmons', 'MP Stoinis', 'Shoaib Ahmed', 'AM Rahane', 'AM Salvi', 'AC Voges', 'PC Valthaty', 'R Ashwin', 'M Prasidh Krishna', 'SB Joshi', 'Abdul Samad', 'S Narwal', 'P Sahu', 'A Symonds', 'RS Bopara', 'Shivam Sharma', 'I Sharma', 'SM Boland', 'FH Edwards', 'Mashrafe Mortaza', 'BJ Rohrer', 'PP Ojha', 'Ankit Soni', 'SD Chitnis', 'CJ Anderson', 'NB Singh', 'AB McDonald', 'DE Bollinger', 'KM Asif', 'JP Behrendorff', 'JDP Oram', 'Sandeep Sharma', 'MA Wood', 'C de Grandhomme', 'RA Tripathi', 'CJ McKay', 'SR Watson', 'MG Neser', 'RA Jadeja', 'K Rabada', 'AUK Pathan', 'PV Tambe', 'BJ Hodge', 'A Mishra', 'P Prasanth', 'R McLaren', 'J Suchith', 'SS Sarkar', 'DW Steyn', 'J Yadav', 'V Sehwag', 'A Flintoff', 'SR Tendulkar', 'KAJ Roach', 'AA Noffke', 'TG Southee', 'P Ray Barman', 'Rasikh Salam', 'TP Sudhindra', 'GD McGrath', 'MM Sharma', 'SK Trivedi', 'P Awana', 'AA Jhunjhunwala', 'IS Sodhi', 'TU Deshpande', 'S Tyagi', 'MM Ali', 'B Kumar', 'SJ Srivastava', 'CJ Green', 'S Dube', 'MJ McClenaghan', 'MK Tiwary', 'JP Faulkner', 'Azhar Mahmood', 'Umar Gul', 'Bipul Sharma', 'MS Gony', 'PJ Cummins', 'AD Mascarenhas', 'MR Marsh', 'AN Ahmed', 'Sunny Gupta', 'S Midhun', 'KL Nagarkoti', 'AD Russell', 'D Salunkhe', 'DAJ Bracewell', 'P Negi', 'CK Kapugedera', 'DS Kulkarni', 'A Nortje', 'TS Mills', 'SE Rutherford', 'MN Samuels', 'FY Fazal', 'B Geeves', 'JR Hazlewood', 'R Sathish', 'MA Starc', 'SB Wagh', 'Harpreet Brar', 'KV Sharma', 'A Kumble', 'CRD Fernando', 'YA Abdulla', 'STR Binny', 'MB Parmar', 'A Chandila', 'ND Doshi', 'BW Hilfenhaus', 'Shivam Mavi', 'HV Patel', 'PD Collingwood', 'WA Mota', 'S Sandeep Warrier', 'Swapnil Singh', 'Y Prithvi Raj', 'Y Nagar', 'Mandeep Singh', 'A Nehra', 'JEC Franklin', 'DJ Hussey', 'C Munro', 'SB Bangar', 'RJ Harris', 'M Ntini', 'M Markande', 'VY Mahesh', 'LA Carseldine', 'DR Smith', 'MJ Clarke', 'DJ Willey', 'Mohammad Hafeez', 'B Chipli', 'MM Patel', 'Shahbaz Ahmed', 'MA Khote', 'GC Viljoen', 'Mohammed Siraj', 'Harmeet Singh (2)', 'RN ten Doeschate', 'Yuvraj Singh', 'TK Curran', 'RG Sharma', 'ST Jayasuriya', 'NM Coulter-Nile', 'JR Hopes', 'DR Sams', 'DL Vettori', 'JM Kemp', 'AG Murtaza', 'MC Henriques', 'JC Archer', 'SPD Smith', 'IK Pathan', 'JL Pattinson', 'AS Joseph', 'SE Bond', 'SA Abbott', 'Ravi Bishnoi', 'DJ Harris', 'WD Parnell', 'S Nadeem', 'SN Khan', 'BCJ Cutting', 'T Thushara', 'BAW Mendis', 'YS Chahal', 'SA Yadav', 'RA Shaikh', 'A Nel', 'A Dananjaya', 'TM Head', 'JPR Scantlebury-Searles', 'S Vidyut', 'JO Holder', 'LR Shukla', 'MJ Santner', 'R Sharma', 'DP Nannes', 'WPUJC Vaas', 'V Shankar', 'S Kaul', 'S Sreesanth', 'AP Dole', 'N Rana', 'AJ Tye', 'Arshdeep Singh', 'YK Pathan', 'KC Cariappa', 'BE Hendricks', 'KK Cooper', 'SS Cottrell', 'AL Menaria', 'R Ninan', 'A Ashish Reddy', 'AC Thomas', 'B Lee', 'JJ Bumrah', 'KMDN Kulasekara', 'Anand Rajan', 'GR Napier', 'KW Richardson', 'K Gowtham', 'VRV Singh', 'RP Singh', 'DJG Sammy', 'L Ablish', 'PM Sarvesh Kumar', 'DJ Muthuswami', 'TM Dilshan', 'R Vinay Kumar', 'CH Gayle', 'Mohammad Asif', 'RV Gomez', 'NLTC Perera', 'B Stanlake', 'SS Agarwal', 'A Uniyal', 'AS Rajpoot', 'JJ van der Wath', 'P Suyal', 'DJ Bravo', 'AR Patel', 'SC Ganguly', 'Ankit Sharma', 'LPC Silva', 'DNT Zoysa', 'AF Milne', 'SM Harwood', 'AB Agarkar', 'CJ Jordan', 'GH Vihari', 'RR Bhatkal', 'SM Curran', 'Mujeeb Ur Rahman', 'A Choudhary', 'J Syed Mohammad', 'CL White', 'R Tewatia', 'R Bhatia', 'M de Lange', 'M Vijay', 'TA Boult', 'MF Maharoof', 'NA Saini', 'SL Malinga', 'CH Morris', 'S Kaushik', 'J Theron', 'Gurkeerat Singh', 'Harbhajan Singh', 'Anureet Singh', 'Mohammed Shami', 'IC Pandey', 'B Laughlin', 'P Amarnath', 'GS Sandhu', 'SW Tait', 'M Muralitharan', 'S Ladda', 'A Mithun', 'Mohammad Nabi', 'CJ Dala', 'DA Warner', 'S Lamichhane', 'PP Chawla', 'JD Ryder', 'K Upadhyay', 'SM Pollock', 'RR Powar', 'Jaskaran Singh', 'Kamran Khan', 'DT Christian', 'M Morkel', 'J Botha', 'GJ Maxwell', 'Kartik Tyagi', 'AS Raut', 'M Manhas', 'P Parameswaran', 'AC Gilchrist', 'RR Bose', 'AD Mathews', 'B Akhil', 'Y Gnaneswara Rao', 'AJ Finch', 'NJ Rimmington', 'L Ngidi', 'SB Jakati', 'R Parag', 'RE van der Merwe', 'JH Kallis', 'TL Suman', 'D Wiese', 'S Rana', 'Pankaj Singh', 'S Randiv', 'LS Livingstone', 'Iqbal Abdulla']


@app.route("/")

def home():
	reset()
	return render_template('main.html',data=data,batsmen=batsmen,bowlers=bowlers)

def reset():
	data.pic1=''
	data.pic2=''


	data.bat=''
	data.bow=''

	data.runs=0
	data.frun=0
	data.srun=0
	data.f4=0
	data.f6=0
	data.s4=0
	data.s6=0
	data.wik=0
	data.fwik=0
	data.swik=0
	data.ball=0
	data.fball=0
	data.sball=0
	data.mat=0

	data.show=False


@app.route("/", methods=['POST'])


def get_data():

	reset()

	bats=(request.form['bat'])
	data.bat=bats
	bats_folder=bats.replace(' ','_')
	bats_folder+='_cricketer'
	bws=bats.replace(' ','_')

	if(bats!=''):
		data.pic1='static\\player_photos\\'+bats_folder+'\\'+bws+'_cricketer_1.jpeg'

	bats=(request.form['bowl'])
	data.bow=bats

	bats_folder=bats.replace(' ','_')
	bats_folder+='_cricketer'
	bws=bats.replace(' ','_')


	if(bats!=''):
		data.pic2='static\\player_photos\\'+bats_folder+'\\'+bws+'_cricketer_1.jpeg'

	

	if(data.bat!='' and data.bow!='' ):
		if((data.bat in batsmen ) and (data.bow in bowlers)):
			data.show=True
			calculate()

	#return redirect(url_for("home"))
	return render_template('main.html',data=data,batsmen=batsmen,bowlers=bowlers)

def calculate():


	file="static/ipl_data.csv"
	

	bat=data.bat
	bow=data.bow

	bat_file="static/Index_Bat/"+bat+'.csv'
	bow_file="static/Index_Bow/"+bow+'.csv'

	d=pd.read_csv(file)
	d=pd.DataFrame(d)
	m=[d.Bat,d.Bow,d.Runs,d.Out_Bat,d.Out,d.inn]
	d=pd.read_csv(bat_file)
	d=pd.DataFrame(d)
	bat_df=d


	d=pd.read_csv(bow_file)
	d=pd.DataFrame(d)
	bow_df=d


	s1 = pd.merge(bat_df, bow_df, how='inner', on=['Index'])

	index=set(s1.Index)
	data.mat=len(set(s1.Match_x))

	for i in index:
   
	    data.runs=data.runs+int(m[2][i])
	    data.ball+=1
	    
	    if(m[5][i]=='1'):
	        data.frun+= int(m[2][i])
	        data.fball+=1
	        if(m[2][i]==4):
	            data.f4+=1
	        if(m[2][i]==6):
	            data.f6+=1
	    else:
	        data.srun+= int(m[2][i])
	        data.sball+=1
	        
	        if(m[2][i]==4):
	            data.s4+=1
	        if(m[2][i]==6):
	            data.s6+=1
	        
	    if(m[3][i]==bat):
	        if(m[4][i]!="run out"):
	            data.wik+=1
	            if(m[5][i]=='1'):
	                data.fwik+=1
	            else:
	                data.swik+=1


def reset():
	data.pic1=''
	data.pic2=''


	data.bat=''
	data.bow=''

	data.runs=0
	data.frun=0
	data.srun=0
	data.f4=0
	data.f6=0
	data.s4=0
	data.s6=0
	data.wik=0
	data.fwik=0
	data.swik=0
	data.ball=0
	data.fball=0
	data.sball=0
	data.mat=0

	data.show=False

	               

	
if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



 	

