#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openjpeg
Version  : 2.5.0
Release  : 7
URL      : https://github.com/uclouvain/openjpeg/archive/v2.5.0/openjpeg-2.5.0.tar.gz
Source0  : https://github.com/uclouvain/openjpeg/archive/v2.5.0/openjpeg-2.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause Libpng MIT
Requires: openjpeg-bin = %{version}-%{release}
Requires: openjpeg-filemap = %{version}-%{release}
Requires: openjpeg-lib = %{version}-%{release}
Requires: openjpeg-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libwebp-dev
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : pkgconfig(lcms2)
BuildRequires : tiff-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev
BuildRequires : zstd-dev

%description
========================================================================
OpenJPIP software 2.1 ReadMe

%package bin
Summary: bin components for the openjpeg package.
Group: Binaries
Requires: openjpeg-license = %{version}-%{release}
Requires: openjpeg-filemap = %{version}-%{release}

%description bin
bin components for the openjpeg package.


%package dev
Summary: dev components for the openjpeg package.
Group: Development
Requires: openjpeg-lib = %{version}-%{release}
Requires: openjpeg-bin = %{version}-%{release}
Provides: openjpeg-devel = %{version}-%{release}
Requires: openjpeg = %{version}-%{release}

%description dev
dev components for the openjpeg package.


%package filemap
Summary: filemap components for the openjpeg package.
Group: Default

%description filemap
filemap components for the openjpeg package.


%package lib
Summary: lib components for the openjpeg package.
Group: Libraries
Requires: openjpeg-license = %{version}-%{release}
Requires: openjpeg-filemap = %{version}-%{release}

%description lib
lib components for the openjpeg package.


%package license
Summary: license components for the openjpeg package.
Group: Default

%description license
license components for the openjpeg package.


%prep
%setup -q -n openjpeg-2.5.0
cd %{_builddir}/openjpeg-2.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652725605
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1652725605
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openjpeg
cp %{_builddir}/openjpeg-2.5.0/LICENSE %{buildroot}/usr/share/package-licenses/openjpeg/a1a529b822da257f69972ea711df38489e9d4251
cp %{_builddir}/openjpeg-2.5.0/src/bin/wx/OPJViewer/source/license.txt %{buildroot}/usr/share/package-licenses/openjpeg/28399384e8bacfe952bb12c4c52a9ba009a9c18d
cp %{_builddir}/openjpeg-2.5.0/thirdparty/astyle/LICENSE.md %{buildroot}/usr/share/package-licenses/openjpeg/3ad29cc31a206b0662eb91917964b82f11b3df16
cp %{_builddir}/openjpeg-2.5.0/thirdparty/liblcms2/COPYING %{buildroot}/usr/share/package-licenses/openjpeg/f595de201a37b00737678b96b4c4a10d5bc5f6d9
cp %{_builddir}/openjpeg-2.5.0/thirdparty/libpng/LICENSE %{buildroot}/usr/share/package-licenses/openjpeg/783722cebfdeba6fa3b211d6fb18d68cc647feb4
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/lib64/
mv %{buildroot}/usr/lib/libopenjp2.so* %{buildroot}/usr/lib64/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/openjpeg-2.5/OpenJPEGConfig.cmake
/usr/lib/openjpeg-2.5/OpenJPEGTargets-relwithdebinfo.cmake
/usr/lib/openjpeg-2.5/OpenJPEGTargets.cmake

%files bin
%defattr(-,root,root,-)
/usr/bin/opj_compress
/usr/bin/opj_decompress
/usr/bin/opj_dump
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/openjpeg-2.5/openjpeg.h
/usr/include/openjpeg-2.5/opj_config.h
/usr/include/openjpeg-2.5/opj_stdint.h
/usr/lib64/libopenjp2.so
/usr/lib64/pkgconfig/libopenjp2.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-openjpeg

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopenjp2.so.2.5.0
/usr/lib64/libopenjp2.so.7
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openjpeg/28399384e8bacfe952bb12c4c52a9ba009a9c18d
/usr/share/package-licenses/openjpeg/3ad29cc31a206b0662eb91917964b82f11b3df16
/usr/share/package-licenses/openjpeg/783722cebfdeba6fa3b211d6fb18d68cc647feb4
/usr/share/package-licenses/openjpeg/a1a529b822da257f69972ea711df38489e9d4251
/usr/share/package-licenses/openjpeg/f595de201a37b00737678b96b4c4a10d5bc5f6d9
