pkgname = "lzfse"
pkgver = "1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Lzfse compression library and command line tool"
maintainer = "breakgimme <adam@plock.com>"
license = "BSD-3-Clause"
url = "https://github.com/lzfse/lzfse"
source = (
    f"https://github.com/lzfse/lzfse/archive/refs/tags/lzfse-{pkgver}.tar.gz"
)
sha256 = "cf85f373f09e9177c0b21dbfbb427efaedc02d035d2aade65eb58a3cbf9ad267"


def post_install(self):
    self.install_license("LICENSE")
