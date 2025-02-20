pkgname = "base-asahi"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64"]
build_style = "meta"
depends = [
    "asahi-scripts",
    "linux-asahi",
    "macsmc-battery-udev",
    "m1n1",
    "u-boot-asahi",
]
pkgdesc = "Chimera base package for Asahi Linux"
maintainer = "breakgimme <adam@plock.com>"
license = "custom:meta"
url = "https://chimera-linux.org"


def install(self):
    self.install_file(
        self.files_path / "99-update-m1n1.sh", "usr/lib/kernel.d", mode=0o755
    )


@subpackage("base-asahi-sound")
def _(self):
    self.subdesc = "sound support"
    self.install_if = [self.parent, "wireplumber"]
    self.depends = [
         "alsa-ucm-conf-asahi",
         "asahi-audio",
    ]
    return []
