# Verity Api Collection

This repository contains the `be_networks.verity` Ansible Collection, which is meant to work with Verity 6.5 and greater.

<!--start requires_ansible-->
<!--end requires_ansible-->

## External requirements

Some modules and plugins require external libraries. Please check the
requirements for each plugin or module you use in the documentation to find out
which requirements are needed.

> [!NOTE]
> This collection is designed to work in conjunction with Verity 6.5 and greater.

## Included content

<!--start collection content-->
<!--end collection content-->

## Using this collection

```bash
    ansible-galaxy collection install be_networks.verity
```

You can also include it in a `requirements.yml` file and install it via
`ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
  - name: be_networks.verity
```

To upgrade the collection to the latest available version, run the following
command:

```bash
ansible-galaxy collection install be_networks.verity --upgrade
```

You can also install a specific version of the collection, for example, if you
need to downgrade when something is broken in the latest version (please report
an issue in this repository). Use the following syntax where `X.Y.Z` can be any
[available version](https://galaxy.ansible.com/be_networks/verity):

```bash
ansible-galaxy collection install be_networks.verity:==X.Y.Z
```

See
[Ansible Using Collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
for more details.

<!-- ## Release notes

See the
[changelog](https://github.com/ansible-collections/be_networks.verity/tree/main/CHANGELOG.rst). -->

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
