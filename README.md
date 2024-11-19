# software_weakness_analysis
This project analyzes software vulnerabilities from the Exploit Database, using Python and Pandas to provide insights into exploit patterns across various platforms for improved security awareness.
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results and Visualizations](#results-and-visualizations)
- [Technologies Used](#technologies-used)
- [License](#license)
## Project Overview
This project aims to analyze software vulnerabilities by gathering data from the Exploit Database and processing it with Python and Pandas. The project provides valuable insights into commonly targeted platforms and types of vulnerabilities.
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/NehaBL/software_weakness_analysis.git
   cd software_weakness_analysis
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
## Usage
To run the analysis, execute the following command:
```bash
python3 load_exploit_data.py
## Methodology
The project loads data from a CSV file, processes it using Pandas, and visualizes the results with Matplotlib. The data is sourced from the Exploit Database and includes information on platform types, exploit categories, and more.
## Results and Visualizations
### Exploit Counts by Platform
![Exploit Counts by Platform](exploit_counts_by_platform.png)
## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn (if applicable)

