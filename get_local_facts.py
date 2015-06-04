import json
import ansible.runner
import ansible.inventory

inventory = ansible.inventory.Inventory(["localhost"])

runner = ansible.runner.Runner(module_name='setup',
                               module_args='',
                               pattern='localhost',
                               inventory=inventory,
                               transport="local"
                               )
result = runner.run()
print(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))
