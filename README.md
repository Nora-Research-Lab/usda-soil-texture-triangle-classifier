<p align="center">
  <img src="https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg" width="72" alt="NORA logo" />
</p>
 
<h1 align="center">USDA Soil Texture Triangle Classifier</h1>
<p align="center"><em>For agronomists and soil scientists: enter sand, silt, and clay percentages and instantly get the USDA textural class and a triangle plot.</em></p>
 
<p align="center">[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
</p>
 

## Overview
 
**Industry:** Soil Science
 
The app classifies a soil sample into its USDA textural class from laboratory particle-size percentages. The user provides three numeric inputs: percent sand, percent silt, and percent clay, each between 0 and 100. The Gradio UI uses a left panel with three Number inputs labeled Sand %, Silt %, and Clay %, a Classify button, and a note that values should sum to 100. The app validates that the three values sum to 100 within a tolerance of 0.5 percentage points; if not, it normalizes them by dividing each value by the total so the soil texture triangle logic still works, and displays a note that normalization was applied. The core logic is a deterministic ternary polygon lookup. The 12 USDA texture classes are stored as closed polygons in ternary coordinates: sand, loamy sand, sandy loam, loam, silt loam, silt, sandy clay loam, clay loam, silty clay loam, sandy clay, silty clay, and clay. Each polygon follows the standard USDA texture triangle boundary definitions. The user point is converted to ternary coordinates and tested against each polygon using a point-in-polygon algorithm in a fixed priority order. The first matching polygon returns the class name. The right panel shows two outputs: a text output with the USDA class name, and a Plotly ternary chart. The chart draws the standard USDA texture triangle with colored class polygons and a red marker at the user sample point. If inputs are invalid, negative, or greater than 100, the tool shows a clear error message and does not draw the point. No AI or machine learning component is used; this is a standards-based classification tool.
 
## Run it
 
```bash
docker build -t usda-soil-texture-triangle-classifier .
docker run -p 7860:7860 usda-soil-texture-triangle-classifier
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-17.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
