# Supply Chain Sustainability Reporting with Python 🌲
*4 steps to build an ESG reporting focusing CO2 emissions of your Distribution Network*

<p align="center">
  <img alt="The image shows a supply chain sustainability report illustrating CO2 emissions from different transportation methods. A distribution center supplies goods to customers through three routes: (1) via road (120 km), air (1450 km), and road again (700 km); (2) directly by road for 200 km; and (3) through road, sea, and road again. Each mode of transportation highlights the distances, representing the CO2 emissions linked to the transportation network’s sustainability calculated with Python." align="center" src="images/intro.png" width=75%>
</p>
<p align="center">Supply Chain Sustainability Reporting</p>

The demand for transparency in sustainable development from investors and customers has grown over the years.

Investors have placed an increased emphasis on business sustainability when assessing an organization's value and resiliency.

Therefore, more organizations are investing resources to build capabilities for sustainability reporting and determine the best strategies for a sustainable supply chain.

### Youtube Video
Click on the GIF below to access a short explainer video to understand the concept behind this solution
<div align="center">
  <a href="https://www.youtube.com/watch?v=yodNWnf7PQ0"><img src="https://github.com/samirsaci/supply-chain-sustainability/blob/main/thumbnail.webp" alt="Explainer Video Link"></a>
</div>

## **Article**
In this [Article](https://towardsdatascience.com/supply-chain-sustainability-reporting-with-python-161c1f63f267), we will introduce a simple methodology to **report the CO2 emissions of your Distribution Network** using **Python and PowerBI**.

## **Definition**
Based on the GHG Protocol corporate standard (Link), greenhouse gas emissions are classified into three scopes:

- Scope 1: direct emissions emissions released to the atmosphere because of the company’s activities (Company’s facilities like manufacturing plant/warehouses, company’s vehicles)
- Scope 2: indirect emissions from the generation of purchased energy
(purchased electricity, gas, ..)
- Scope 3: all indirect emissions (out of scope 2) occurring in the value chain of the company (Transportation, Waste of Operations, Business Travels, …)

In this article, we will focus on the Scope 3 calculations related to downstream transportation.
What is the environmental impact of your distribution network?

## **Formula**
Following the protocol the French Environmental Agency Ademe (Link), the formula to estimate the CO2 emissions of transportation is:

<p align="center">
  <img alt="A mathematical formula to calculate CO2 emissions based on emissions factors. The formula is structured as follows: “CO2 Emissions = Distance × Weight × Emission Factor.” This equation calculates the carbon dioxide emissions by multiplying the distance traveled by the weight of the goods transported and the emission factor (representing the rate of emissions per unit of weight and distance). The formula is used in the context of transportation-related emissions calculations." align="center" src="images/equation.png" width=75%>
</p>
<p align="center">Formula using Emission Factor</p>

## **Objective**

1. Based on this formula, we collect and process data to calculate the emissions.

<p align="center">
  <img alt="The image shows a data model for calculating supply chain CO2 emissions. “Master Data” includes item details like net weight. “Shipped Order Lines” contains shipment info (order number, warehouse, customer). “Business Units” holds warehouse data, while “Address Book” lists customer locations. “Distance by Mode” records transport distances (road, sea, air, rail) between warehouses and customers, used for CO2 emission calculations based on shipment and distance data." align="center" src="images/data collection.png" width=75%>
</p>
<p align="center">Data to be Collected</p>

2. We calculate the unit of measure conversions considering the shipped handling units.

<p align="center">
  <img alt="A flowchart shows three types of order packaging: full pallets, cartons, and individual units. Each order type follows a distinct path for packaging and palletization. For full pallets, the weight reference is the pallet; for cartons, it’s the carton, and for individual units, it’s converted into weight after being packed and palletized. This diagram visualizes how different order types are handled in supply chain processes, with weight reference at each stage of transportation." align="center" src="images/weight reference.png" width=75%>
</p>
<p align="center">Handling Units</p>

3. We add distances by mode and compute the CO2 emissions by order 

<p align="center">
  <img alt="" align="center" src="images/emissions factors.png" width=75%>
</p>
<p align="center">Emission by transportation mode</p>



## **Exemples of visuals using PowerBI**

### Bubble map with size = f(CO2 Total)
<p align="center">
  <img alt="A map visualization showing various cities in Europe, marked with blue bubbles. The size of the bubbles represents the total CO2 emissions. Locations include cities in the UK, France, and Germany, illustrating CO2 emissions across different regions of Europe." align="center" src="images/bubble map.png" width=75%>
</p>
<p align="center">Bubble Map</p>

_Visual Insights_

You can observe where you have the majority of CO2 emissions (large bubbles) with a color coding by transportation mode.

### Split by Country Destination and Item Code
<p align="center">
  <img alt="" align="center" src="images/bar chart.png" width=75%>
</p>
<p align="center">Bar Chart</p>

**Product Portfolio Insights**
For each market, which item has the highest environmental impact?

_Product Portfolio Insights_

For each market, which item has the highest environmental impact?

### CO2 = f(Turnover) by City Destination
<p align="center">
  <img alt="A bar chart with horizontal bars representing the total CO2 emissions by customer country. Germany has the highest emissions, followed by the United Kingdom, France, Bulgaria, and Mauritania." align="center" src="images/scatter plot.png" width=75%>
</p>
<p align="center">Scatter Plot</p>

_Financial Insights_

The impacts of your future efforts for CO2 Emission reductions on profitability will be higher for the customers in PEINE-WOLTORF.

# Code
This repository code you will find all the code used to explain the concepts presented in the article.

# About me 🤓
Senior Supply Chain Engineer with international experience working on Logistics and Transportation operations. \
Have a look at my portfolio: [Data Science for Supply Chain Portfolio](https://samirsaci.com) \
Data Science for Warehousing📦, Transportation 🚚 and Demand Forecasting 📈 
