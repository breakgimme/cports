pkgname = "alsa-ucm-conf-asahi"
pkgver = "6"
pkgrel = 0
arch = ["aarch64"]
depends = ["alsa-ucm-conf"]
pkgdesc = "Alsa UCM configuration for Asahi Linux"
maintainer = "breakgimme <adam@plock.com>"
license = "BSD-3-Clause"
url = "https://github.com/AsahiLinux/alsa-ucm-conf-asahi"
source = f"https://github.com/AsahiLinux/alsa-ucm-conf-asahi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8f4817b76720d86f1894ff6755d26b46a8f8e37868434bd6251e2880ce7a994d"


def install(self):
    self.install_files("ucm2", "usr/share/alsa")
    self.install_license("LICENSE.asahi")
