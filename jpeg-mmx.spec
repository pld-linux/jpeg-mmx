# TODO: cleanups, desc, summary, source (?)
Summary:	jpeg mmx
Summary(pl):	jpeg mmx
Name:		jpeg-mmx
Version:	1.1.2
Release:	0.2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/mjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	63d871b28cb1524b4cf088155688778d
Patch0:		%{name}-DESTDIR.patch
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
install -d $RPM_BUILD_ROOT{%{_includedir},%{_bindir},%{_libdir},%{_mandir}/man1/}

%{__make} install install-prog DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README usage.doc wizard.doc change.log libjpeg.doc example.c structure.doc filelist.doc coderules.doc
%{_includedir}
%attr(755,root,root)%{_bindir}
%{_libdir}
%{_mandir}/man1/
