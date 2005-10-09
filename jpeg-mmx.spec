# TODO
# - cleanups, desc, summary, source (?)
# - -devel, -progs sub packages?
# - shared library?
Summary:	jpeg mmx
Summary(pl):	jpeg mmx
Name:		jpeg-mmx
Version:	1.1.6
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/mjpeg/%{name}-0.1.6.tar.gz
# Source0-md5:	9156c429bd8c4dea65c877c50ed89e15
Patch0:		%{name}-DESTDIR.patch
ExcludeArch:	amd64 ppc
URL:		http://mjpeg.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} install-prog install_real \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README usage.doc wizard.doc change.log libjpeg.doc example.c structure.doc filelist.doc coderules.doc
%{_includedir}/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_mandir}/man1/*
