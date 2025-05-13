import csv
import yaml
import sys

csv_file = 'publications_.csv'
yaml_file = 'publications.yml'

with open(csv_file, 'r', encoding='utf-8') as f:
    import csv, yaml
    data = list(csv.DictReader(f))

with open(yaml_file, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)

print(f"Converted {csv_file} to {yaml_file}")
