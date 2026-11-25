
# 🚗 Car Sales Dashboard

This project focuses on the development and deployment of an interactive web application for exploring used car advertisement data in the United States, combining data analysis and software engineering.

This interactive application was developed with [Streamlit](https://streamlit.io/) to explore used car listings across the United States. It allows users to visualize distributions and relationships between variables such as mileage, price, model year, fuel type, and other vehicle characteristics.

## 1. Project Objective

Develop a dynamic dashboard for exploratory data analysis (EDA) of the automotive market.

The goal is to allow end users to intuitively explore price distributions, mileage patterns, and correlations between variables through interactive visualization tools and cloud infrastructure.

## 2. Results

- **Public Application:** Deployment of a functional dashboard hosted in the cloud.
- **Interactive Visual Analysis:** Development of histograms and scatter plots that respond to user inputs in real time.
- **Online Access:** 🔗 [Access the Dashboard on Render](https://car-sales-dashboard-iauy.onrender.com/)

## 3. Tools & Technologies

- **Programming Language:** Python 3.8+
- **Libraries:** Streamlit, Pandas, Plotly Express.
- **DevOps & Cloud:** Git, GitHub, Render (Hosting).
- **Development Environment:** VS Code and Virtualenv (Virtual Environments).

## 4. Skills Developed

- **Software Engineering for Data Applications:** Managing virtual environments, organizing configuration files (`config.toml`), and managing project dependencies (`requirements.txt`).
- **Cloud Deployment:** Implementing automated deployment workflows (Continuous Deployment) through Render.
- **Interactive Data Visualization:** Building dynamic charts with Plotly that go beyond the limitations of static visualizations.
- **Technical Documentation and Standardization:** Creating technical documentation focused on results and processes, following technology industry best practices.

## 5. Future Improvements

- **Advanced Filters:** Implementing sidebar filters for vehicle make, model, and manufacturing year.
- **KPI Metrics:** Adding indicators such as average price and listing volume by category.
- **Performance Optimization:** Implementing data caching to improve application loading times when working with larger datasets.

## 💻 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/andrezacarrano/car-sales-dashboard.git
   ```

2. Navigate to the project directory:

   ```bash
   cd car-sales-dashboard
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```text
car-sales-dashboard/
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── .streamlit/
│   └── config.toml
├── notebooks/
│   └── EDA.ipynb
└── README.md
```

## 📋 Requirements

- Python 3.8+
- Streamlit
- Pandas
- Plotly

## 📊 Data Source

The `vehicles_us.csv` dataset contains information about used car listings in the United States, including price, model year, vehicle model, fuel type, mileage, and other characteristics.

## 🌐 Live Demo

Access the application online:

[Car Sales Dashboard – Render](https://car-sales-dashboard-iauy.onrender.com/)

---

**Author:** Andreza Carrano

[LinkedIn](https://www.linkedin.com/in/andrezacarrano-dados/) | [GitHub](https://github.com/andrezacarrano)
