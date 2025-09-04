# Configure the Azure provider
provider "azurerm" {
  features {}
}

# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = "rg-demo-free"
  location = "West Europe"
}

# Storage Account (free-tier eligible)
resource "azurerm_storage_account" "storage" {
  name                     = "demostorage${random_integer.suffix.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# Random integer to avoid name collisions
resource "random_integer" "suffix" {
  min = 10000
  max = 99999
}

# Storage Container
resource "azurerm_storage_container" "container" {
  name                  = "files"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}
