from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Drought Analysis - Maharashtra</title>

    <style>
        body{
            margin:0;
            font-family:Arial;
            background:#f4f6f9;
        }

        .header{
            background:linear-gradient(90deg,#1a237e,#0d47a1);
            color:white;
            padding:20px;
            text-align:center;
            font-size:26px;
        }

        .container{
            width:80%;
            margin:auto;
            padding:20px;
        }

        .card{
            background:white;
            padding:20px;
            margin:15px 0;
            border-radius:12px;
            box-shadow:0 5px 15px rgba(0,0,0,0.1);
        }

        h2{
            color:#0d47a1;
        }

        .map{
            width:100%;
            height:300px;
            background:linear-gradient(135deg,#90caf9,#e3f2fd);
            border-radius:10px;
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:18px;
            color:#0d47a1;
            font-weight:bold;
        }

        .footer{
            background:#1a237e;
            color:white;
            text-align:center;
            padding:10px;
            margin-top:20px;
        }
    </style>
</head>

<body>

<div class="header">
🌍 Drought Analysis in Maharashtra (GIS Blog)
</div>

<div class="container">

<div class="card">
<h2>📌 Introduction</h2>
<p>
Drought is a major environmental issue in Maharashtra affecting agriculture, water supply, and rural livelihoods.
Regions like Marathwada and Vidarbha frequently face severe water scarcity due to irregular rainfall and climate change.
</p>
</div>

<div class="card">
<h2>📊 GIS Importance</h2>
<p>
Geographic Information System (GIS) helps in monitoring rainfall patterns, soil moisture, groundwater levels, and drought intensity.
It supports decision-making for disaster management and agriculture planning.
</p>
</div>

<div class="card">
<h2>🌦 Affected Regions in Maharashtra</h2>
<ul>
<li>Vidarbha</li>
<li>Marathwada</li>
<li>Western Maharashtra (some districts)</li>
</ul>
</div>

<div class="card">
<h2>🗺 GIS Map View (Sample)</h2>
<div class="map">
Maharashtra Drought Risk Map Visualization Area
</div>
</div>

<div class="card">
<h2>📉 Causes of Drought</h2>
<ul>
<li>Low rainfall</li>
<li>Deforestation</li>
<li>Climate change</li>
<li>Overuse of groundwater</li>
</ul>
</div>

<div class="card">
<h2>💡 Solutions</h2>
<ul>
<li>Rainwater harvesting</li>
<li>Drip irrigation</li>
<li>Afforestation</li>
<li>GIS-based monitoring systems</li>
</ul>
</div>

</div>

<div class="footer">
© 2026 GIS Drought Analysis Blog | Maharashtra Project
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)