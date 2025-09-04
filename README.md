# Terraform Azure Demo

This project demonstrates how to use **Terraform** and **Python** to interact with **Microsoft Azure** cloud services. It includes a simple example of uploading and downloading files from an Azure Storage Account.

## Features
- ⚙️ Provision Azure resources using Terraform (IaC)
- Provision Azure resources (Resource Group, Storage Account, Storage Container) using Terraform.
- Upload and download files to Azure Blob Storage using Python (`azure-storage-blob` package).
- Example files included for testing: `test_upload.txt` and `downloaded_test.txt`.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed.
- [Python 3](https://www.python.org/downloads/) installed.
- Azure account (free tier works fine).
- Python packages:  
  ```bash
  pip install azure-storage-blob

## Setup & Usage
1. Clone the repo
2. Initialize Terraform: `terraform init`
3. Apply Terraform configuration: `terraform apply`
4. Set `CONNECTION_STRING` in `azure_demo.py`
5. Run Python script: `python azure_demo.py`

## Project Structure
- `main.tf` - Terraform configuration
- `versions.tf` - Terraform provider versions
- `azure_demo.py` - Python script to upload/download files
- `test_upload.txt` - Example file for upload
- `downloaded_test.txt` - Example downloaded file
- `LICENSE`, `README.md` - Documentation
