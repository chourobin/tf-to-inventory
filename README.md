# Terraform to Inventory

This is a small python script that generates an Ansible [inventory](http://docs.ansible.com/intro_inventory.html)  from a [Terraform](https://terraform.io/) state file. You can spawn a lot of VMs using Terraform and then provision them with Ansible.

## Usage

```python
# whereever your terraform.tfstate file is located, run:
python tf-to-inventory.py
# => hosts
```

Look at the example hosts file to see the output of this script.

## Acknowledgement

Inspired by the [zookeeper-ansible-terraform](https://github.com/ianunruh/zookeeper-ansible-terraform) recipe. I adopted much of the code and added support for Amazon EC2 instances.

## License

MIT
