# Databricks notebook source
dbutils.widgets.text("catalog_name", "")
dbutils.widgets.text("source_system", "")
dbutils.widgets.text("bundle_path", ".")


bundle_path = dbutils.widgets.get("bundle_path")
catalog_name = dbutils.widgets.get("catalog_name")
source_system = dbutils.widgets.get("source_system")

# add bundle to PATH
import sys

sys.path.append(bundle_path)

# now import relative modules
from src.utilities.demo import utility_function

utility_function()

print(f"""{catalog_name=}""")
print(f"""{source_system=}""")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC show schemas in ${catalog_name};
