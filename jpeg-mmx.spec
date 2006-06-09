Summary:	libjpeg library with MMX support
Summary(pl):	Biblioteka libjpeg z obs³ug± MMX
Name:		jpeg-mmx
Version:	0.1.6
Release:	0.1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/mjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	9156c429bd8c4dea65c877c50ed89e15
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-PIC.patch
Patch2:		%{name}-gcc41.patch
# XXX: replace it with real x86_64 port or drop
#Patch1: %{name}-x8664.patch
URL:		http://mjpeg.sourceforge.net/
BuildRequires:	gcc >= 5:3.0
BuildRequires:	nasm
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	/usr/include/jpeg-mmx

%description
jpeg-mmx is a modified version of IJG libjpeg library that can use MMX
extension of x86 processors (if available).

%description -l pl
jpeg-mmx to zmodyfikowana wersja biblioteki IJG libjpeg potrafi±ca
u¿ywaæ rozszerzenia MMX procesorów x86 (je¶li jest dostêpne).

%package libs
Summary:	Shared jpeg-mmx library
Group:		Libraries

%description libs
Shared jpeg-mmx library

%package devel
Summary:	Headers for developing programs using libjpeg
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}

%description devel
The jpeg-mmx-devel package includes the header files and static
libraries necessary for developing programs which will manipulate JPEG
files using the libjpeg library.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%configure \
	--enable-shared \
	--disable-static \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} install_real install-prog \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README usage.doc wizard.doc change.log libjpeg.doc example.c structure.doc filelist.doc coderules.doc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjpeg-mmx.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}
%{_libdir}/libjpeg-mmx.la
%{_libdir}/libjpeg-mmx.so
