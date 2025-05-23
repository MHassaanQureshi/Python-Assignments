import streamlit as st 

st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("Unit Converter")

# Conversion dictionaries
length_conversion = {
    "Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Micrometer": 1e-6, 
    "Nanometer": 1e-9, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254, "Light Year": 9.461e15
}

volume_conversion = {
    "Liter": 1, "Milliliter": 0.001, "Cubic Meter": 1000, "Cubic Centimeter": 0.001, "Cubic Millimeter": 1e-6, 
    "Gallon (US)": 3.78541, "Gallon (UK)": 4.54609, "Quart (US)": 0.946353, "Pint (US)": 0.473176, "Cup": 0.24, "Fluid Ounce (US)": 0.0295735
}

weight_conversion = {
    "Kilogram": 1, "Gram": 0.001, "Milligram": 1e-6, "Microgram": 1e-9, "Metric Ton": 1000, 
    "Pound": 0.453592, "Ounce": 0.0283495, "Stone": 6.35029
}

area_conversion = {
    "Square Meter": 1, "Square Kilometer": 1e6, "Square Centimeter": 0.0001, "Square Millimeter": 1e-6, 
    "Hectare": 10000, "Acre": 4046.86, "Square Mile": 2.59e6, "Square Yard": 0.836127, "Square Foot": 0.092903, "Square Inch": 0.00064516
}

time_conversion = {
    "Second": 1, "Millisecond": 0.001, "Microsecond": 1e-6, "Nanosecond": 1e-9, 
    "Minute": 60, "Hour": 3600, "Day": 86400, "Week": 604800, "Month (30 days)": 2592000, "Year": 31536000
}


unit_conversions = {
    "Length": length_conversion,
    "Volume": volume_conversion,
    "Weight": weight_conversion,
    "Area": area_conversion,
    "Time": time_conversion
}


choice = st.selectbox("Select a category", list(unit_conversions.keys()))


conversion_dict = unit_conversions[choice]


from_unit = st.selectbox("Select the unit you want to convert from", list(conversion_dict.keys()))
to_unit = st.selectbox("Select the unit you want to convert to", list(conversion_dict.keys()))
value = st.number_input(f"Enter the value in {from_unit}", min_value=0.0)


if st.button("Convert"):
    converted_value = value * (conversion_dict[from_unit] / conversion_dict[to_unit])
    st.success(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
