# 🎬 MovieAnalytics – Movie Data Analysis Using Medallion Architecture

## 📌 Project Overview
MovieAnalytics is a data engineering project designed to analyze movie popularity and audience engagement using a structured **Medallion Architecture (Bronze, Silver, Gold)** approach.

The dataset includes:
- Original Title
- Original Language
- Genre
- Overview
- Popularity
- Vote Count
- Vote Average

This project demonstrates how raw data can be transformed into analytics-ready datasets using industry best practices.

---

## 🏗️ Architecture Overview
The project follows the **Medallion Architecture** pattern:

Bronze Layer → Silver Layer → Gold Layer

Each layer has a specific responsibility to ensure data quality, scalability, and analytical usability.

---

## 🥉 Bronze Layer – Raw Data Ingestion
**Purpose:** Maintain raw data integrity

- Ingested raw movie data into the catalog as `movie_data`
- Preserved original schema without transformations
- Created a Databricks notebook and assigned data to a working variable
- Acts as the single source of truth

---

## 🥈 Silver Layer – Data Cleaning & Standardization
**Purpose:** Improve data quality

- Removed duplicate records
- Identified and handled null values
- Applied business rules:
  - Text fields → `Unknown`
  - Numeric fields → `0`
- Validated schema and data types
- Stored cleaned data in cloud storage as **Parquet format**
- Updated or overwrote existing catalog tables

---

## 🥇 Gold Layer – Business Analytics
**Purpose:** Generate insights

- Applied transformations using:
  - `AVG`, `SUM`, `COUNT`
- Grouped data by:
  - Genre
  - Language
- Ranked movies by popularity and voting metrics
- Produced analytics-ready tables for reporting and dashboards

---

## 📊 Use Cases
- Identify most popular movies by genre and language
- Analyze audience engagement using vote metrics
- Enable BI dashboards using Power BI or Tableau

---

## 🛠️ Tech Stack
- Databricks
- SQL
- Cloud Storage
- Parquet File Format
- GitHub

---

## 🚀 Key Takeaways
- Implemented a real-world data engineering pipeline
- Followed best practices using Medallion Architecture
- Ensured data reliability and performance
- Designed datasets ready for business analytics

---

## 📂 Repository Structure
