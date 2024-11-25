# Python Script: CSV Image Downloader

## Table of Contents
- [Python Script: CSV Image Downloader](#python-script-csv-image-downloader)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)

---

## Introduction

This Python script automates the process of reading a CSV file, downloading images from URLs provided in the file, and saving the images with dynamically generated filenames based on specific fields (`Row Number`, `Supplier Name`, and `Submitted By`). It is a useful utility for managing image assets linked to datasets in a structured and automated way.

---

## Features

- Reads image URLs from a CSV file.
- Dynamically generates filenames using:
  - Row number
  - Supplier name
  - Submitted by field
- Downloads and saves images locally.
- Handles errors gracefully, such as invalid URLs or download failures.

---

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone git@github.com:waeltech/Python_Bulk_Downloader.git

2. Clone the repository or download the script:
   ```bash
   pip install pandas requests
2. Clone the repository or download the script:
   ```bash
   python3 test.py