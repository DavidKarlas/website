---
title: Dvig morja v Sloveniji
date: git Last Modified
topics: dvig morja
summary: Pokazali bomo kako se bo skozi leta in v različnih scenarijih dvigalo in poplavljalo morje.
---

# Dvig morja v Sloveniji in svetu
Razložimo kako in zakaj se bo morje po svetu dvigalo. Razložimo zakaj se bo dvigalo v Sloveniji približno enako kot drugje po svetu.

<object id="svgGraph" class="svgGraph w-96" type="image/svg+xml"></object>

Razlaga kaj je RCP4.5, RCP8.5, link na [ipcc report.](https://www.ipcc.ch/srocc/chapter/chapter-4-sea-level-rise-and-implications-for-low-lying-islands-coasts-and-communities/)

# Scenariji dviga

Pokazali bomo več scenarijev dviga, RCP4.5, RCP8.5...

# Razlaga kdaj se zgodijo poplave
Zgodijo se ko se jugo na jadranu pokrije z plimo, in mogoče poskusimo razložiti efekt "vala v kadi".

## Razlaga depresije, in to ni isto kot poplave

Vizualizacije spodaj prikazujejo depresije, ki niso nujno poplave...

## Dvig po RCP4.5, ko NE poplavlja

<div id="seaRise45NoFlood">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin="">
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet-fullscreen@1.0.2/dist/leaflet.fullscreen.css" integrity="sha512-Tbna5DrK+N26ZZczWjdHj7BHyU3vUAjA7JsGhIyTM/7jBiy4f4DbiScuLQxaxB51+Gh/+a+Z7AwQmh2FyafjLg==" crossorigin="">
    <script src="https://unpkg.com/leaflet-fullscreen@1.0.2/dist/Leaflet.fullscreen.min.js" integrity="sha512-N/rydaIg6KU3Pvy8M0RZTQoMBsgA3+oKZ5dWY3lvGoT7DeOyLI0rhNb12OGmu8zRixAOXJvs8QQ02zcbkjwx8g==" crossorigin=""></script>
    <script type="module">
        import SeaRise from '/code/dvig-morja/index.jsx'
        SeaRise(document.getElementById('seaRise45NoFlood'), document.getElementById('svgGraph'), true, false)
    </script>
    <div class="chart map h-80"></div>
    <div>
        <input class="yearSelectionSlider w-full" type="range" min="2020" max="2100" value="2050">
    </div>
</div>

## Dvig po RCP4.5, ko poplavlja

<div id="seaRise45Flood">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin="">
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet-fullscreen@1.0.2/dist/leaflet.fullscreen.css" integrity="sha512-Tbna5DrK+N26ZZczWjdHj7BHyU3vUAjA7JsGhIyTM/7jBiy4f4DbiScuLQxaxB51+Gh/+a+Z7AwQmh2FyafjLg==" crossorigin="">
    <script src="https://unpkg.com/leaflet-fullscreen@1.0.2/dist/Leaflet.fullscreen.min.js" integrity="sha512-N/rydaIg6KU3Pvy8M0RZTQoMBsgA3+oKZ5dWY3lvGoT7DeOyLI0rhNb12OGmu8zRixAOXJvs8QQ02zcbkjwx8g==" crossorigin=""></script>
    <script type="module">
        import SeaRise from '/code/dvig-morja/index.jsx'
        SeaRise(document.getElementById('seaRise45Flood'), document.getElementById('svgGraph'), true, true)
    </script>
    <div class="chart map h-80"></div>
    <div>
        <input class="yearSelectionSlider w-full" type="range" min="2020" max="2100" value="2050">
    </div>
</div>

## Dvig po RCP8.5, ko NE poplavlja

<div id="seaRise85NoFlood">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin="">
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet-fullscreen@1.0.2/dist/leaflet.fullscreen.css" integrity="sha512-Tbna5DrK+N26ZZczWjdHj7BHyU3vUAjA7JsGhIyTM/7jBiy4f4DbiScuLQxaxB51+Gh/+a+Z7AwQmh2FyafjLg==" crossorigin="">
    <script src="https://unpkg.com/leaflet-fullscreen@1.0.2/dist/Leaflet.fullscreen.min.js" integrity="sha512-N/rydaIg6KU3Pvy8M0RZTQoMBsgA3+oKZ5dWY3lvGoT7DeOyLI0rhNb12OGmu8zRixAOXJvs8QQ02zcbkjwx8g==" crossorigin=""></script>
    <script type="module">
        import SeaRise from '/code/dvig-morja/index.jsx'
        SeaRise(document.getElementById('seaRise85NoFlood'), document.getElementById('svgGraph'), false, false)
    </script>
    <div class="chart map h-80"></div>
    <div>
        <input class="yearSelectionSlider w-full" type="range" min="2020" max="2100" value="2050">
    </div>
</div>

## Dvig po RCP8.5, ko poplavlja

<div id="seaRise85Flood">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin="">
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet-fullscreen@1.0.2/dist/leaflet.fullscreen.css" integrity="sha512-Tbna5DrK+N26ZZczWjdHj7BHyU3vUAjA7JsGhIyTM/7jBiy4f4DbiScuLQxaxB51+Gh/+a+Z7AwQmh2FyafjLg==" crossorigin="">
    <script src="https://unpkg.com/leaflet-fullscreen@1.0.2/dist/Leaflet.fullscreen.min.js" integrity="sha512-N/rydaIg6KU3Pvy8M0RZTQoMBsgA3+oKZ5dWY3lvGoT7DeOyLI0rhNb12OGmu8zRixAOXJvs8QQ02zcbkjwx8g==" crossorigin=""></script>
    <script type="module">
        import SeaRise from '/code/dvig-morja/index.jsx'
        SeaRise(document.getElementById('seaRise85Flood'), document.getElementById('svgGraph'), false, true)
    </script>
    <div class="chart map h-80"></div>
    <div>
        <input class="yearSelectionSlider w-full" type="range" min="2020" max="2100" value="2050">
    </div>
</div>