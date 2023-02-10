
# Ansible Role:  `victoriametrics`

Ansible role to setup [victoriametrics](https://github.com/VictoriaMetrics/VictoriaMetrics).


[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bodsch/ansible-victoriametrics/CI)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-victoriametrics)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-victoriametrics)][releases]

[ci]: https://github.com/bodsch/ansible-victoriametrics/actions
[issues]: https://github.com/bodsch/ansible-victoriametrics/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-victoriametrics/releases

If `latest` is set for `victoriametrics_version`, the role tries to install the latest release version.
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/bin/victoriametrics/${victoriametrics_version}` and later linked to `/usr/bin`.
This should make it possible to downgrade relatively safely.

The Prometheus archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`.
By default it is `${HOME}/.cache/ansible/victoriametrics`.
If this type of installation is not desired, the download can take place directly on the target system.
However, this must be explicitly activated by setting `victoriametrics_direct_download` to `true`.


## Requirements & Dependencies

- None

### Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10
* RedHat based
    - Alma Linux 8
    - Rocky Linux 8
    - Oracle Linux 8

## usage

### default configuration

```yaml
victoriametrics_version: "1.76.1"

victoriametrics_release: {}

victoriametrics_system_user: victoriametrics
victoriametrics_system_group: victoriametrics

victoriametrics_direct_download: false

victoriametrics_service: {}
```

#### `victoriametrics_service`

```yaml
victoriametrics_service:
  log:
    level: info
    format: ""
  web:
    config:
      file: ""
    listen_address: "127.0.0.1:9091"
    telemetry_path: ""
    external_url: ""
    route_prefix: ""
    enable_lifecycle: false
    enable_admin_api: false
  persistence:
    file: ""
    interval: 5m
  push:
    disable_consistency_check: false
```

## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-victoriametrics/tags)!

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
