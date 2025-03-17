from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_html():
    html_content = """
    <html>
<head>
    <style>
        #head {
            background-color: orange;
            color: white;
            padding: 5%;
            text-align: center;
            text-decoration: underline double;
        }
        #menu {
            margin-left: 2%;
            font-size: 120%;
        }
        .subhead {
            background-color: grey;
            color: white;
            padding: 10px;
            text-align: center;
        }
    </style>
    <link rel="stylesheet" type="text/css" href="Exp1.css">
</head>
<body style="border-left: 5px solid orange;">
    <div>
        <h1 id="head">Mandhi Mansil</h1>
        <h3 class="subhead">India / Kollam, Kerala / MANDI MANZIL</h3>
    </div>

    <div id="menu">
        <h2>MENU</h2>
        <p id="item"> Chicken Mandi  <br></p>
        <p style="margin-left: 5%;">₹149<br>Mayonnaise and salata</p>
        <img src="chicken.jpeg" alt="ERROR">

       
    </div>
</body>
</html>

    """
    return html_content