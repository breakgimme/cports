pkgname = "asahi-audio"
pkgver = "3.0"
pkgrel = 0
arch = ["aarch64"]
build_style = "makefile"
depends = [
    "bankstown",
    "lsp-plugins-lv2",
    "pipewire",
    "speakersafetyd",
    "triforce",
    "wireplumber",
]
pkgdesc = "Asahi Linux userspace audio configuration"
maintainer = "breakgimme <adam@plock.com>"
license = "MIT"
url = "https://github.com/AsahiLinux/asahi-audio"
source = f"https://github.com/AsahiLinux/asahi-audio/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8fc53e1ca976ed572e5ee9cc39dd682c2542057a0fedb650f5bc66c87805a7ae"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
