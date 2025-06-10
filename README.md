# NEPSE Index Performance: Trends, Changes, and Investor Sentiment (2020–2025)
![GitHub Gist stars](https://img.shields.io/github/gist/stars/:gistId) ![Stack Exchange questions](https://img.shields.io/stackexchange/:stackexchangesite/t/:query)  ![GitHub License](https://img.shields.io/github/license/:user/:repo)
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9d6ae523",
   "metadata": {},
   "source": [
    "  \n",
    " # NEPSE Index Performance: Trends, Changes, and Investor Sentiment (2020–2025)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8687dbcf",
   "metadata": {},
   "source": [
    "<img src=\"https://i1.wp.com/kaamkura.com/wp-content/uploads/2021/06/Nepse-Chart.png?resize=768%2C502&ssl=1\" alt=\"NEPSE Chart\" width=\"400\"/>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6261050",
   "metadata": {},
   "source": [
    "# About the Dataset  \n",
    "## NEPSE Daily Index Data (2020-2025)\n",
    "\n",
    "This dataset contains daily records of the Nepal Stock Exchange (NEPSE) Index from January 1, 2020, to March 4, 2025. The NEPSE Index reflects the overall performance of Nepal’s stock market by tracking the value of listed companies.\n",
    "\n",
    "---\n",
    "\n",
    "## What’s in the Dataset?  \n",
    "- **Date:** The trading day (e.g., 2025-03-04).  \n",
    "- **Index Value:** The closing value of the NEPSE Index for that day.  \n",
    "- **Absolute Change:** How much the index changed from the previous day (in points).  \n",
    "- **Percentage Change:** The daily percentage change (how much the index went up or down).\n",
    "\n",
    "---\n",
    "\n",
    "## Data Details  \n",
    "- Covers over 5 years of daily trading data (excludes weekends and holidays).  \n",
    "- Contains around 1,200 to 1,500 rows of data.  \n",
    "- Data sourced from ShareSansar, a popular Nepal financial website.  \n",
    "- Collected and cleaned using automated Python tools.\n",
    "\n",
    "---\n",
    "\n",
    "<!-- ## How Can You Use This Data?  \n",
    "- Analyze trends in Nepal’s stock market.  \n",
    "- Forecast future index values with models like ARIMA or LSTM.  \n",
    "- Study market growth and volatility.  \n",
    "- Create charts and graphs to visualize daily changes.  \n",
    "- Learn financial data analysis using real market data. -->\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3f83815",
   "metadata": {},
   "source": [
    "## Source of Data  \n",
    "Dataset retrieved from [Kaggle](https://www.kaggle.com/datasets/suyogghimire/nepse-daily-index-data-2020-2025).\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ca10477",
   "metadata": {},
   "source": [
    "## 🎯 Objective of Analyzing NEPSE Data:\n",
    "### 1. Identify trend (upward/downward)\t\n",
    "### 2. Track Daily Market Performance"
   ]
  },



## Overview

This repository contains the NEPSE Daily Index Data from January 1, 2020, to March 4, 2025. This dataset offers insights into the overall performance of Nepal's stock market by tracking the value of listed companies. It is a valuable resource for analyzing market trends, changes, and investor sentiment over the specified period.

## About the Dataset

This dataset provides daily records of the Nepal Stock Exchange (NEPSE) Index from January 1, 2020, to March 4, 2025. The NEPSE Index is a key indicator of Nepal’s stock market performance, reflecting the collective value of companies listed on the exchange.

## What’s in the Dataset?

The dataset includes detailed information about the NEPSE Index, such as:

* **Yearly Trends (2020-2025):**
    * **2020:** The index began around 1500, dropping to below 1200 during the initial lockdown, then recovering to end the year near 1800.
    * **2021:** A bullish year, with the index consistently above 2500 and peaking near 3200.
    * **2022:** A bear market, with the index falling below 2000 from a peak of 2750.
    * **2023:** Continued downward trend, with the index fluctuating between 1800 and 2200, but showing some recovery towards the end.
    * **2024:** A period of volatility, with the index mostly below 2000, reaching a peak of around 3000.
    * **2025:** NEPSE shows signs of stabilization, staying mostly between 2750 and 3000.
* **Daily Market Performance:**
    * Daily percentage and absolute changes mostly hovered near zero, showing no long-term bias toward increase or decrease.
    * The median of daily point change is close to zero → most changes are small.
    * Outliers exist, with a few extreme changes (±150 points), reflecting possible macroeconomic or political impacts.
    * The box plot shows a central index value of ~2000–2050 with no extreme outliers, indicating moderate stability.
    * The distribution is slightly right-skewed, meaning occasional higher values, but generally balanced.

---

<sub>Made by Sanjaaya Kumar Giri</sub>
