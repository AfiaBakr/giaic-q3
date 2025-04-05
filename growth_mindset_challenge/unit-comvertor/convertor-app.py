

import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient (135deg, #98f5f2, #5fede9);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    }
    h1 {
        text-align: center;
        font: 36px;
        color: white;
    }
    .stButton>button {
        background-color: linear-gradient(45deg, #796de8, #4b3ae8);
        color: white;
        font-size: 18px;
        padding: 10px 20px:
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0,201,255, 0.1);
    }
    .stButton>button:hover{
        background: linear-gradient(45deg #6fa8dc #8e7cc3);
        transform: scale(1.05);
        color: gray;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold:
        font-align: center;
        background: rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0,201,255, 0.1);
    }
    .formula-box{
        font-size: 18px;
        font-weight: medium:
        font-align: left;
        background: rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0,201,255, 0.1);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: gray;
        font-size: 18px; 
    }
    </style>
    """, 
        unsafe_allow_html=True
)

#title and description

st.markdown("<h1> Welcome to Python and Streamlit Unit Converter!</h1>", unsafe_allow_html=True)
st.write("Easily convert your value between different units of Area, Digital Storage, Energy, Length, Mass, Speed, Temprature, Time and Volume")

#Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Area", "Digital Storage", "Energy","Length", "Mass", "Speed", "Temprature" ,"Time", "Volume"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)

col1,col2 = st.columns(2)

if conversion_type == "Area":
    with col1:
        from_unit = st.selectbox("From", ['Square Kilometer','Square Meter', 'Square Centimeter',  'Square Mile', 'Square Yard', 'Square Feet', 'Square Inch', 'Hectare' 'Acre'])
    with col2:
        to_unit = st.selectbox("To", ['Square Kilometer','Square Meter', 'Square Centimeter',  'Square Mile', 'Square Yard', 'Square Feet', 'Square Inch', 'Hectare' 'Acre'])

elif conversion_type == "Digital Storage":
    with col1:
        from_unit = st.selectbox("From", ['Bit','Kilobit', 'Kibibite', 'Megabit', 'Mebibit', 'Gigabit', 'Gibibit', 'Terabit', 'Tebibit', 'Petabit', 'Pebibit' 'Byte', 'KiloByte', 'Kilibyte', 'Megabyte','Mebibyte', 'Mebibyte', 'Gegabyte','Gebibyte', 'Terabyte', 'Tebibyte', 'Petabyte', 'Pebibyte' ])
    with col2:
        to_unit = st.selectbox("To", ['Bit','Kilobit', 'Kibibite', 'Megabit', 'Mebibit', 'Gigabit', 'Gibibit', 'Terabit', 'Tebibit', 'Petabit', 'Pebibit' 'Byte', 'KiloByte', 'Kilibyte', 'Megabyte','Mebibyte', 'Mebibyte', 'Gegabyte','Gebibyte', 'Terabyte', 'Tebibyte', 'Petabyte', 'Pebibyte' ])

elif conversion_type == "Energy":
    with col1:
        from_unit = st.selectbox("From", ['Joule','Kilojoule', 'Gram Calorie',  'Kilo Calorie', 'Watt-hour', 'Kilowatt-hour', 'Eloctron Vlot', 'British Thermal Unit', 'US Therm', 'Foot-Pound'])
    with col2:
        to_unit = st.selectbox("To", ['Joule','Kilojoule', 'Gram Calorie',  'Kilo Calorie', 'Watt-hour', 'Kilowatt-hour', 'Eloctron Vlot', 'British Thermal Unit', 'US Therm', 'Foot-Pound'])

elif conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ['Kilometer','Meter', 'Centimeter', 'Milimeter', 'Micrometer', 'Nanometer', 'Mile', 'Yard', 'Feet', 'Inch', 'Nauticle mile'])
    with col2:
        to_unit = st.selectbox("To", ['Kilometer','Meter', 'Centimeter', 'Milimeter', 'Micrometer', 'Nanometer', 'Mile', 'Yard', 'Feet', 'Inch', 'Nauticle mile'])

elif conversion_type == "Mass":
    with col1:
        from_unit = st.selectbox("From", ['Tonne','Kilogram', 'Gram',  'Miligram', 'Microgram', 'Imerial tone', 'US tone', 'Stone', 'Pound', 'Ounce'])
    with col2:
        to_unit = st.selectbox("To", ['Tonne','Kilogram', 'Gram',  'Miligram', 'Microgram', 'Imerial tone', 'US tone', 'Stone', 'Pound', 'Ounce'])

elif conversion_type == "Speed":
    with col1:
        from_unit = st.selectbox("From", ['Mile per Houre','Foot per Second', 'Meter per Second',  'Kelomerter per Hour', 'Knote'])
    with col2:
        to_unit = st.selectbox("To", ['Mile per Houre','Foot per Second', 'Meter per Second',  'Kelomerter per Hour', 'Knote'])

elif conversion_type == "Temprature":
    with col1:
        from_unit = st.selectbox("From", ['Celsius','Fahrenheit', 'Kalvin'])
    with col2:
        to_unit = st.selectbox("To", ['Celsius','Fahrenheit', 'Kalvin'])

elif conversion_type == "Time":
    with col1:
        from_unit = st.selectbox("From", ['Nanosecond','Microsecond', 'Milisecond', 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Calender Year', 'Decade', 'Century'])
    with col2:
        to_unit = st.selectbox("To", ['Nanosecond','Microsecond', 'Milisecond', 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Calender Year', 'Decade', 'Century'])

elif conversion_type == "Volume":
    with col1:
        from_unit = st.selectbox("From", ['US Liquid Gallon','US Liquid Quart', 'US Liquid Pint', 'US Legal Cup', 'US Fluid Once', 'US Tablespoon', 'US Teapoon', 'Cubic Meter', 'Litre', 'Mililitre', 'Imperial Liquid Gallon','Imperial Liquid Quart', 'Imperial Liquid Pint', 'Imperial Legal Cup', 'Imperial Fluid Once', 'Imperial Tablespoon', 'Imperial Teapoon', 'Cubic Feet', 'Cubic Inch'])
    with col2:
        to_unit = st.selectbox("To", ['US Liquid Gallon','US Liquid Quart', 'US Liquid Pint', 'US Legal Cup', 'US Fluid Once', 'US Tablespoon', 'US Teapoon', 'Cubic Meter', 'Litre', 'Mililitre', 'Imperial Liquid Gallon','Imperial Liquid Quart', 'Imperial Liquid Pint', 'Imperial Legal Cup', 'Imperial Fluid Once', 'Imperial Tablespoon', 'Imperial Teapoon', 'Cubic Feet', 'Cubic Inch'])


# Conversion Function
def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Kilometer':0.001, 'Meter':1, 'Centimeter':100, 'Milimeter':1000, 'Micrometer':100000, 'Nanometer':1e+9, 'Mile':0.000621371, 'Yard':1.09361, 'Feet':3.28084, 'Inch':39.3701, 'Nauticle mile':0.000539957
    }
    return(value / length_units[from_unit] * length_units[to_unit])

def mass_convertor(value, from_unit, to_unit):
    mass_units = {
        'Tonne':0.001, 'Kilogram':1, 'Gram':1000, 'Miligram':1e+6, 'Microgram':1e+9, 'Imerial tone':0.000984207, 'US tone':0.00110231, 'Stone':0.157473, 'Pound':2.20462, 'Ounce':35.274
    }
    return(value / mass_units[from_unit] * mass_units[to_unit])

def temprature_convertor(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kalvin" else value 
    elif from_unit == 'Fahrenheit':
        return (value - 32 ) *5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kalvin" else value
    elif from_unit == 'Kalvin':
        return value -273.15 if  to_unit == "Celsius" else (value -273.15) * 9/5 + 32 if to_unit == "Fahrentheit" else value 
    return value

#Button for Conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Mass":
        result = mass_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temprature":
        result = temprature_convertor(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)
    # st.markdown(f"<div class = 'formula-box'>"Formula", {}</div>")
st.markdown("<div class = 'footer'>Create by Afia Bakr</div>", unsafe_allow_html=True)
