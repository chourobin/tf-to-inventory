import json

hosts = {}
groups = {}

with open("terraform.tfstate") as fp:
    state = json.load(fp)

for module in state["modules"]:
    index = 0
    for key, resource in module["resources"].iteritems():
        values = key.split(".")
        resource_type, group_name = values[0], values[1]
        if len(values) == 3:
            index = int(values[2])

        attributes = resource["primary"]["attributes"]

        if resource_type == "aws_instance":
            name = attributes["id"]
            hosts[name] = attributes["public_dns"]
            groups.setdefault(group_name, {})[name] = {
                "index": index
            }

        if resource_type == "digitalocean_droplet" and attributes["status"] == "active":
            name = attributes["name"]
            hosts[name] = attributes["ipv4_address"]
            groups.setdefault(group_name, {})[name] = {
                "index": index
            }

with open("hosts", "w") as fp:
    for host, ip_address in hosts.iteritems():
        fp.write("{} ansible_ssh_host={} ansible_ssh_user=ubuntu\n".format(host, ip_address))

    fp.write("\n")

    for group, hosts in groups.iteritems():
        fp.write("[{}]\n".format(group))
        for host, variables in hosts.iteritems():
            fp.write(host)
            for k, v in variables.iteritems():
                fp.write(" {}={}".format(k, v))
            fp.write("\n")
