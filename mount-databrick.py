# Databricks notebook source
Application (client) ID : *****
Object ID : *****
Directory (tenant) ID : ****
secret_value = ****
secret_id = *****


# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "******",
          "fs.azure.account.oauth2.client.secret": "*****",
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/*****/oauth2/token"}

          # Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://raw@musicetllake.dfs.core.windows.net/",
  mount_point = "/mnt/raw",
  extra_configs = configs)


# COMMAND ----------

#mount processed container

# COMMAND ----------


dbutils.fs.mount(
  source = "abfss://processed@musicetllake.dfs.core.windows.net/",
  mount_point = "/mnt/processed",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/processed")

# COMMAND ----------

dbutils.fs.ls("/mnt/raw")

# COMMAND ----------

#replacing the placeholder with actual values 
blob_storage_name = "musicetlproject"
storage_account_key = "https://musicetlproject.blob.core.windows.net/incomingartistdata?sp=racwdli&st=2024-11-10T05:45:53Z&se=2024-11-12T13:45:53Z&spr=https&sv=2022-11-02&sr=c&sig=%2FYAcgv7xvrGm1BwKFmqHHiRuzEX%2F4Xg7c4B%2F%2FSXKfTE%3D"
blob_container_name = "incomingartistdata"

dbutils.fs.mount(
 source = f"wasbs://{blob_container_name}@{blob_storage_name}.blob.core.windows.net/",
 mount_point = "/mnt/musicetlproject",
 extra_configs = {f"fs.azure.sas.{blob_container_name}.{blob_storage_name}.blob.core.windows.net": storage_account_key}
)

# COMMAND ----------

