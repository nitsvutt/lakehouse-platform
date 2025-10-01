# Lakehouse Platform

![license](https://img.shields.io/github/license/nitsvutt/lakehouse-platform)
![stars](https://img.shields.io/github/stars/nitsvutt/lakehouse-platform)
![forks](https://img.shields.io/github/forks/nitsvutt/lakehouse-platform)

## Table of Contents
1. [Introduction](#introduction)
2. [Architecture](#architecture)
3. [In progress](#in-progress)


<div id="introduction"/>

## 1. Introduction

These days, data becomes the DNA of every organization including both startups and big corporations. The more an enterprise leverages the data, the more competitive advantages it gains. After defining where are data sources, all of them always require a "single source of truth" for furthure actions, such as reporting and advance analytics. This project aims to introduce an universal solution known as a **Data Lakehouse Platform**.

<div id="architecture"/>

## 2. Architecture

<p align="center">
  <img src="https://github.com/nitsvutt/lakehouse-platform/blob/main/asset/lakehouse-platform.png" width="100%" title="architecture" alt="architecture">
</p>

- Data source: 
    - Flat files: diverse file formats from users (Example: CSV, XML).
    - Database: application databases (Example: MySQL, PostgreSQL).
    - Others: external APIs, sensors, streaming services.
- Data platform:
    - Event streaming: store or buffer event between systems (Example: Apache Kafka).
    - Batch processing: process large datasets or run scheduled jobs (Example: Apache Spark, Apache Trino, Apache Airflow).
    - Stream processing: support low-latency and realtime applications (Example: Apache Flink).
    - Data lakehouse:
        - Storage:
            - Distributed File System or Object Storage: play as a central repository storing your data (Example: Apache Hadoop).
            - High-performance Database (Depend on use case): play as a staging storage for realtime applications (Example: ScyllaDB).
        - Table format: support ACID for tables (Example: Apache Iceberg).
        - Metastore: store table metadata supporting query engines quickly access this information (Example: Apache Hive).
    - Data Marts +/ Warehouse (Depend on use case): play as an OLAP layer for BI & Reporting (Example: StarRocks, Apache Druid).
    - User interface: serve users (Example: Jupyter, DBeaver, Apache Superset, Imply).

<div id="in-progress"/>

## 3. In progress